from .client import ApiClient
from .client import CommonClient
from ..utils.url_params import OpenApiUrlParams

"""
UserClient
单据管理
"""


class ToolClient(ApiClient):

    # 获取三要素校验
    def get_three_element_verify_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_GET_THREE_ELEMENT_VERIFY_URL, data)

    # 获取四要素校验
    def get_four_element_verify_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_GET_FOUR_ELEMENT_VERIFY_URL, data)

    # 获取要素校验身份证图片下载链接
    def get_user_idcard_image_download_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_GET_IDCARD_IMAGE_DOWNLOAD_URL, data)

    # 个人认证授权管理-身份证OCR
    def user_get_ocr_idcard(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_GET_OCR_IDCARD, data)

    # 个人运营商三要素校验接口版
    def telecom_there_element_verify(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.telecom_there_element_verify, data)

    # 个人银行卡四要素校验接口版
    def bank_four_element_verify(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.bank_four_element_verify, data)

    # 个人银行卡二要素校验接口版
    def bank_two_element_verify(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.bank_two_element_verify, data)

    # 个人银行卡三要素校验
    def user_identity_bank_three_element_verify(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.user_identity_bank_three_element_verify, data)

    # 人脸图片比对校验
    def user_identity_idcard_three_element_verify(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.user_identity_idcard_three_element_verify, data)

    # 获取人脸核验链接
    def user_verify_face_recognition(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_VERIFY_FACE_RECOGNITION, data)

    # 查询人脸核验结果
    def user_verify_face_status_query(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_VERIFY_FACE_STATUS_QUERY, data)

    # 个人认证授权管理-银行卡OCR
    def user_verify_face_status_query(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_OCR_BANKCARD, data)

    # 个人认证授权管理-营业执照OCR
    def user_get_ocr_biz_license(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_GET_OCR_BIZ_LICENSE, data)

    # 个人认证授权管理-驾驶证OCR
    def user_get_ocr_driving_license(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_GET_OCR_DRIVING_LICENSE, data)

    # 个人认证授权管理-行驶证OCR
    def user_get_ocr_vehicle_license(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_GET_OCR_VEHICLE_LICENSE, data)

    # 个人认证授权管理-行驶证OCR
    def user_get_ocr_mainland_permit(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_GET_OCR_MAINLAND_PERMIT, data)

    # 企业组织三要素校验
    def corp_identity_business_three_element_verify(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.corp_identity_business_three_element_verify, data)

    # 企业组织四要素校验
    def corp_identity_business_four_element_verify(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.corp_identity_business_four_element_verify, data)

    # 企业工商信息查询
    def corp_identity_business_info_query(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.corp_identity_business_info_query, data)

    # 银行卡四要素核验
    def user_verify_bankcard_four_element_create(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_VERIFY_BANKCARD_FOUR_ELEMENT_CREATE, data)

    # 手机号三要素核验
    def user_verify_telecom_three_element_create(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_VERIFY_TELECOM_THREE_ELEMENT_CREATE, data)

    # 验证码校验
    def user_verify_auth_code_check(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_VERIFY_AUTH_CODE_CHECK, data)

    # 获取验证码
    def user_verify_auth_code_get(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_VERIFY_AUTH_CODE_GET, data)

    # 获取身份核验详情
    def user_verify_get_detail(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.USER_VERIFY_GET_DETAIL, data)

