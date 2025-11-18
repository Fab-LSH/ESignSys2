from fasc_api.client.service_client import ServiceClient
from fasc_api.client.voucher_client import VoucherClient
from fasc_api.exception.exceptions import ClientException
from fasc_api.exception.exceptions import ServerException

from init_demo_data import InitDemoData

api_client = InitDemoData.api_client
access_token = ServiceClient.get_access_token_value(api_client)
api_client.set_access_token(access_token)


# 单据创建
def voucher_task_create_demo():
    try:
        data = {
            "initiator": {
                "idType": "corp",
                "openId": "972f3189db2d48539b984ad3ec491515"
            },
            "signTaskSubject": "签署任务模板发起V5.1签署任务-1694671943",
            "transReferenceId": "456",
            "docs": [
                {
                    "docId": "测试文档",
                    "docName": "测试文档",
                    "docTemplateId": "1693972174827151841"
                }
            ],
            "attachs": [
                {
                    "attachId": "attachId1",
                    "attachName": "附件名1",
                    "attachFileId": "1694406112553133105"
                },
                {
                    "attachId": "attachId2",
                    "attachName": "附件名2",
                    "attachFileId": "1694584251120145201"
                }
            ],
            "actors": [
                {
                    "actorId": "参与方2",
                    "actorName": "李小二",
                    "signConfigInfo": {
                        "signerSignMethod": "ai_hand_write",
                        "readingToEnd": True,
                        "readingTime": "8"
                    },
                    "fillFields": [
                        {
                            "fieldDocId": "测试文档",
                            "fieldId": "单行文本2",
                            "fieldName": "单行文本",
                            "fieldValue": "单行文本1默认值"
                        },
                        {
                            "fieldDocId": "测试文档",
                            "fieldId": "多行文本2",
                            "fieldName": "多行文本",
                            "fieldValue": "多行文本默认值"
                        },
                        {
                            "fieldDocId": "测试文档",
                            "fieldId": "表格2",
                            "fieldName": "表格",
                            "fieldValue": ""
                        }
                    ],
                    "signFields": [
                        {
                            "fieldDocId": "测试文档",
                            "fieldId": "个人签名2",
                            "fieldName": "个人签名"
                        }
                    ]
                },
                {
                    "actorId": "参与方1",
                    "actorName": "王二小",
                    "signConfigInfo": {
                        "signerSignMethod": "hand_write",
                        "readingToEnd": True,
                        "readingTime": "8"
                    },
                    "fillFields": [
                        {
                            "fieldDocId": "测试文档",
                            "fieldId": "单行文本1",
                            "fieldName": "单行文本",
                            "fieldValue": "单行文本1默认值"
                        },
                        {
                            "fieldDocId": "测试文档",
                            "fieldId": "多行文本1",
                            "fieldName": "多行文本",
                            "fieldValue": "多行文本默认值"
                        },
                        {
                            "fieldDocId": "测试文档",
                            "fieldId": "表格1",
                            "fieldName": "表格",
                            "fieldValue": ""
                        }
                    ],
                    "signFields": [
                        {
                            "fieldDocId": "测试文档",
                            "fieldId": "个人签名1",
                            "fieldName": "个人签名"
                        }
                    ]
                }
            ]
        }
        res = VoucherClient.voucher_task_create(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 单据详情
def voucher_task_detail_demo():
    try:
        data = {
            "signTaskId": "1699315365090713600"
        }
        res = VoucherClient.voucher_task_detail(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 单据列表
def voucher_task_list_demo():
    try:
        data = {
            "initiator": {
                "idType": "corp",
                "openId": "972f3189db2d48539b984ad3ec491515"

            },
            "signTaskListFilter": {
                "signTaskSubject": "签署任务",
                "signTaskStatus": [
                    "sign_progress"
                ]
            },
            "listPageNo": 1,
            "listPageSize": 10
        }
        res = VoucherClient.voucher_task_list(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 单据文件下载
def voucher_task_download_demo():
    try:
        data = {
            "ownerId": {
                "idType": "corp",
                "openId": "972f3189db2d48539b984ad3ec491515"
            },
            "signTaskId": "1701837582592581632",
            "fileType": "doc",
            "id": "测试文档"
        }
        res = VoucherClient.voucher_task_download(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 单据撤销
def voucher_task_cancel_demo():
    try:
        data = {
            "signTaskId": "1701837582592581632",
            "terminationNote": "测试撤回"
        }
        res = VoucherClient.voucher_task_cancel(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 单据签署链接
def voucher_task_actor_get_url_demo():
    try:
        data = {
            "actorId": "参与方1",
            "signTaskId": "1701837582592581632"
        }
        res = VoucherClient.voucher_task_actor_get_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


if __name__ == '__main__':
    # 单据创建
    voucher_task_create_demo()
    # 单据详情
    voucher_task_detail_demo()
    # 单据列表
    voucher_task_list_demo()
    # # 单据文件下载
    voucher_task_download_demo()
    # # 单据撤销
    voucher_task_cancel_demo()
    # # 单据签署链接
    voucher_task_actor_get_url_demo()
