import json

from fasc_api.client.approve_client import ApproveClient
from fasc_api.client.service_client import ServiceClient
from fasc_api.exception.exceptions import ClientException
from fasc_api.exception.exceptions import ServerException
from fasc_api.utils.url_params import OpenApiUrlParams
from init_demo_data import InitDemoData

api_client = InitDemoData.api_client
access_token = ServiceClient.get_access_token_value(api_client)
api_client.set_access_token(access_token)


# 获取审批链接
def approval_get_url_demo():
    try:
        data = {
            "openCorpId": "972f3189db2d48539b984ad3ec491515",
            "clientUserId": "qq1686214278242151536",
            "approvalId": "1686314714361147677",
            "redirectUrl": "https://www.fadada.com/hetongmuban/list-13?option=2"
        }
        res = ApproveClient.approval_get_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取审批列表
def approval_get_list_demo():
    try:
        data = {
            "openCorpId": "972f3189db2d48539b984ad3ec491515",
            "approvalType": "sign_task_start",
            "listPageNo": 1,
            "listPageSize": 50
        }
        res = ApproveClient.approval_get_list(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# # 获取审批详情
def approval_get_detail_demo():
    try:
        data = {
            "openCorpId": "972f3189db2d48539b984ad3ec491515",
            "approvalType": "sign_task_start",
            "approvalId": "1686555671817175095"
        }
        res = ApproveClient.approval_get_detail(api_client, data)
        print(json.dumps(res))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取服务访问凭证
def get_access_token_value(self):
    from fasc_api.client.client import CommonClient
    res = CommonClient.post_json(self, OpenApiUrlParams.SERVICE_GET_ACCESS_TOKEN, None)
    return res['data']['accessToken']


if __name__ == '__main__':
    # 获取审批链接
    approval_get_url_demo()
    # 获取审批列表
    # approval_get_list_demo()
    # 获取审批详情
    # approval_get_detail_demo()
