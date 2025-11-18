from .client import CommonClient
from .client import ApiClient
from ..utils.url_params import OpenApiUrlParams

"""
TemplateClient
模板管理
"""


class TemplateClient(ApiClient):
    # 查询文档模板列表
    def get_doc_template_list(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.DOC_TEMPLATE_GET_LIST, data)

    # 获取文档模板详情
    def get_doc_template_detail(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.DOC_TEMPLATE_GET_DETAIL, data)

    # 查询签署模板列表
    def get_sign_template_list(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TEMPLATE_GET_LIST, data)

    # 获取签署模板详情
    def get_sign_template_detail(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TEMPLATE_GET_DETAIL, data)

    # 获取模板新增链接
    def get_template_create_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TEMPLATE_GET_CREATE_URL, data)

    # 获取模板编辑链接
    def get_template_edit_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TEMPLATE_GET_EDIT_URL, data)

    # 获取模板预览链接
    def get_template_preview_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TEMPLATE_GET_PREVIEW_URL, data)

    # 获取模板管理链接
    def get_template_manage_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TEMPLATE_GET_MANAGE_URL, data)

    # 查询应用文档模板列表
    def get_app_doc_templates(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.APP_DOC_TEMPLATE_GET_LIST, data)

    # 获取应用文档模板详情
    def get_app_doc_template_detail(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.APP_DOC_TEMPLATE_GET_DETAIL, data)

    # 查询应用签署任务模板列表
    def get_app_sign_templates(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.APP_SIGN_TEMPLATE_GET_LIST, data)

    # 获取应用签署任务模板详情
    def get_app_sign_template_detail(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.APP_SIGN_TEMPLATE_GET_DETAIL, data)

    # 获取应用模板新增链接
    def get_app_template_create_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.APP_TEMPLATE_CREATE_GET_URL, data)

    # 获取应用模板编辑链接
    def get_app_template_edit_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.APP_TEMPLATE_EDIT_GET_URL, data)

    # 获取应用模板预览链接
    def get_app_template_preview_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.APP_TEMPLATE_PREVIEW_GET_URL, data)

    # 创建业务控件
    def create_app_field(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.APP_FIELD_CREATE, data)

    # 修改业务控件
    def modify_app_field(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.APP_FIELD_MODIFY, data)

    # 设置业务控件状态
    def set_app_field_status(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.APP_FIELD_SET_STATUS, data)

    # 查询业务控件列表
    def get_app_field_list(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.APP_FIELD_GET_LIST, data)

    # 启用/停用应用文档模板
    def set_app_template_status(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.APP_DOC_TEMPLATE_SET_STATUS, data)

    # 删除应用文档模板
    def delete_app_template(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.APP_DOC_TEMPLATE_DELETE, data)

    # 启用/停用应用签署任务模板
    def set_sign_app_template_status(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.APP_DOC_SIGN_TEMPLATE_SET_STATUS, data)

    # 删除应用文档模板
    def delete_app_sign_template(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.APP_DOC_SIGN_TEMPLATE_DELETE, data)

    # 启用/停用文档模板
    def doc_template_set_status(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.DOC_TEMPLATE_SET_STATUS, data)

    # 删除文档模板
    def doc_template_delete(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.DOC_TEMPLATE_DELETE, data)

    # 启用/停用签署模板
    def sign_template_set_status(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TEMPLATE_SET_STATUS, data)

    # 删除签署模板
    def sign_template_delete(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TEMPLATE_DELETE, data)

    # 新增业务控件
    def create_corp_field(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CREATE_CORP_FIELD, data)

    # 获取业务控件列表
    def get_corp_field_list(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.GET_CORP_FIELD_LIST, data)

    # 删除企业业务控件信息
    def delete_corp_field(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.DELETE_CORP_FIELD, data)

    # 查询印章标签列表
    def seal_tag_get_list(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SEAL_TAG_GET_LIST, data)

    # 创建文档模板
    def doc_template_create(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.DOC_TEMPLATE_CREATE, data)

    # 复制新增文档模板
    def doc_template_copy_create(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.DOC_TEMPLATE_COPY_CREATE, data)

    # 填写文档模板生成接口
    def doc_template_fill_values(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.DOC_TEMPLATE_FILL_VALUES, data)
