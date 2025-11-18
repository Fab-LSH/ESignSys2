import json
import os
from datetime import datetime
from pathlib import Path

class Config:
    """配置管理类"""
    
    def __init__(self):
        # 获取项目根目录（backend/src -> backend -> 项目根目录）
        self.project_root = Path(__file__).parent.parent.parent
        self.config_path = self.project_root / 'config.json'
        
        self.config = self.load_config()
        
    def load_config(self):
        """从config.json加载配置"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                print(f"✓ 配置加载成功: {self.config_path}")
                return config
        except Exception as e:
            print(f"✗ 读取配置文件失败: {e}")
            return {}
    
    # 法大大API配置
    @property
    def app_id(self):
        return self.config.get('ESIGN_APP_ID', '')
    
    @property
    def app_secret(self):
        return self.config.get('ESIGN_APP_SECRET', '')
    
    @property
    def request_url(self):
        return self.config.get('ESIGN_REQUEST_URL', '')
    
    @property
    def access_token(self):
        return self.config.get('ESIGN_ACCESS_TOKEN', '')
    
    @access_token.setter
    def access_token(self, value):
        self.config['ESIGN_ACCESS_TOKEN'] = value
        self.save_config()
    
    @property
    def file_type(self):
        return self.config.get('ESIGN_FILE_TYPE', 'pdf')
    
    @property
    def id_type(self):
        return self.config.get('ESIGN_ID_TYPE', '')
    
    @property
    def corp_id(self):
        return self.config.get('ESIGN_CORP_ID', '')
    
    @property
    def business_id(self):
        return self.config.get('ESIGN_BUSINESS_ID', '')
    
    @business_id.setter
    def business_id(self, value):
        self.config['ESIGN_BUSINESS_ID'] = value
        self.save_config()

# 创建全局配置实例
config = Config()