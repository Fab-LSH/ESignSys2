from fasc_api.client.corp_client import CorpClient
from fasc_api.client.service_client import ServiceClient
from fasc_api.exception.exceptions import ClientException
from fasc_api.exception.exceptions import ServerException

from init_demo_data import InitDemoData

api_client = InitDemoData.api_client
access_token = ServiceClient.get_access_token_value(api_client)
api_client.set_access_token(access_token)


# 获取个人用户授权链接
def get_crop_auth_url_demo():
    try:
        data = {
            "clientCorpId": "1623621278903943168",
            "accountName": "18723710724",
            "clientUserId":"2131323237107667",
            "corpIdentInfo": {
                "corpName": "包小豸",
                "corpIdentType": "corp",
                "corpIdentNo": "91120225942792064P",
                "legalRepName": "谢明",
                "corpIdentMethod":[]
            },
            "corpNonEditableInfo": [
                "corpName"
            ],
            "oprIdentInfo": {
                "userName": "谢盛",
                "identType": "id_card",
                "userIdentNo": "440306199805201350",
                "mobile": "17000217007",
                "bankAccountNo": "405471244390570096",
                "corpIdentMethod":[]
            },
            "corpIdentType": "corp",
            "corpName": "包小豸",
            "corpIdentNo": "91120225942792064P",
            "corpIdentInfoMatch": False,
            "authScopes": [
                "seal_info",
                "signtask_info"
            ],
            "oprNonEditableInfo":[],
            "redirectUrl": "www.baidu.com"
        }
        res = CorpClient.get_corp_auth_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 禁用企业用户
def disable_corp_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488"
        }
        res = CorpClient.disable(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 恢复企业用户
def enable_corp_demo():
    try:
        data = {
            'openCorpId': InitDemoData.openCorpId
        }
        res = CorpClient.enable(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 解除企业用户授权
def unbind_corp_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488"
        }
        res = CorpClient.unbind(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询企业用户基本信息
def get_detail_corp_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "clientCorpId": "745c3bbcaddc46abbf01cd61e28d7aee"
        }
        res = CorpClient.get_detail(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取企业用户身份信息
def get_identity_info_corp_demo():
    try:
        data = {
            # 法大大平台为该企业在该应用appId范围内分配的唯一标识
            'openCorpId': InitDemoData.openCorpId
        }
        res = CorpClient.get_identity_info(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取企业实名认证状态
def get_identified_status_demo():
    try:
        data = {
            "corpName": "包小豸",
            "corpIdentNo": "1623621278903943168"
        }
        res = CorpClient.get_identified_status(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())

# 查询相对方列表
def get_identified_status_demo():
    try:
        data = {
            "openCorpId": "972f3189db2d48539b984ad3ec491515"
        }
        res = CorpClient.get_counterpart_list(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())



if __name__ == '__main__':
    # 获取授权链接企业
    # get_crop_auth_url_demo()
    # 禁用企业用户
    # disable_corp_demo()
    # 恢复企业用户
    # enable_corp_demo()
    # 解除企业用户授权
    # unbind_corp_demo()
    # 查询企业用户基本信息
    # get_detail_corp_demo()
    # 获取企业实名认证状态
    get_identified_status_demo()

