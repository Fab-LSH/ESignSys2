from .client import CommonClient
from .client import ApiClient
from ..utils.url_params import OpenApiUrlParams

"""
UserClient
个人用户帐号管理
"""


class UserClient(ApiClient):

    # 禁用个人用户
    def disable(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_DISABLE, data)

    # 恢复个人用户
    def enable(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_ENABLE, data)

    # 查询个人用户基本信息
    def get(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_GET, data)

    # 查询个人用户基本信息
    def get_identity_info(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_GET_IDENTITY_INFO, data)

    # 解绑个人用户账号
    def unbind(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_UNBIND, data)

    #  获取用户实名信息
    def get_user_auth_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_GET_AUTH_URL, data)



