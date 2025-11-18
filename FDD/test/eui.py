from fasc_api.client.service_client import ServiceClient
from fasc_api.exception.exceptions import ClientException
from fasc_api.exception.exceptions import ServerException
from fasc_api.client.eui_client import EUIClient

from init_demo_data import InitDemoData

api_client = InitDemoData.api_client
access_token = ServiceClient.get_access_token_value(api_client)
api_client.set_access_token(access_token)


# 获取计费账户链接
def get_bill_url_demo():
    try:
        data = {
            "openId": {
                "idType": "person",
                "openId": "aeeb1f1bf6f349e89915a9701793d1bd"
            },
            "urlType": "account",
            "redirectUrl": "https://www.baidu.com/",
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = EUIClient.get_bill_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取应用级资源访问链接
def get_app_page_resource_url_demo():
    try:
        data = {
            "ownerId": {
                "idType": "String",
                "openId": "String"
            },
            "resource": {
                "resourceId": "String",
                "action": "String",
                "params": "String"
            },
            "accessToken": "String"
        }
        res = EUIClient.get_app_page_resource_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取用户级资源访问链接
def get_user_page_resource_url_demo():
    try:
        data = {
            "openCorpId": "String",
            "clientUserId": "String",
            "resource": {
                "resourceId": "String",
                "action": "String",
                "params": "String"
            },
            "accessToken": "String"
        }
        res = EUIClient.get_user_page_resource_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


if __name__ == '__main__':
    # 获取计费链接
    get_bill_url_demo()
    # 获取应用级资源访问链接
    get_app_page_resource_url_demo()
    # 获取用户级资源访问链接
    # get_user_page_resource_url_demo()
