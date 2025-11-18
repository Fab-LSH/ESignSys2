from .client import CommonClient
from .client import ApiClient
from ..utils.url_params import OpenApiUrlParams


"""
CorpClient
审批管理
"""
class ApproveClient(ApiClient):

    # 获取审批链接
    def approval_get_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.APPROVAL_GET_URL, data)

    # 获取审批列表
    def approval_get_list(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.APPROVAL_GET_LIST, data)

    # 获取审批详情
    def approval_get_detail(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.APPROVAL_GET_DETAIL, data)
