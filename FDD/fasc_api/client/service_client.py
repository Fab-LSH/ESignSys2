from .client import CommonClient
from .client import ApiClient
from ..utils.url_params import OpenApiUrlParams

"""
ServiceClient
服务访问凭证
"""


class ServiceClient(ApiClient):
    # 获取服务访问凭证
    def get_access_token(self):
        return CommonClient.post_json(self, OpenApiUrlParams.SERVICE_GET_ACCESS_TOKEN, None)

    # 获取服务访问凭证
    def get_access_token_value(self):
        res = ServiceClient.get_access_token(self)
        return res['data']['accessToken']

    # # 获取应用级资源访问凭证
    # def get_app_access_ticket(self):
    #     return CommonClient.post_json(self, OpenApiUrlParams.SERVICE_GET_APP_ACCESS_TICKET, None)
    #
    # # 获取用户级资源访问凭证
    # def get_user_access_ticket(self):
    #     return CommonClient.post_json(self, OpenApiUrlParams.SERVICE_GET_USER_ACCESS_TICKET, None)
