from .client import ApiClient
from .client import CommonClient
from ..utils.url_params import OpenApiUrlParams

"""
UserClient
单据管理
"""


class VoucherClient(ApiClient):

    # 单据创建
    def voucher_task_create(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.voucher_task_create, data)

    # 单据详情
    def voucher_task_detail(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.voucher_task_detail, data)

    # 单据列表
    def voucher_task_list(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.voucher_task_list, data)

    # 单据文件下载
    def voucher_task_download(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.voucher_task_download, data)

    # 单据撤销
    def voucher_task_cancel(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.voucher_task_cancel, data)

    #  单据签署链接
    def voucher_task_actor_get_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.voucher_task_actor_get_url, data)
