from .client import ApiClient, CommonClient
from ..utils.url_params import OpenApiUrlParams

"""
EUIClient
EUI页面资源
"""


class OcrClient(ApiClient):

    # 获取文件对比页面链接
    def get_ocr_edit_compare_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.OCR_EDIT_GET_COMPARE_URL, data)

    # 获取历史文件对比页面链接
    def get_ocr_edit_result_compare_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.OCR_EDIT_GET_RESULT_COMPARE_URL, data)

    # 获取合同智审页面链接
    def get_ocr_edit_examine_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.OCR_EDIT_GET_EXAMINE_URL, data)

    # 获取历史合同智审页面链接
    def get_ocr_edit_result_examine_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.OCR_EDIT_GET_RESULT_EXAMINE_URL, data)

    # 获取历史合同智审数据
    def get_ocr_edit_examine_result_data(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.OCR_EDIT_GET_EXAMINE_RESULT_DATA, data)
