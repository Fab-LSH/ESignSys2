from fasc_api.client.service_client import ServiceClient
from fasc_api.client.user_client import UserClient
from fasc_api.exception.exceptions import ClientException
from fasc_api.exception.exceptions import ServerException

from init_demo_data import InitDemoData

api_client = InitDemoData.api_client
access_token = ServiceClient.get_access_token_value(api_client)
api_client.set_access_token(access_token)


# 禁用个人用户
def disable_demo():
    try:
        data = {
            "openUserId": "745c3bbcaddc46abbf01cd61e28d7aee"
        }
        res = UserClient.disable(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 恢复个人用户
def enable_demo():
    try:
        data = {
            "openUserId": "745c3bbcaddc46abbf01cd61e28d7aee"
        }
        res = UserClient.enable(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询个人用户基本信息
def get_demo():
    try:
        data = {
            "clientUserId": "745c3bbcaddc46abbf01cd61e28d7aee",
            # "openUserId": "79650673d131498b8832c21732e91e84",
        }
        res = UserClient.get(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取用户实名信息
def get_identity_info_demo():
    try:
        data = {
            "openUserId": "75e54d7b08854b6aadaefdfd2b2e7f11"
        }
        res = UserClient.get_identity_info(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 解除个人用户授权
def unbind_demo():
    try:
        data = {
            "openUserId": "745c3bbcaddc46abbf01cd61e28d7aee"
        }
        res = UserClient.unbind(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


#  获取个人用户授权链接
def get_user_auth_url_demo():
    try:
        data = {
            "clientUserId": "AutoClientIdUser1677050079018",
            "userName": "谢盛",
            "userIdentType": "id_card",
            "userIdentNo": "440306199803096833",
            "userIdentInfoMatch": False,
            "authScopes": [
                "ident_info"
            ],
            "redirectUrl": "https://www.fadada.com/hetongmuban/list-13?option=1",
            "accountName": "v5test1677050079018@fdd.com",
            "userIdentInfo": {
                "userName": "谢盛",
                "userIdentType": "id_card",
                "userIdentNo": "440306199803096833",
                "mobile": "13616523633",
                "bankAccountNo": "6226455636772293",
                "identMethod": [
                    "mobile"
                ]
            },
            "nonEditableInfo": [
                "mobile"
            ],
            "unbindAccount": False,
        }
        res = UserClient.get_user_auth_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


if __name__ == '__main__':
    # # 禁用个人用户
    # disable_demo()
    # # 恢复个人用户
    # enable_demo()
    # # 解除个人用户授权
    # unbind_demo()
    # # 获取用户实名信息
    # get_identity_info_demo()
    # # 查询个人用户基本信息
    # get_demo()
    # # 获取个人用户授权链接
    get_user_auth_url_demo()
