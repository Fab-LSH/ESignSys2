import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.models.contract import Contract, Attachment
from src.models.user import db
from main import app  # 直接复用 main.py 里的 app

with app.app_context():
    # 删除所有附件文件
    attachments = Attachment.query.all()
    for att in attachments:
        if hasattr(att, 'attachment_path') and att.attachment_path and os.path.exists(att.attachment_path):
            try:
                os.remove(att.attachment_path)
                print(f"已删除附件文件: {att.attachment_path}")
            except Exception as e:
                print(f"删除附件文件失败: {att.attachment_path}, {e}")

    # 删除所有合同PDF文件
    contracts = Contract.query.all()
    for contract in contracts:
        if contract.original_pdf_path and os.path.exists(contract.original_pdf_path):
            try:
                os.remove(contract.original_pdf_path)
                print(f"已删除原始合同: {contract.original_pdf_path}")
            except Exception as e:
                print(f"删除原始合同失败: {contract.original_pdf_path}, {e}")
        if contract.stamped_pdf_path and os.path.exists(contract.stamped_pdf_path):
            try:
                os.remove(contract.stamped_pdf_path)
                print(f"已删除盖章合同: {contract.stamped_pdf_path}")
            except Exception as e:
                print(f"删除盖章合同失败: {contract.stamped_pdf_path}, {e}")

    # 删除数据库记录
    Attachment.query.delete()
    Contract.query.delete()
    db.session.commit()
    print("所有合同及附件数据库记录已删除。")