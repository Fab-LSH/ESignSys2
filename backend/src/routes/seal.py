from flask import Blueprint, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os
import uuid
from src.models.user import db
from src.models.seal import Seal

seal_bp = Blueprint('seal', __name__)

# 配置上传文件夹
UPLOAD_FOLDER = 'uploads/seals'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def ensure_upload_folder():
    """确保上传文件夹存在"""
    upload_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), UPLOAD_FOLDER)
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)
    return upload_path

@seal_bp.route('/upload', methods=['POST'])
def upload_seal():
    """上传印章"""
    try:
        # 检查文件
        if 'seal_image' not in request.files:
            return jsonify({'error': '缺少印章图片文件'}), 400
        
        file = request.files['seal_image']
        if file.filename == '':
            return jsonify({'error': '未选择文件'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': '不支持的文件格式，请上传PNG或JPG格式'}), 400
        
        # 获取表单数据
        seal_name = request.form.get('seal_name')
        seal_type = request.form.get('seal_type', 'official')
        user_id = request.form.get('user_id', 1)  # 默认用户ID为1
        
        if not seal_name:
            return jsonify({'error': '缺少印章名称'}), 400
        
        # 确保上传文件夹存在
        upload_path = ensure_upload_folder()
        
        # 保存文件
        filename = secure_filename(file.filename)
        file_id = str(uuid.uuid4())
        file_path = os.path.join(upload_path, f"{file_id}_{filename}")
        file.save(file_path)
        
        # 创建印章记录
        seal = Seal(
            user_id=user_id,
            name=seal_name,
            image_path=file_path,
            seal_type=seal_type
        )
        
        db.session.add(seal)
        db.session.commit()
        
        return jsonify({
            'message': '印章上传成功',
            'seal_id': seal.id,
            'seal': seal.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'上传失败: {str(e)}'}), 500

@seal_bp.route('/list')
def list_seals():
    """获取印章列表"""
    try:
        user_id = request.args.get('user_id', 1)
        seals = Seal.query.filter_by(user_id=user_id).order_by(Seal.created_at.desc()).all()
        
        return jsonify({
            'seals': [seal.to_dict() for seal in seals]
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'获取印章列表失败: {str(e)}'}), 500

@seal_bp.route('/<int:seal_id>')
def get_seal(seal_id):
    """获取单个印章信息"""
    try:
        seal = Seal.query.get_or_404(seal_id)
        return jsonify({'seal': seal.to_dict()}), 200
        
    except Exception as e:
        return jsonify({'error': f'获取印章信息失败: {str(e)}'}), 500

@seal_bp.route('/<int:seal_id>/image')
def get_seal_image(seal_id):
    """获取印章图片"""
    try:
        seal = Seal.query.get_or_404(seal_id)
        
        if not os.path.exists(seal.image_path):
            return jsonify({'error': '印章图片不存在'}), 404
        
        return send_file(seal.image_path, as_attachment=False)
        
    except Exception as e:
        return jsonify({'error': f'获取印章图片失败: {str(e)}'}), 500

@seal_bp.route('/<int:seal_id>', methods=['PUT'])
def update_seal(seal_id):
    """更新印章信息"""
    try:
        seal = Seal.query.get_or_404(seal_id)
        
        data = request.get_json()
        
        if 'name' in data:
            seal.name = data['name']
        if 'seal_type' in data:
            seal.seal_type = data['seal_type']
        
        db.session.commit()
        
        return jsonify({
            'message': '印章信息更新成功',
            'seal': seal.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'更新失败: {str(e)}'}), 500

@seal_bp.route('/<int:seal_id>', methods=['DELETE'])
def delete_seal(seal_id):
    """删除印章"""
    try:
        seal = Seal.query.get_or_404(seal_id)
        
        # 删除文件
        if os.path.exists(seal.image_path):
            os.remove(seal.image_path)
        
        # 删除数据库记录
        db.session.delete(seal)
        db.session.commit()
        
        return jsonify({'message': '印章删除成功'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'删除失败: {str(e)}'}), 500

@seal_bp.route('/<int:seal_id>/replace', methods=['POST'])
def replace_seal_image(seal_id):
    """替换印章图片"""
    try:
        seal = Seal.query.get_or_404(seal_id)
        
        # 检查文件
        if 'seal_image' not in request.files:
            return jsonify({'error': '缺少印章图片文件'}), 400
        
        file = request.files['seal_image']
        if file.filename == '':
            return jsonify({'error': '未选择文件'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': '不支持的文件格式，请上传PNG或JPG格式'}), 400
        
        # 删除旧文件
        if os.path.exists(seal.image_path):
            os.remove(seal.image_path)
        
        # 确保上传文件夹存在
        upload_path = ensure_upload_folder()
        
        # 保存新文件
        filename = secure_filename(file.filename)
        file_id = str(uuid.uuid4())
        file_path = os.path.join(upload_path, f"{file_id}_{filename}")
        file.save(file_path)
        
        # 更新数据库记录
        seal.image_path = file_path
        db.session.commit()
        
        return jsonify({
            'message': '印章图片替换成功',
            'seal': seal.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'替换失败: {str(e)}'}), 500

