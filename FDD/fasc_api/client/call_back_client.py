from .client import ApiClient
from .client import CommonClient
from ..utils.url_params import OpenApiUrlParams

"""
CorpClient
回调
"""
class CallBackClient(ApiClient):

    # 获取回调列表
    def get_call_back_list(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.GET_CALL_BACK_LIST, data)
