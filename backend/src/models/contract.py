from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from src.models.user import db
import json

class Contract(db.Model):
    __tablename__ = 'contracts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    contract_number = db.Column(db.String(100), nullable=False)
    counterparty_abbr = db.Column(db.String(100), nullable=False)
    contract_name = db.Column(db.String(200), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    original_pdf_path = db.Column(db.String(255), nullable=False)
    stamped_pdf_path = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(50), default='uploaded')  # uploaded, processing, stamped, confirmed
    ai_suggested_positions = db.Column(db.Text, nullable=True)  # JSON string
    final_stamp_positions = db.Column(db.Text, nullable=True)  # JSON string
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 关联用户
    user = db.relationship('User', backref=db.backref('contracts', lazy=True))
    
    def get_ai_suggested_positions(self):
        if self.ai_suggested_positions:
            return json.loads(self.ai_suggested_positions)
        return []
    
    def set_ai_suggested_positions(self, positions):
        self.ai_suggested_positions = json.dumps(positions)
    
    def get_final_stamp_positions(self):
        if self.final_stamp_positions:
            return json.loads(self.final_stamp_positions)
        return []
    
    def set_final_stamp_positions(self, positions):
        self.final_stamp_positions = json.dumps(positions)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'contract_number': self.contract_number,
            'counterparty_abbr': self.counterparty_abbr,
            'contract_name': self.contract_name,
            'upload_date': self.upload_date.isoformat() if self.upload_date else None,
            'original_pdf_path': self.original_pdf_path,
            'stamped_pdf_path': self.stamped_pdf_path,
            'status': self.status,
            'ai_suggested_positions': self.get_ai_suggested_positions(),
            'final_stamp_positions': self.get_final_stamp_positions(),
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class Attachment(db.Model):
    __tablename__ = 'attachments'
    
    id = db.Column(db.Integer, primary_key=True)
    contract_id = db.Column(db.Integer, db.ForeignKey('contracts.id'), nullable=False)
    attachment_path = db.Column(db.String(255), nullable=False)
    filename = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # 关联合同
    contract = db.relationship('Contract', backref=db.backref('attachments', lazy=True))
    
    def to_dict(self):
        return {
            'id': self.id,
            'contract_id': self.contract_id,
            'attachment_path': self.attachment_path,
            'filename': self.filename,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

