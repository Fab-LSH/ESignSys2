import os
import fitz  # PyMuPDF
from PyPDF2 import PdfMerger
from PIL import Image
import io
import json
from datetime import datetime

class PDFProcessor:
    def __init__(self):
        pass
    
    def merge_pdfs(self, main_pdf_path, attachment_paths, output_path):
        """合并主合同和附件PDF"""
        try:
            merger = PdfMerger()
            
            # 添加主合同
            merger.append(main_pdf_path)
            
            # 添加附件
            for attachment_path in attachment_paths:
                if os.path.exists(attachment_path):
                    merger.append(attachment_path)
            
            # 保存合并后的PDF
            with open(output_path, 'wb') as output_file:
                merger.write(output_file)
            
            merger.close()
            return True
        except Exception as e:
            print(f"PDF合并错误: {e}")
            return False
    
    def add_text_to_pdf(self, pdf_path, output_path, contract_number, date_str):
        """在PDF上添加合同编号和日期"""
        try:
            doc = fitz.open(pdf_path)
            
            # 在第一页添加合同编号和日期
            page = doc[0]
            
            # 获取页面尺寸
            rect = page.rect
            
            # 在页面右上角添加合同编号
            contract_text = f"合同编号: {contract_number}"
            date_text = f"日期: {date_str}"
            
            # 添加文本
            page.insert_text(
                (rect.width - 200, 30),  # 右上角位置
                contract_text,
                fontsize=10,
                color=(0, 0, 0)
            )
            
            page.insert_text(
                (rect.width - 200, 50),  # 合同编号下方
                date_text,
                fontsize=10,
                color=(0, 0, 0)
            )
            
            doc.save(output_path)
            doc.close()
            return True
        except Exception as e:
            print(f"添加文本错误: {e}")
            return False
    
    def add_stamp_to_pdf(self, pdf_path, output_path, stamp_image_path, positions):
        """在PDF上加盖印章"""
        try:
            doc = fitz.open(pdf_path)
            
            for position in positions:
                page_num = position.get('page', 0)
                x = position.get('x', 0)
                y = position.get('y', 0)
                width = position.get('width', 100)
                height = position.get('height', 100)
                
                if page_num < len(doc):
                    page = doc[page_num]
                    
                    # 插入印章图片
                    rect = fitz.Rect(x, y, x + width, y + height)
                    page.insert_image(rect, filename=stamp_image_path)
            
            # 添加骑缝章
            self._add_cross_page_stamps(doc, stamp_image_path)
            
            doc.save(output_path)
            doc.close()
            return True
        except Exception as e:
            print(f"加盖印章错误: {e}")
            return False
    
    def _add_cross_page_stamps(self, doc, stamp_image_path):
        """添加骑缝章"""
        try:
            # 在每两页之间的边缘添加骑缝章
            for i in range(len(doc) - 1):
                page = doc[i]
                rect = page.rect
                
                # 在页面右边缘添加骑缝章
                stamp_rect = fitz.Rect(
                    rect.width - 30,  # 右边缘
                    rect.height / 2 - 25,  # 中间位置
                    rect.width - 5,
                    rect.height / 2 + 25
                )
                page.insert_image(stamp_rect, filename=stamp_image_path)
        except Exception as e:
            print(f"添加骑缝章错误: {e}")
    
    def extract_text_and_positions(self, pdf_path):
        """提取PDF文本和位置信息，用于AI识别盖章位置"""
        try:
            doc = fitz.open(pdf_path)
            text_data = []
            
            for page_num in range(len(doc)):
                page = doc[page_num]
                
                # 提取文本块
                text_dict = page.get_text("dict")
                
                page_data = {
                    'page': page_num,
                    'width': page.rect.width,
                    'height': page.rect.height,
                    'text_blocks': []
                }
                
                for block in text_dict["blocks"]:
                    if "lines" in block:
                        for line in block["lines"]:
                            for span in line["spans"]:
                                text_block = {
                                    'text': span["text"],
                                    'bbox': span["bbox"],  # [x0, y0, x1, y1]
                                    'font': span["font"],
                                    'size': span["size"]
                                }
                                page_data['text_blocks'].append(text_block)
                
                text_data.append(page_data)
            
            doc.close()
            return text_data
        except Exception as e:
            print(f"提取文本错误: {e}")
            return []
    
    def convert_pdf_page_to_image(self, pdf_path, page_num=0):
        """将PDF页面转换为图片"""
        try:
            doc = fitz.open(pdf_path)
            page = doc[page_num]
            
            # 渲染页面为图片
            mat = fitz.Matrix(2, 2)  # 放大2倍
            pix = page.get_pixmap(matrix=mat)
            
            # 转换为PIL Image
            img_data = pix.tobytes("png")
            img = Image.open(io.BytesIO(img_data))
            
            doc.close()
            return img
        except Exception as e:
            print(f"PDF转图片错误: {e}")
            return None
    
    def generate_filename(self, contract_number, counterparty_abbr, contract_name):
        """生成文件名"""
        # 清理文件名中的特殊字符
        safe_contract_number = "".join(c for c in contract_number if c.isalnum() or c in ('-', '_'))
        safe_counterparty = "".join(c for c in counterparty_abbr if c.isalnum() or c in ('-', '_'))
        safe_contract_name = "".join(c for c in contract_name if c.isalnum() or c in ('-', '_', '（', '）', '(', ')'))
        
        filename = f"{safe_contract_number}-{safe_counterparty}-{safe_contract_name}.pdf"
        return filename

