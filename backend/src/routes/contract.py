from flask import Blueprint, request, jsonify, current_app, send_file
from werkzeug.utils import secure_filename
import os
import uuid
from datetime import datetime
from src.models.user import db
from src.models.contract import Contract, Attachment
from src.utils.pdf_processor import PDFProcessor
from src.utils.ai_position_detector import AIPositionDetector

contract_bp = Blueprint('contract', __name__)

# 配置上传文件夹
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def ensure_upload_folder():
    """确保上传文件夹存在"""
    upload_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), UPLOAD_FOLDER)
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)
    return upload_path

@contract_bp.route('/upload', methods=['POST'])
def upload_contract():
    """上传合同和附件"""
    try:
        # 检查必要的表单数据
        if 'main_contract' not in request.files:
            return jsonify({'error': '缺少主合同文件'}), 400
        
        main_contract = request.files['main_contract']
        if main_contract.filename == '':
            return jsonify({'error': '未选择主合同文件'}), 400
        
        if not allowed_file(main_contract.filename):
            return jsonify({'error': '不支持的文件格式'}), 400
        
        # 获取表单数据
        contract_number = request.form.get('contract_number')
        counterparty_abbr = request.form.get('counterparty_abbr')
        contract_name = request.form.get('contract_name')
        user_id = request.form.get('user_id', 1)  # 默认用户ID为1
        
        if not all([contract_number, counterparty_abbr, contract_name]):
            return jsonify({'error': '缺少必要的合同信息'}), 400
        
        # 确保上传文件夹存在
        upload_path = ensure_upload_folder()
        
        # 保存主合同
        main_filename = secure_filename(main_contract.filename)
        main_file_id = str(uuid.uuid4())
        main_file_path = os.path.join(upload_path, f"{main_file_id}_{main_filename}")
        main_contract.save(main_file_path)
        
        # 创建合同记录
        contract = Contract(
            user_id=user_id,
            contract_number=contract_number,
            counterparty_abbr=counterparty_abbr,
            contract_name=contract_name,
            original_pdf_path=main_file_path,
            status='uploaded'
        )
        
        db.session.add(contract)
        db.session.flush()  # 获取contract.id
        
        # 处理附件
        attachment_paths = []
        attachments = request.files.getlist('attachments')
        
        for attachment in attachments:
            if attachment and attachment.filename != '' and allowed_file(attachment.filename):
                att_filename = secure_filename(attachment.filename)
                att_file_id = str(uuid.uuid4())
                att_file_path = os.path.join(upload_path, f"{att_file_id}_{att_filename}")
                attachment.save(att_file_path)
                attachment_paths.append(att_file_path)
                
                # 创建附件记录
                att_record = Attachment(
                    contract_id=contract.id,
                    attachment_path=att_file_path,
                    filename=att_filename
                )
                db.session.add(att_record)
        
        # 合并PDF
        pdf_processor = PDFProcessor()
        merged_filename = f"merged_{main_file_id}.pdf"
        merged_path = os.path.join(upload_path, merged_filename)
        
        if pdf_processor.merge_pdfs(main_file_path, attachment_paths, merged_path):
            contract.original_pdf_path = merged_path
        
        db.session.commit()
        
        return jsonify({
            'message': '文件上传成功',
            'contract_id': contract.id,
            'contract': contract.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'上传失败: {str(e)}'}), 500

@contract_bp.route('/analyze/<int:contract_id>', methods=['POST'])
def analyze_contract(contract_id):
    """AI分析合同，识别盖章位置"""
    try:
        contract = Contract.query.get_or_404(contract_id)
        
        if not os.path.exists(contract.original_pdf_path):
            return jsonify({'error': '合同文件不存在'}), 404
        
        # 提取PDF文本和位置信息
        pdf_processor = PDFProcessor()
        text_data = pdf_processor.extract_text_and_positions(contract.original_pdf_path)
        
        if not text_data:
            return jsonify({'error': 'PDF文本提取失败'}), 500
        
        # AI识别盖章位置
        ai_detector = AIPositionDetector()
        suggested_positions = ai_detector.detect_stamp_positions(text_data)
        
        # 保存AI建议的位置
        contract.set_ai_suggested_positions(suggested_positions)
        contract.status = 'analyzed'
        db.session.commit()
        
        return jsonify({
            'message': 'AI分析完成',
            'contract_id': contract.id,
            'suggested_positions': suggested_positions
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'分析失败: {str(e)}'}), 500

@contract_bp.route('/preview/<int:contract_id>')
def preview_contract(contract_id):
    """预览合同PDF"""
    try:
        contract = Contract.query.get_or_404(contract_id)
        
        if not os.path.exists(contract.original_pdf_path):
            return jsonify({'error': '合同文件不存在'}), 404
        
        return send_file(contract.original_pdf_path, as_attachment=False)
        
    except Exception as e:
        return jsonify({'error': f'预览失败: {str(e)}'}), 500

@contract_bp.route('/stamp/<int:contract_id>', methods=['POST'])
def stamp_contract(contract_id):
    """加盖印章"""
    try:
        contract = Contract.query.get_or_404(contract_id)
        
        if not os.path.exists(contract.original_pdf_path):
            return jsonify({'error': '合同文件不存在'}), 404
        
        # 获取印章位置和印章文件
        data = request.get_json()
        stamp_positions = data.get('stamp_positions', [])
        seal_id = data.get('seal_id')
        
        if not stamp_positions:
            return jsonify({'error': '缺少印章位置信息'}), 400

        # 使用真实印章图片
        if not seal_id:
            return jsonify({'error': '缺少印章ID'}), 400

        from src.models.seal import Seal
        seal = Seal.query.get(seal_id)
        if not seal or not seal.image_path or not os.path.exists(seal.image_path):
            return jsonify({'error': '印章图片不存在'}), 404

        stamp_image_path = seal.image_path
        
        # 生成输出文件名
        pdf_processor = PDFProcessor()
        output_filename = pdf_processor.generate_filename(
            contract.contract_number,
            contract.counterparty_abbr,
            contract.contract_name
        )
        
        upload_path = ensure_upload_folder()
        output_path = os.path.join(upload_path, output_filename)
        
        # 先添加文本信息
        temp_path = os.path.join(upload_path, f"temp_{contract.id}.pdf")
        current_date = datetime.now().strftime("%Y年%m月%d日")
        
        if not pdf_processor.add_text_to_pdf(
            contract.original_pdf_path, 
            temp_path, 
            contract.contract_number, 
            current_date
        ):
            return jsonify({'error': '添加文本信息失败'}), 500
        
        # 加盖印章
        if not pdf_processor.add_stamp_to_pdf(
            temp_path, 
            output_path, 
            stamp_image_path, 
            stamp_positions
        ):
            return jsonify({'error': '加盖印章失败'}), 500
        
        # 清理临时文件
        if os.path.exists(temp_path):
            os.remove(temp_path)
        
        # 更新合同记录
        contract.stamped_pdf_path = output_path
        contract.set_final_stamp_positions(stamp_positions)
        contract.status = 'stamped'
        db.session.commit()
        
        return jsonify({
            'message': '印章加盖成功',
            'contract_id': contract.id,
            'download_filename': output_filename
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'加盖印章失败: {str(e)}'}), 500

@contract_bp.route('/download/<int:contract_id>')
def download_contract(contract_id):
    """下载已盖章的合同"""
    try:
        contract = Contract.query.get_or_404(contract_id)
        
        if not contract.stamped_pdf_path or not os.path.exists(contract.stamped_pdf_path):
            return jsonify({'error': '盖章文件不存在'}), 404
        
        # 生成下载文件名
        pdf_processor = PDFProcessor()
        download_filename = pdf_processor.generate_filename(
            contract.contract_number,
            contract.counterparty_abbr,
            contract.contract_name
        )
        
        return send_file(
            contract.stamped_pdf_path, 
            as_attachment=True,
            download_name=download_filename
        )
        
    except Exception as e:
        return jsonify({'error': f'下载失败: {str(e)}'}), 500

@contract_bp.route('/list')
def list_contracts():
    """获取合同列表"""
    try:
        user_id = request.args.get('user_id', 1)
        contracts = Contract.query.filter_by(user_id=user_id).order_by(Contract.created_at.desc()).all()
        
        return jsonify({
            'contracts': [contract.to_dict() for contract in contracts]
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'获取合同列表失败: {str(e)}'}), 500

@contract_bp.route('/confirm/<int:contract_id>', methods=['POST'])
def confirm_contract(contract_id):
    """法务确认合同"""
    try:
        contract = Contract.query.get_or_404(contract_id)
        
        data = request.get_json()
        action = data.get('action')  # 'approve' 或 'reject'
        comment = data.get('comment', '')
        
        if action == 'approve':
            contract.status = 'confirmed'
        elif action == 'reject':
            contract.status = 'rejected'
        else:
            return jsonify({'error': '无效的操作'}), 400
        
        db.session.commit()
        
        return jsonify({
            'message': f'合同已{action}',
            'contract_id': contract.id,
            'status': contract.status
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'确认失败: {str(e)}'}), 500

@contract_bp.route('/preview_final')
def preview_final():
    """
    根据合同编号、签约对方简称、合同名称查找已盖章合同并预览
    前端参数：contract_number, counterparty_abbr, contract_name
    """
    try:
        contract_number = request.args.get('contract_number')
        counterparty_abbr = request.args.get('counterparty_abbr')
        contract_name = request.args.get('contract_name')

        if not all([contract_number, counterparty_abbr, contract_name]):
            return jsonify({'error': '缺少必要参数'}), 400

        contract = Contract.query.filter_by(
            contract_number=contract_number,
            counterparty_abbr=counterparty_abbr,
            contract_name=contract_name
        ).first()

        if not contract:
            return jsonify({'error': '未找到对应合同'}), 404

        if not contract.stamped_pdf_path or not os.path.exists(contract.stamped_pdf_path):
            return jsonify({'error': '盖章文件不存在'}), 404

        return send_file(contract.stamped_pdf_path, as_attachment=False)
    except Exception as e:
        return jsonify({'error': f'预览失败: {str(e)}'}), 500

def _create_default_seal(output_path):
    """创建默认印章图片"""
    from PIL import Image, ImageDraw, ImageFont
    
    # 创建一个红色圆形印章
    size = (100, 100)
    img = Image.new('RGBA', size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # 画红色圆圈
    draw.ellipse([5, 5, 95, 95], outline=(255, 0, 0, 255), width=3)
    
    # 添加文字
    try:
        # 尝试使用系统字体
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
    except:
        font = ImageFont.load_default()
    
    text = "电子印章"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    
    draw.text((x, y), text, fill=(255, 0, 0, 255), font=font)
    
    # 确保目录存在
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)

