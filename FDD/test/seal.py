from fasc_api.client.seal_client import SealClient
from fasc_api.client.service_client import ServiceClient
from fasc_api.exception.exceptions import ClientException
from fasc_api.exception.exceptions import ServerException

from init_demo_data import InitDemoData

api_client = InitDemoData.api_client
access_token = ServiceClient.get_access_token_value(api_client)
api_client.set_access_token(access_token)


# 查询印章列表
def get_seal_list_demo():
    try:
        data = {
            "openCorpId": "1cfbd982ebde44beb6e57578d8a5bb24",
            "listFilter": {
                "categoryType": ""
            },
            "grantFreeSign": "no_free_sign",
        }
        res = SealClient.get_seal_list(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询印章详情
def get_seal_detail_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "sealId": 19800
        }
        res = SealClient.get_seal_detail(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取指定印章详情链接
def get_appointed_seal_url_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "sealId": 184386,
            "clientUserId": "AutoClientUserId1656985245",
            "redirectUrl": "http://www.baidu.com"
        }
        res = SealClient.get_appointed_seal_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询企业用印员列表
def get_seal_user_list_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "listFilter": {
                "categoryType": [
                    "official_seal"
                ]
            }
        }
        res = SealClient.get_seal_user_list(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询指定成员的印章列表
def get_user_seal_list_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "memberId": 1980,
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = SealClient.get_user_seal_list(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取印章创建链接
def get_seal_create_url_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "clientUserId": "AutoClientUserId1656985245",
            "sealName": "法人章",
            "categoryType": "official_seal",
            "sealTag": "合同使用",
            "createSerialNo": "191115",
            "redirectUrl": "http://www.baidu.com"
        }
        res = SealClient.get_seal_create_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询审核中的印章列表
def get_seal_verify_list_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488"
        }
        res = SealClient.get_seal_verify_list(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 修改印章基本信息
def modify_seal_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "sealId": 34220,
            "sealName": "法人章",
            "categoryType": "official_seal",
            "sealTag": "测试"
        }
        res = SealClient.modify_seal(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取设置用印员链接
def get_seal_grant_url_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "sealId": 34220,
            "memberInfo": {
                "memberIds": [
                    0
                ],
                "grantStartTime": "1677115605000",
                "grantEndTime": "1677215605000"
            },
            "clientUserId": "AutoClientUserId1656985245",
            "redirectUrl": "http://www.baidu.com"
        }
        res = SealClient.get_seal_grant_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取设置企业印章免验证签链接
def get_seal_free_sign_url_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "clientUserId": "AutoClientUserId1656985245",
            "sealId": 34220,
            "businessId": "342",
            "email": "1677116109675@fdd.com",
            "expiresTime": "1677115605000",
            "redirectUrl": "http://www.baidu.com"
        }
        res = SealClient.get_seal_free_sign_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 解除印章授权
def cancel_seal_grant_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "sealId": 184386,
            "memberId": "1656985245"
        }
        res = SealClient.cancel_seal_grant(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 设置印章状态
def set_seal_status_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "sealId": 34220,
            "sealStatus": "enable"
        }
        res = SealClient.set_seal_status(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 删除印章
def delete_seal_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "sealId": 34220
        }
        res = SealClient.delete_seal(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取印章管理链接
def get_seal_manage_url_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "clientUserId": "AutoClientUserId1656985245",
            "redirectUrl": "http://www.baidu.com"
        }
        res = SealClient.get_seal_manage_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询个人签名列表
def get_personal_seal_list_demo():
    try:
        data = {
            "openUserId": "745c3bbcaddc46abbf01cd61e28d7aee"
        }
        res = SealClient.get_personal_seal_list(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取设置个人签名免验证签链接
def get_personal_seal_free_sign_url_demo():
    try:
        data = {
            "openUserId": "220146e34b3d403c8fb46d3f4b7c5fde",
            "sealIds": [1683538027890119554],
            "businessId": "cd5e672775fa9d85e8c2017d5a0c84f7",
            # "email": "1677116109675@fdd.com",
            # "expiresTime": "1677115605000",
            "redirectUrl": "http://www.baidu.com"
        }
        res = SealClient.get_personal_seal_free_sign_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 解除印章免验证签
def cancel_seal_free_sign_demo():
    try:
        data = {
            "accessToken": "a7b018b6ec8c492593e0f84dca9a5fbc",
            "openCorpId": "faad7b0b566b40dab8ba75cee7f9c672",
            "sealId": 1683538712239131962,
            "businessId": "cd5e672775fa9d85e8c2017d5a0c84f7"
        }
        res = SealClient.cancel_seal_free_sign(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 解除签名免验证签
def personal_seal_free_sign_cancel_demo():
    try:
        data = {
            "openUserId": "220146e34b3d403c8fb46d3f4b7c5fde",
            "sealId": 1683538027890119554,
            "businessId": "cd5e672775fa9d85e8c2017d5a0c84f7",
        }

        res = SealClient.personal_seal_free_sign_cancel(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取签名管理链接
def personal_seal_get_manage_url_demo():
    try:
        data = {
            "openUserId": "f608140fa01f4d829aa3ab298b24d1d3",
            "redirectUrl": "http://www.baidu.com"
        }

        res = SealClient.personal_seal_get_manage_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取签名创建链接
def personal_seal_get_create_url_demo():
    try:
        data = {
            "clientUserId": "AutoClientUserId16569852456",
            "createSerialNo": "zpt123",
            "redirectUrl": "http://www.baidu.com"
        }
        res = SealClient.personal_seal_get_create_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 删除个人签名
def personal_seal_delete_demo():
    try:
        data = {
            "openUserId": "f608140fa01f4d829aa3ab298b24d1d3",
            "sealId": "1686711139652190725"
        }
        res = SealClient.personal_seal_delete(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 创建模板印章
def seal_create_by_template_demo():
    try:
        data = {
            "accessToken": "a7b018b6ec8c492593e0f84dca9a5fbc",
            "openCorpId": "1cfbd982ebde44beb6e57578d8a5bb24",
            "sealName": "SDK测试印章"
        }
        res = SealClient.seal_create_by_template(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 创建图片印章
def seal_create_by_image_demo():
    try:
        data = {
            "sealImage": "",
            "openCorpId": "1cfbd982ebde44beb6e57578d8a5bb24",
            "sealName": "SDK测试印章"}
        res = SealClient.seal_create_by_image(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())

# 	创建法定代表人模板印章
def seal_create_legal_representative_by_template_demo():
    try:
        data = {
            "openCorpId": "1cfbd982ebde44beb6e57578d8a5bb24",
            "openUserId": "f608140fa01f4d829aa3ab298b24d1d3",
            "sealName": "SDK测试模板法人章"
        }
        res = SealClient.seal_create_legal_representative_by_template(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())

# 	创建法定代表人图片印章
def seal_create_legal_representative_by_image_demo():
    try:
        data = {
            "sealImage": "",
            "openCorpId": "1cfbd982ebde44beb6e57578d8a5bb24",
            "openUserId": "f608140fa01f4d829aa3ab298b24d1d3",
            "sealName": "SDK测试图片法人章"
        }
        res = SealClient.seal_create_legal_representative_by_image(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())

# 	创建模板签名
def personal_seal_create_by_template_demo():
    try:
        data = {
            "openUserId": "f608140fa01f4d829aa3ab298b24d1d3",
            "sealName": "SDK测试模板签名"
        }
        res = SealClient.personal_seal_create_by_template(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 	创建图片签名
def personal_seal_create_by_image_demo():
    try:
        data = {
            "sealImage": "",
            "openUserId": "f608140fa01f4d829aa3ab298b24d1d3",
            "sealName": "SDK测试图片签名"
        }
        res = SealClient.personal_seal_create_by_image(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


if __name__ == '__main__':
    # # 查询印章列表
    # get_seal_list_demo()
    # # 查询印章详情
    # get_seal_detail_demo()
    # # 获取指定印章详情链接
    # get_appointed_seal_url_demo()
    # # 查询企业用印员列表
    # get_seal_user_list_demo()
    # # 查询指定成员的印章列表
    # get_user_seal_list_demo()
    # # 获取印章创建链接
    # get_seal_create_url_demo()
    # # 查询审核中的印章列表
    # get_seal_verify_list_demo()
    # # 修改印章基本信息
    # modify_seal_demo()
    # # 获取设置用印员链接
    # get_seal_grant_url_demo()
    # # 获取设置企业印章免验证签链接
    # get_seal_free_sign_url_demo()
    # # 解除印章授权
    # cancel_seal_grant_demo()
    # # 设置印章状态
    # set_seal_status_demo()
    # # 删除印章
    # delete_seal_demo()
    # # 获取印章管理链接
    # get_seal_manage_url_demo()
    # # 查询个人签名列表
    # get_personal_seal_list_demo()
    # # 获取设置个人签名免验证签链接
    # get_personal_seal_free_sign_url_demo()
    # 解除印章免验证签
    # cancel_seal_free_sign_demo()
    # 解除签名免验证签
    # personal_seal_free_sign_cancel_demo()
    # # 获取签名管理链接
    # personal_seal_get_manage_url_demo()
    # # 签名创建链接
    # personal_seal_get_create_url_demo()
    # 删除个人签名
    # personal_seal_delete_demo()
    # 创建模板印章
    seal_create_by_template_demo()
    # 创建模板印章
    seal_create_by_image_demo()
    # 创建法定代表人模板印章
    seal_create_legal_representative_by_template_demo()
    # 	创建法定代表人图片印章
    seal_create_legal_representative_by_image_demo()
    # 创建模板签名
    personal_seal_create_by_template_demo()
    # 创建图片签名
    personal_seal_create_by_image_demo()