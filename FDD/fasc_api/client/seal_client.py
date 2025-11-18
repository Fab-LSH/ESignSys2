from .client import CommonClient
from .client import ApiClient
from ..utils.url_params import OpenApiUrlParams

"""
SealClient
组织架构管理
"""


class SealClient(ApiClient):

    # 查询印章列表
    def get_seal_list(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SEAL_GET_LIST, data)

    # 查询印章详情
    def get_seal_detail(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SEAL_GET_DETAIL, data)

    # 获取指定印章详情链接
    def get_appointed_seal_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SEAL_GET_APPOINTED_URL, data)

    # 查询企业用印员列表
    def get_seal_user_list(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SEAL_GET_USER_LIST, data)

    # 查询指定成员的印章列表
    def get_user_seal_list(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.GET_USER_SEAL_LIST, data)

    # 获取印章创建链接
    def get_seal_create_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SEAL_GET_CREATE_URL, data)

    # 查询审核中的印章列表
    def get_seal_verify_list(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SEAL_GET_VERIFY_LIST, data)

    # 修改印章基本信息
    def modify_seal(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SEAL_MODIFY, data)

    # 获取设置用印员链接(获取印章授权给成员链接)
    def get_seal_grant_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SEAL_GET_GRANT_URL, data)

    # 获取设置企业印章免验证签链接
    def get_seal_free_sign_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SEAL_GET_FREE_SIGN_URL, data)

    # 解除印章授权
    def cancel_seal_grant(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SEAL_CANCEL_GRANT, data)

    # 设置印章状态
    def set_seal_status(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SEAL_SET_STATUS, data)

    # 删除印章
    def delete_seal(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SEAL_DELETE, data)

    # 获取印章管理链接
    def get_seal_manage_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SEAL_GET_MANAGE_URL, data)

    # 查询个人签名列表
    def get_personal_seal_list(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.PERSONAL_SEAL_GET_LIST, data)

    # 获取设置个人签名免验证签链接
    def get_personal_seal_free_sign_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.PERSONAL_SEAL_GET_FREE_SIGN_URL, data)

    # 解除印章免验证签
    def cancel_seal_free_sign(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CANCEL_SEAL_FREE_SIGN, data)

    # 解除签名免验证签
    def personal_seal_free_sign_cancel(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.PERSONAL_SEAL_FREE_SIGN_CANCEL, data)

    # 获取签名管理链接
    def personal_seal_get_manage_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.PERSONAL_SEAL_GET_MANAGE_URL, data)

    # 获取签名创建链接
    def personal_seal_get_create_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.PERSONAL_SEAL_GET_CREATE_URL, data)

    # 删除个人签名
    def personal_seal_delete(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.PERSONAL_SEAL_DELETE, data)

    # 创建模板印章
    def seal_create_by_template(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SEAL_CREATE_BY_TEMPLATE, data)

    # 创建图片印章
    def seal_create_by_image(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SEAL_CREATE_BY_IMAGE, data)

     # 	创建法定代表人模板印章
    def seal_create_legal_representative_by_template(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SEAL_CREATE_LEGAL_REPRESENTATIVE_BY_TEMPLATE, data)

    # 	创建法定代表人图片印章
    def seal_create_legal_representative_by_image(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SEAL_CREATE_LEGAL_REPRESENTATIVE_BY_IMAGE, data)

    # 	创建模板签名
    def personal_seal_create_by_template(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.PERSONAL_SEAL_CREATE_BY_TEMPLATE, data)

    # 	创建图片签名
    def personal_seal_create_by_image(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.PERSONAL_SEAL_CREATE_BY_IMAGE, data)

