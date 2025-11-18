from .client import ApiClient, CommonClient
from ..utils.url_params import OpenApiUrlParams

"""
EUIClient
EUI页面资源
"""


class EUIClient(ApiClient):

    # 获取计费链接
    def get_bill_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.BILLING_GET_BILL_URL, data)

    # 获取应用级资源访问链接
    def get_app_page_resource_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.APP_PAGE_RESOURCE_GET_URL, data)

    # 获取用户级资源访问链接
    def get_user_page_resource_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_PAGE_RESOURCE_GET_URL, data)
