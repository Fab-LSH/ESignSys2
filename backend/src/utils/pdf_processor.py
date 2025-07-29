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
            # page.insert_text(
            #     (rect.width - 200, 30),  # 右上角位置
            #     contract_text,
            #     fontsize=10,
            #     color=(0, 0, 0)
            # )
            
            # page.insert_text(
            #     (rect.width - 200, 50),  # 合同编号下方
            #     date_text,
            #     fontsize=10,
            #     color=(0, 0, 0)
            # )
            
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
                page = doc[0]
                # PyMuPDF默认单位为pt，1pt=1/72英寸
                # 页面宽度（像素）= 页面宽度（pt）/ 72 * DPI
                # 但fitz的rect.width就是像素
                # 这里假设页面分辨率为72dpi，如果有更高分辨率可自定义
                dpi = 72
                # 如果页面有实际像素信息，可用 page.get_pixmap().width / page.rect.width * 72
                # 这里采用标准72dpi
                # 40mm转像素
                mm = 40
                width = height = int(mm / 25.4 * dpi)
                # width = position.get('width', 120)
                # height = position.get('height', 120)
                
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
        """骑缝章：将印章图片等分为N份，分别盖在每页边缘，整体宽度为40mm，按DPI换算像素"""
        try:
            from PIL import Image
            import io

            num_pages = len(doc)
            if num_pages < 2:
                return  # 单页无需骑缝章

            # 计算DPI（以第一页为准）
            page = doc[0]
            # PyMuPDF默认单位为pt，1pt=1/72英寸
            # 页面宽度（像素）= 页面宽度（pt）/ 72 * DPI
            # 但fitz的rect.width就是像素
            # 这里假设页面分辨率为72dpi，如果有更高分辨率可自定义
            dpi = 72
            # 如果页面有实际像素信息，可用 page.get_pixmap().width / page.rect.width * 72
            # 这里采用标准72dpi
            # 40mm转像素
            mm = 40
            px_total_width = int(mm / 25.4 * dpi)
            px_height = px_total_width  # 高度也为40mm对应像素

            # 打开骑缝章图片
            stamp_img = Image.open(stamp_image_path).convert("RGBA")
            w, h = stamp_img.size

            # 每页分配的宽度
            part_width = px_total_width // num_pages

            for i in range(num_pages):
                left = i * (w // num_pages)
                right = left + (w // num_pages) if i < num_pages - 1 else w
                part_img = stamp_img.crop((left, 0, right, h))

                # 每页骑缝章尺寸：宽度为part_width，高度为px_height
                part_img_resized = part_img.resize((part_width, px_height), Image.LANCZOS)

                img_bytes = io.BytesIO()
                part_img_resized.save(img_bytes, format="PNG")
                img_bytes.seek(0)

                # 盖在页面右侧中间，距离边缘5像素
                page = doc[i]
                rect = page.rect
                x0 = rect.width - part_width - 5
                y0 = (rect.height - px_height) / 2
                x1 = rect.width - 5
                y1 = y0 + px_height
                stamp_rect = fitz.Rect(x0, y0, x1, y1)
                page.insert_image(stamp_rect, stream=img_bytes.getvalue(), overlay=True)
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
        
        filename = f"{safe_contract_number}{safe_counterparty}{safe_contract_name}.pdf"
        return filename

