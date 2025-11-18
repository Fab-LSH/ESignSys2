from fasc_api.client.approve_client import ApproveClient
from fasc_api.client.call_back_client import CallBackClient
from fasc_api.client.service_client import ServiceClient
from fasc_api.exception.exceptions import ClientException
from fasc_api.exception.exceptions import ServerException

from init_demo_data import InitDemoData

api_client = InitDemoData.api_client
access_token = ServiceClient.get_access_token_value(api_client)
api_client.set_access_token(access_token)


# 获取审批列表
def get_call_back_list_demo():
    try:
        data = {
            "callbackType": "approval",
            "startTime": "1685779302000",
            "endTime": "1686645975188",
            "listPageNo": 1,
            "listPageSize": 10
        }
        res = CallBackClient.get_call_back_list(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


if __name__ == '__main__':
    # 获取审批列表
    get_call_back_list_demo()
