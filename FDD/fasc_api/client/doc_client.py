from .client import CommonClient
from .client import ApiClient
from ..utils.url_params import OpenApiUrlParams

"""
DocClient
文档管理
"""


class DocClient(ApiClient):

    # 通过网络文件地址上传
    def file_upload_by_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.FILE_UPLOAD_BY_URL, data)

    # 获取上传文件地址
    def file_get_upload_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.FILE_GET_UPLOAD_URL, data)

    # 文件处理
    def file_process(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.FILE_PROCESS, data)

    # 文档验签
    def file_verify_sign(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.DOC_POST_FILE_VERIFY_SIGN, data)

    # 关键字坐标查询
    def file_get_keyword_positions(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.FILE_GET_KEYWORD_POSITIONS, data)
