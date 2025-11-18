from fasc_api.client.service_client import ServiceClient
from fasc_api.client.template_client import TemplateClient
from fasc_api.exception.exceptions import ClientException
from fasc_api.exception.exceptions import ServerException

from init_demo_data import InitDemoData

api_client = InitDemoData.api_client
access_token = ServiceClient.get_access_token_value(api_client)
api_client.set_access_token(access_token)


# 查询文档模板列表
def get_doc_template_list_demo():
    try:
        data = {
            "ownerId": {
                "idType": "corp",
                "openId": "1623621278903943168"
            },
            "listFilter": {
                "docTemplateName": "测试模板"
            },
            "listPageNo": "2",
            "listPageSize": "4"
        }
        res = TemplateClient.get_doc_template_list(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取文档模板详情
def get_doc_template_detail_demo():
    try:
        data = {
            "ownerId": {
                "idType": "corp",
                "openId": "1623621278903943168"
            },
            "docTemplateId": 0
        }
        res = TemplateClient.get_doc_template_detail(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询签署模板列表
def get_sign_template_list_demo():
    try:
        data = {
            "ownerId": {
                "idType": "corp",
                "openId": "1623621278903943168"
            },
            "listFilte": {
                "signTemplateName": "模板1"
            },
            "listPageNo": 1,
            "listPageSize": 20,
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = TemplateClient.get_sign_template_list(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取签署模板详情
def get_sign_template_detail_demo():
    try:
        data = {
            "ownerId": {
                "idType": "corp",
                "openId": "1623621278903943168"
            },
            "signTemplateId": "423342"
        }
        res = TemplateClient.get_sign_template_detail(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取模板新增链接
def get_template_create_url_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "type": "doc",
            "createSerialNo": "05689",
            "redirectUrl": "http://www.baidu.com"
        }
        res = TemplateClient.get_template_create_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取模板编辑链接
def get_template_edit_url_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "templateId": "doc",
            "redirectUrl": "http://www.baidu.com"
        }
        res = TemplateClient.get_template_edit_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取模板预览链接
def get_template_preview_url_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "templateId": "doc",
            "redirectUrl": "http://www.baidu.com"
        }
        res = TemplateClient.get_template_preview_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取模板管理链接
def get_template_manage_url_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "redirectUrl": "http://www.baidu.com"
        }
        res = TemplateClient.get_template_manage_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询应用文档模板列表
def get_app_doc_templates_demo():
    try:
        data = {
            "listFilter": {
                "appDocTemplateName": "测试应用模板"
            },
            "listPageNo": 0,
            "listPageSize": 10,
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = TemplateClient.get_app_doc_templates(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取应用文档模板详情
def get_app_doc_template_detail_demo():
    try:
        data = {
            "appDocTemplateId": "18439",
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = TemplateClient.get_app_doc_template_detail(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询应用签署任务模板列表
def get_app_sign_templates_demo():
    try:
        data = {
            "listFilter": {
                "appDocTemplateName": "测试应用模板"
            },
            "listPageNo": 0,
            "listPageSize": 10
        }
        res = TemplateClient.get_app_sign_templates(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取应用签署任务模板详情
def get_app_sign_template_detail_demo():
    try:
        data = {
            "appSignTemplateId": "18438605689"
        }
        res = TemplateClient.get_app_sign_template_detail(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取应用模板新增链接
def get_app_template_create_url_demo():
    try:
        data = {
            "type": "doc",
            "createSerialNo": "18438605689",
            "redirectUrl": "www.baidu.com"
        }
        res = TemplateClient.get_app_template_create_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取应用模板编辑链接
def get_app_template_edit_url_demo():
    try:
        data = {
            "appTemplateId": "18438605689",
            "redirectUrl": "www.baidu.com"
        }
        res = TemplateClient.get_app_template_edit_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取应用模板预览链接
def get_app_template_preview_url_demo():
    try:
        data = {
            "appTemplateId": "18438605689",
            "redirectUrl": "www.baidu.com"
        }
        res = TemplateClient.get_app_template_preview_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 创建业务控件
def create_app_field_demo():
    try:
        data = {
            "fieldKey": "18438605689",
            "fieldName": "控件名1",
            "fieldType": "text_single_line"
        }
        res = TemplateClient.create_app_field(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 修改业务控件
def modify_app_field_demo():
    try:
        data = {
            "fieldKey": "18438605689",
            "fieldName": "控件名2"
        }
        res = TemplateClient.modify_app_field(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 设置业务控件状态
def set_app_field_status_demo():
    try:
        data = {
            "fieldKey": "18438605689",
            "fieldStatus": "enable"
        }
        res = TemplateClient.set_app_field_status(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询业务控件列表
def get_app_field_list_demo():
    try:
        data = {
            "fieldKey": "18438605689"
        }
        res = TemplateClient.get_app_field_list(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 启用/停用应用文档模板
def set_app_template_status_demo():
    try:
        data = {
            "appDocTemplateId": "1231231",
            "appDocTemplateStatus": "invalid"
        }
        res = TemplateClient.set_app_template_status(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 删除应用文档模板
def delete_app_template_demo():
    try:
        data = {
            "appDocTemplateId": "1231231"
        }
        res = TemplateClient.delete_app_template(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 启用/停用应用签署任务模板
def set_sign_app_template_status_demo():
    try:
        data = {
            "appSignTemplateId": "1231231",
            "appSignTemplateStatus": "invalid"
        }
        res = TemplateClient.set_sign_app_template_status(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 删除应用文档模板
def delete_app_sign_template_demo():
    try:
        data = {
            "appSignTemplateId": "1231231"
        }
        res = TemplateClient.delete_app_sign_template(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 启用/停用文档模板
def doc_template_set_status_demo():
    try:
        data = {
            "openCorpId": "faad7b0b566b40dab8ba75cee7f9c672",
            "docTemplateId": "1683539217157153212",
            "docTemplateStatus": "valid"
        }
        res = TemplateClient.doc_template_set_status(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 删除文档模板
def doc_template_delete_demo():
    try:
        data = {
            "docTemplateId": "1683539217157153212",
            "openCorpId": "faad7b0b566b40dab8ba75cee7f9c672"
        }

        res = TemplateClient.doc_template_delete(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 启用/停用签署模板
def sign_template_set_status_demo():
    try:
        data = {
            "openCorpId": "faad7b0b566b40dab8ba75cee7f9c672",
            "signTemplateId": "1683539054112118249",
            "signTemplateStatus": "valid"
        }
        res = TemplateClient.sign_template_set_status(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 删除签署模板
def sign_template_delete_demo():
    try:
        data = {
            "signTemplateId": "1683539054112118249",
            "openCorpId": "faad7b0b566b40dab8ba75cee7f9c672"
        }
        res = TemplateClient.sign_template_delete(api_client, data)
        print(jsres)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 创建企业业务控件
def create_corp_field_demo():
    try:
        data = {
            "openCorpId": "23322343535ert",
            "fields": [
                {
                    "fieldName": "业务控件6",
                    "fieldType": "multi_checkbox",
                    "fieldMultiCheckbox": {
                        "required": false,
                        "option": ["owieow", "jsdks", "ksjdksdls"],
                    }
                },
                {
                    "fieldName": "业务控件7",
                    "fieldType": "text_single_line",
                    "fieldTextSingleLine": {
                        "tips": "skdjsdlsdsdskdks",
                        "fontType": "songti"
                    }
                }
            ]
        }
        res = TemplateClient.create_corp_field(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取企业业务控件信息
def get_corp_field_list_demo():
    try:
        data = {
            "signTemplateId": "1683539054112118249",
            "openCorpId": "faad7b0b566b40dab8ba75cee7f9c672"
        }
        res = TemplateClient.get_corp_field_list(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 删除企业业务控件信息
def delete_corp_field_demo():
    try:
        data = {
            "fieldKey": "18438605689",
            "fieldName": "控件名2"
        }
        res = TemplateClient.delete_corp_field(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询印章标签列表
def seal_tag_get_list_demo():
    try:
        data = {
            "openCorpId": "3276823742762365",
        }
        res = TemplateClient.seal_tag_get_list(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 创建文档模板
def doc_template_create_demo():
    try:
        data = {
            "openCorpId": "3276823742762365",
            "docTemplateName": "",
            "createSerialNo": "",
            "fileId": ""
        }
        res = TemplateClient.doc_template_create(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 复制新增文档模板
def doc_template_copy_create_demo():
    try:
        data = {
            "accessToken": "a7b018b6ec8c492593e0f84dca9a5fbc",
            "openCorpId": "1cfbd982ebde44beb6e57578d8a5bb24",
            "docTemplateId": "1689839609131141352",
            "docTemplateName": "复制出的文档模板",
            "createSerialNo": "1691042552885"
        }
        res = TemplateClient.doc_template_copy_create(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())

# 填写文档模板生成接口
def doc_template_fill_values_demo():
    try:
        data = {
            "openCorpId": "c5aa3ea8db994fb3b8138a5ba86a63f4",
            "docTemplateId": "1691137930100157021",
            "fileName": "fileName1691649494",
            "docFieldValues": [
                {
                    "fieldId": "单行文本",
                    "fieldName": "单行文本",
                    "fieldValue": "单行文本默认值"
                },
                {
                    "fieldId": "多行文本",
                    "fieldName": "多行文本",
                    "fieldValue": "多行文本默认值"
                }
            ]
        }
        res = TemplateClient.doc_template_fill_values(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


if __name__ == '__main__':
    # # 查询文档模板列表
    # get_doc_template_list_demo()
    # # 获取文档模板详情
    # get_doc_template_detail_demo()
    # # 查询签署模板列表
    # get_sign_template_list_demo()
    # # 获取签署模板详情
    # get_sign_template_detail_demo()
    # # 获取模板新增链接
    # get_template_create_url_demo()
    # # 获取模板编辑链接
    # get_template_edit_url_demo()
    # # 获取模板预览链接
    # get_template_preview_url_demo()
    # # 查询应用文档模板列表
    # get_app_doc_templates_demo()
    # # 获取应用文档模板详情
    # get_app_doc_template_detail_demo()
    # # 查询应用签署任务模板列表
    # get_app_sign_templates_demo()
    # # 获取应用签署任务模板详情
    # get_app_sign_template_detail_demo()
    # # 获取应用模板新增链接
    # get_app_template_create_url_demo()
    # # 获取应用模板编辑链接
    # get_app_template_edit_url_demo()
    # # 获取应用模板预览链接
    # get_app_template_preview_url_demo()
    # # 创建业务控件
    # create_app_field_demo()
    # # 修改业务控件
    # modify_app_field_demo()
    # # 设置业务控件状态
    # set_app_field_status_demo()
    # # 查询业务控件列表
    # get_app_field_list_demo()
    #
    # # 启用/停用应用文档模板
    # set_app_template_status_demo()
    # # 删除应用文档模板
    # delete_app_template_demo()
    # # 启用/停用应用签署任务模板
    # set_sign_app_template_status_demo()
    # # 删除应用文档模板
    # delete_app_sign_template_demo()

    # 启用/停用文档模板
    # doc_template_set_status_demo()
    # 删除文档模板
    # doc_template_delete_demo()
    # 启用/停用签署模板
    # sign_template_set_status_demo()
    # 删除签署模板
    # sign_template_delete_demo()
    # 删除企业业务控件信息
    # delete_corp_field_demo()
    # # 获取企业业务控件信息
    # get_corp_field_list_demo()
    # # 创建企业业务控件
    # create_corp_field_demo()
    # 查询印章标签列表
    # seal_tag_get_list_demo()
    # 创建文档模板
    # doc_template_create_demo()
    # 复制新增文档模板
    # doc_template_copy_create_demo()
    # 填写文档模板生成接口
    doc_template_fill_values_demo()