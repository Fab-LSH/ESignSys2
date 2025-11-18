from .client import CommonClient
from .client import ApiClient
from ..utils.url_params import OpenApiUrlParams

"""
CorpClient
企业用户帐号管理
"""


class CorpClient(ApiClient):

    # 获取企业认证链接
    def get_corp_auth_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CORP_GET_AUTH_URL, data)

    # 禁用企业用户
    def disable(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CORP_DISABLE, data)

    # 恢复企业用户
    def enable(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CORP_ENABLE, data)

    # 查询企业用户基本信息
    def get_detail(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CORP_GET_DETAIL, data)

    # 解除企业用户授权
    def unbind(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CORP_UNBIND, data)

    # 获取企业用户身份信息
    def get_identity_info(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CORP_GET_IDENTITY_INFO, data)

    # 获取业实名认证状态
    def get_identified_status(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CORP_GET_IDENTIFIED_STATUS, data)

    # 查询相对方
    def get_counterpart_list(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.COUNTERPART_GET_LIST, data)