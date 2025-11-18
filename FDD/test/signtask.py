from fasc_api.client.service_client import ServiceClient
from fasc_api.client.sign_task_client import SignTaskClient
from fasc_api.exception.exceptions import ClientException
from fasc_api.exception.exceptions import ServerException

from init_demo_data import InitDemoData

api_client = InitDemoData.api_client
access_token = ServiceClient.get_access_token_value(api_client)
api_client.set_access_token(access_token)


# 创建签署任务
def create_demo():
    try:
        data = {
            "initiator": {
                "idType": "corp",
                "openId": "c5aa3ea8db994fb3b8138a5ba86a63f4"
            },
            "signTaskSubject": "原始文件2132131",
            "autoStart": True,
            "autoFinish": True,
            "autoFillFinalize": True,
            "signInOrder": False,
            "certCAOrg": "CFCA",
            "dueDate": "",
            "docs": [
                {
                    "docId": "docId1",
                    "docName": "1签署页上显示的名称1",
                    "docFileId": "1679018208957151705",
                    "docFields": [
                        {
                            "fieldId": "个人签名",
                            "fieldName": "个人签名",
                            "moveable": True,
                            "position": {
                                "positionY": 9128.32,
                                "positionMode": "pixel",
                                "positionPageNo": 1,
                                "positionX": 9128.32
                            },
                            "fieldType": "person_sign"
                        },
                        {
                            "fieldId": "身份证号控件",
                            "fieldName": "身份证号控件",
                            "position": {
                                "positionY": 728.32,
                                "positionMode": "pixel",
                                "positionPageNo": 1,
                                "positionX": 728.32
                            },
                            "fieldType": "id_card"
                        },
                        {
                            "fieldId": "企业印章",
                            "fieldName": "企业印章",
                            "moveable": True,
                            "position": {
                                "positionY": 228.32,
                                "positionMode": "pixel",
                                "positionPageNo": 1,
                                "positionX": 228.32
                            },
                            "fieldType": "corp_seal"
                        },
                        {
                            "fieldId": "表格",
                            "fieldName": "表格",
                            "position": {
                                "positionY": 128.32,
                                "positionMode": "pixel",
                                "positionPageNo": 1,
                                "positionX": 628.32
                            },
                            "fieldType": "table"
                        },
                        {
                            "fieldId": "骑缝章",
                            "fieldName": "骑缝章",
                            "position": {
                                "positionY": 328.32,
                                "positionMode": "pixel",
                                "positionPageNo": 1,
                                "positionX": 328.32
                            },
                            "fieldType": "corp_seal_cross_page"
                        },
                        {
                            "fieldId": "日期戳",
                            "fieldName": "日期戳",
                            "moveable": True,
                            "position": {
                                "positionY": 428.32,
                                "positionMode": "pixel",
                                "positionPageNo": 1,
                                "positionX": 428.32
                            },
                            "fieldType": "date_sign"
                        },
                        {
                            "fieldId": "备注区",
                            "fieldName": "备注区",
                            "position": {
                                "positionY": 528.32,
                                "positionMode": "pixel",
                                "positionPageNo": 1,
                                "positionX": 228.32
                            },
                            "fieldType": "remark_sign"
                        },
                        {
                            "fieldId": "单行文本",
                            "fieldName": "单行文本",
                            "moveable": True,
                            "position": {
                                "positionY": 528.32,
                                "positionMode": "pixel",
                                "positionPageNo": 1,
                                "positionX": 628.32
                            },
                            "fieldType": "text_single_line"
                        },
                        {
                            "fieldId": "数字控件",
                            "fieldName": "数字控件",
                            "position": {
                                "positionY": 928.32,
                                "positionMode": "pixel",
                                "positionPageNo": 1,
                                "positionX": 928.32
                            },
                            "fieldType": "number",
                            "fieldNumber": {
                                "defaultValue": "333666"
                            }
                        },
                        {
                            "fieldId": "多行文本",
                            "fieldName": "多行文本",
                            "position": {
                                "positionY": 828.32,
                                "positionMode": "pixel",
                                "positionPageNo": 1,
                                "positionX": 628.32
                            },
                            "fieldType": "text_multi_line"
                        },
                        {
                            "fieldId": "填写日期控件",
                            "fieldName": "填写日期控件",
                            "position": {
                                "positionY": 828.32,
                                "positionMode": "pixel",
                                "positionPageNo": 1,
                                "positionX": 228.32
                            },
                            "fieldType": "fill_date"
                        },
                        {
                            "fieldId": "图片",
                            "fieldName": "图片",
                            "position": {
                                "positionY": 728.32,
                                "positionMode": "pixel",
                                "positionPageNo": 1,
                                "positionX": 228.32
                            },
                            "fieldType": "picture"
                        },
                        {
                            "fieldId": "下拉",
                            "fieldName": "下拉",
                            "position": {
                                "positionY": 628.32,
                                "positionMode": "pixel",
                                "positionPageNo": 1,
                                "positionX": 228.32
                            },
                            "fieldType": "select_box",
                            "FieldSelectBox": {
                                "option": [
                                    "选项一",
                                    "选项二"
                                ]
                            }
                        }
                    ]
                }
            ],
            "actors": [
                {
                    "actor": {
                        "actorId": "个人方",
                        "actorType": "person",
                        "actorName": "个人方",
                        "permissions": [
                            "sign",
                            "fill"
                        ],
                        "actorOpenId": "",
                        "identNameForMatch": "",
                        "certNoForMatch": "",
                        "notification": {
                            "notifyWay": "mobile",
                            "sendNotification": False,
                            "notifyAddress": "17871907081"
                        }
                    },
                    "fillFields": [
                        {
                            "fieldDocId": "docId1",
                            "fieldId": "单行文本",
                            "moveable": True
                        },
                        {
                            "fieldDocId": "docId1",
                            "fieldName": "身份证号控件"
                        },
                        {
                            "fieldDocId": "docId1",
                            "fieldId": "填写日期控件"
                        },
                        {
                            "fieldDocId": "docId1",
                            "fieldId": "图片"
                        },
                        {
                            "fieldDocId": "docId1",
                            "fieldId": "下拉"
                        }
                    ],
                    "signFields": [
                        {
                            "fieldDocId": "docId1",
                            "moveable": False,
                            "fieldName": "个人签名"
                        },
                        {
                            "fieldDocId": "docId1",
                            "fieldId": "日期戳"
                        }
                    ],
                    "signConfigInfo": {
                        "orderNo": "2",
                        "blockHere": False,
                        "requestVerifyFree": False,
                        "signerSignMethod": "unlimited",
                        "viewCompletedTask": False
                    }
                },
                {
                    "actor": {
                        "actorId": "企业方",
                        "actorType": "corp",
                        "actorName": "企业方",
                        "permissions": [
                            "sign",
                            "fill"
                        ],
                        "actorOpenId": "",
                        "identNameForMatch": "",
                        "certNoForMatch": "",
                        "notification": {
                            "notifyWay": "email",
                            "sendNotification": False,
                            "notifyAddress": "xiej@fadada.com"
                        }
                    },
                    "fillFields": [
                        {
                            "fieldDocId": "docId1",
                            "fieldId": "多行文本"
                        },
                        {
                            "fieldDocId": "docId1",
                            "fieldId": "表格"
                        }
                    ],
                    "signFields": [
                        {
                            "fieldDocId": "docId1",
                            "fieldId": "企业印章"
                        },
                        {
                            "fieldDocId": "docId1",
                            "fieldId": "备注区"
                        },
                        {
                            "fieldDocId": "docId1",
                            "fieldId": "骑缝章"
                        }
                    ],
                    "signConfigInfo": {
                        "orderNo": "1",
                        "blockHere": False,
                        "requestVerifyFree": False,
                        "signerSignMethod": "unlimited",
                        "viewCompletedTask": False
                    }
                },
                {
                    "actor": {
                        "actorId": "抄送个人",
                        "actorType": "person",
                        "actorName": "抄送个人",
                        "permissions": [
                            "cc"
                        ],
                        "notification": {
                            "sendNotification": True,
                            "notifyWay": "mobile",
                            "notifyAddress": "17771907081"
                        }
                    }
                }
            ],
            "watermarks": [
                {
                    "type": "",
                    "content": "",
                    "fontSize": 0,
                    "fontColor": "",
                    "rotation": 0,
                    "transparency": 0,
                    "position": "",
                    "density": ""
                }
            ]
        }
        res = SignTaskClient.create(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 创建签署任务（基于签署模板）
def create_with_template_demo():
    try:
        data = {
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b",
            "initiator": {
                "idType": "person",
                "openId": "aeeb1f1bf6f349e89915a9701793d1bd"
            },
            "signTaskSubject": "签署任务模板发起V5.1签署任务-个人1677138236",
            "signTemplateId": "1655865624105123407",
            "expiresTime": "1686752087000",
            "coverMessage": "公开的封面消息",
            "autoStart": True,
            "autoFillFinalize": True,
            "autoFinish": True,
            "businessScene": {
                "businessId": "9c0ee07dde1ef7459bbad26f26d4569c",
                "transReferenceId": "1677138236"
            },
            "dueDate": "",
            "actors": [
                {
                    "actor": {
                        "actorId": "个人方",
                        "actorType": "person",
                        "actorName": "个人方昵称",
                        "permissions": [
                            "fill",
                            "sign"
                        ],
                        "actorFDDId": "C1543477",
                        "identNameForMatch": "",
                        "certNoForMatch": "",
                        "notification": {
                            "notifyWay": "mobile",
                            "sendNotification": False,
                            "notifyAddress": "17000217007"
                        }
                    },
                    "fillFields": {
                        "fieldDocId": "19161471",
                        "fieldId": "单行文本",
                        "fieldName": "单行文本",
                        "fieldValue": "单行文本默认值"
                    },
                    "signConfigInfo": {
                        "blockHere": False,
                        "requestVerifyFree": False,
                        "viewCompletedTask": ""
                    }
                }
            ],
            "watermarks": [
                {
                    "type": "",
                    "content": "",
                    "fontSize": 0,
                    "fontColor": "",
                    "rotation": 0,
                    "transparency": 0,
                    "position": "",
                    "density": ""
                }
            ]
        }
        res = SignTaskClient.create_with_template(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 添加签署任务文档
def add_doc_demo():
    try:
        data = {
            "signTaskId": "1656656963244180430",
            "docs": [
                {
                    "docId": "docId1",
                    "docName": "签署页上显示的名称1",
                    "docFileId": "1679018208957151705",
                    "docTemplateId": "1655953099101128413",
                    "docFields": [
                        {
                            "fieldId": "1605689",
                            "fieldName": "测试文件",
                            "fieldKey": "测试标识1",
                            "moveable": False,
                            "position": {
                                "positionMode": "keyword",
                                "positionPageNo": 122,
                                "positionX": "2231",
                                "positionY": "20",
                                "positionKeyword": "测试",
                                "keywordOffsetX": "测试",
                                "keywordOffsetY": "测试"
                            },
                            "fieldType": "person_sign",
                            "fieldTextSingleLine": {
                                "required": False,
                                "defaultValue": "测试"
                            },
                            "fieldTextMultiLine": {
                                "required": False,
                                "defaultValue": "测试"
                            },
                            "fieldCheckBox": {
                                "required": False,
                                "defaultValue": False
                            }
                        }
                    ]
                }
            ],
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = SignTaskClient.add_doc(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 移除签署任务文档
def delete_doc_demo():
    try:
        data = {
            "signTaskId": "1656656963244180430",
            "docs": [
                {
                    "docId": "docId1",
                    "docName": "签署页上显示的名称1",
                    "docTemplateId": "1655953099101128413"
                }
            ],
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = SignTaskClient.delete_doc(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 添加签署任务控件
def add_field_demo():
    try:
        data = {
            "signTaskId": "1656928831553122296",
            "actorId": "3252",
            "fields": [
                {
                    "docId": "docId1",
                    "docFields": [
                        {
                            "fieldId": "个人签名",
                            "fieldName": "个人签名",
                            "position": {
                                "positionY": 128.32,
                                "positionMode": "pixel",
                                "positionPageNo": 1,
                                "positionX": 128.32
                            },
                            "fieldType": "person_sign"
                        }
                    ]
                }
            ]
        }
        res = SignTaskClient.add_field(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 移除签署任务控件
def delete_field_demo():
    try:
        data = {
            "signTaskId": "1656657193146145802",
            "fields": [
                {
                    "docId": "docId1",
                    "fieldIds": [
                        "个人签名"
                    ]
                }
            ],
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = SignTaskClient.delete_field(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 添加签署任务附件
def add_attach_demo():
    try:
        data = {
            "signTaskId": "1656928831553122296",
            "attachs": [
                {
                    "attachId": "attachId1",
                    "attachName": "附件名1",
                    "attachFileId": "1656917134268168485"
                }
            ],
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = SignTaskClient.add_attach(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 移除签署任务附件
def delete_attach_demo():
    try:
        data = {
            "signTaskId": "1656928831553122296",
            "attachIds": [
                "2131"
            ],
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = SignTaskClient.delete_attach(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 添加签署任务参与方
def add_actor_demo():
    try:
        data = {
            "signTaskId": "1656933214308159617",
            "actors": [
                {
                    "actor": {
                        "actorId": "个人方签署",
                        "actorType": "person",
                        "actorName": "个人方昵称",
                        "permissions": [
                            "sign"
                        ],
                        "actorOpenId": "aeeb1f1bf6f349e89915a9701793d1bd",
                        "identNameForMatch": "",
                        "certNoForMatch": "",
                        "notification": {
                            "notifyWay": "mobile",
                            "sendNotification": False,
                            "notifyAddress": "广东"
                        }
                    },
                    "signConfigInfo": {
                        "orderNo": "1",
                        "blockHere": False,
                        "requestVerifyFree": False,
                        "signerSignMethod": "unlimited",
                        "viewCompletedTask": False
                    }
                }
            ]
        }
        res = SignTaskClient.add_actor(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 移除签署任务参与方
def delete_actor_demo():
    try:
        data = {
            "signTaskId": "1656933214308159617",
            "actorIds": [
                "34232"
            ],
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = SignTaskClient.delete_actor(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 发起签署任务
def start_demo():
    try:
        data = {
            "signTaskId": "1656657193146145802",
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = SignTaskClient.start(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 填写签署任务控件内容
def fill_field_values_demo():
    try:
        data = {
            "signTaskId": "1689233750998121742",
            "docFieldValues": [
                {
                    "docId": "docId1",
                    # "fieldId": "单行文本",
                    "fieldValue": "单行文本默认值ceshi",
                    # "fieldKey": "单行文本key",
                    "fieldName": "单行文本1"
                }
            ],
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = SignTaskClient.fill_field_values(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 定稿签署任务
def finalize_doc_demo():
    try:
        data = {
            "signTaskId": "1656928831553122296",
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = SignTaskClient.finalize_doc(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 阻塞签署任务
def block_demo():
    try:
        data = {
            "signTaskId": "1656928831553122296",
            "actorId": "16553122296",
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = SignTaskClient.block(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 解阻签署任务
def unblock_demo():
    try:
        data = {
            "signTaskId": "1656928831553122296",
            "actorId": "16553122296",
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = SignTaskClient.unblock(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 撤销签署任务
def cancel_demo():
    try:
        data = {
            "signTaskId": "1656928831553122296",
            "terminationNote": "测试",
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = SignTaskClient.cancel(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取签署任务详情
def get_detail_demo():
    try:
        data = {
            "signTaskId": "1656928831553122296",
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = SignTaskClient.get_detail(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取指定归属方的签署任务列表
def get_owner_list_demo():
    try:
        data = {
            "ownerId": {
                "idType": "person",
                "openId": "aeeb1f1bf6f349e89915a9701793d1bd"
            },
            "ownerRole": "initiator",
            "listFilter": {
                "signTaskSubject": "签署任务",
                "signTaskStatus": "task_created",
                "transReferenceId": "1234"
            },
            "listPageNo": 1,
            "listPageSize": 100,
            "memberId": "ed6aaa63d"
        }
        res = SignTaskClient.get_owner_list(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取指定归属方的签署任务文档下载地址
def get_owner_download_url_demo():
    try:
        data = {
            "ownerId": {
                "idType": "person",
                "openId": "aeeb1f1bf6f349e89915a9701793d1bd"
            },
            "signTaskId": "1656657193146145802",
            "fileType": "doc",
            "id": "docId1"
        }
        res = SignTaskClient.get_owner_download_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取参与方专属链接
def sign_task_actor_get_url_demo():
    try:
        data = {
            "signTaskId": "1656928831553122296",
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = SignTaskClient.sign_task_actor_get_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询企业签署任务文件夹
def sign_task_cataloglist_demo():
    try:
        data = {
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b",
            "ownerId": {
                "idType": "corp",
                "openId": "1623621278903943168"
            }
        }
        res = SignTaskClient.sign_task_cataloglist(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询签署任务控件信息
def list_sign_task_field_demo():
    try:
        data = {
            "signTaskId": "1656656963244180430",
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = SignTaskClient.list_sign_task_field(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询签署任务参与方信息
def list_sign_task_actor_demo():
    try:
        data = {
            "signTaskId": "1656928831553122296",
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = SignTaskClient.list_sign_task_actor(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询签署任务审批信息
def get_approval_info_demo():
    try:
        data = {
            "signTaskId": "1656928831553122296",
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = SignTaskClient.get_approval_info(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取批量签署链接
def get_batch_sign_url_demo():
    try:
        data = {
            "idType": "person",
            "accountName": "17871907081",
            "signTaskIds": [
                "1690440267306170000",
                "1690440293449140876"
            ],
        }
        res = SignTaskClient.get_batch_sign_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取签署任务编辑链接
def get_sign_task_edit_url_demo():
    try:
        data = {
            "signTaskId": "1656657193146145802",
            "redirectUrl": "http://www.baidu.com",
            "nonEditableInfo": []
        }
        res = SignTaskClient.get_sign_task_edit_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取签署任务预览链接
def get_sign_task_preview_url_demo():
    try:
        data = {
            "signTaskId": "1656657193146145802",
            "redirectUrl": "http://www.baidu.com",
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = SignTaskClient.get_sign_task_preview_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 催办签署任务
def sign_task_urge_demo():
    try:
        data = {
            "signTaskId": "1656928831553122296",
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = SignTaskClient.sign_task_urge(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 下载签署任务公证处保全报告
def get_download_evidence_report_demo():
    try:
        data = {
            "signTaskId": "1656928831553122296",
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = SignTaskClient.get_download_evidence_report(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 删除签署任务
def delete_sign_task_demo():
    try:
        data = {
            "signTaskId": "1656928831553122296"
        }
        res = SignTaskClient.delete_sign_task(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 结束签署任务
def finish_sign_task_demo():
    try:
        data = {
            "signTaskId": "1656928831553122296"
        }
        res = SignTaskClient.finish_sign_task(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询签署业务类型列表
def get_sign_task_business_type_list_demo():
    try:
        data = {
            "openCorpId": "1553122296"
        }
        res = SignTaskClient.get_sign_task_business_type_list(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询参与方的签署刷脸底图
def get_sign_task_face_picture_demo():
    try:
        data = {
            "signTaskId": "1679915600856163014",
            "actorId": "企业方"
        }
        res = SignTaskClient.get_sign_task_face_picture(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 作废签署任务
def sign_task_abolish_demo():
    try:
        data = {
            "signTaskId": "1673402692685180687",
            "abolishedInitiator": {
                "initiatorId": "972f3189db2d48539b984ad3ec491515"
            },
            "reason": "不合规API",
            "autoStart": False
        }
        res = SignTaskClient.sign_task_abolish(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 签署文档切图
def get_sign_task_owner_slicing_ticket_id_demo():
    try:
        data = {
            "ownerId": {
                "idType": "corp",
                "openId": "972f3189db2d48539b984ad3ec491515"
            },
            "signTaskId": "1673402692685180687"
        }
        res = SignTaskClient.get_sign_task_owner_slicing_ticket_id(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取图片版签署文档下载地址
def get_sign_task_owner_pic_download_url_demo():
    try:
        data = {
            "slicingTicketId": "1681798354547169957"
        }
        res = SignTaskClient.get_sign_task_owner_pic_download_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取参与方签署音视频下载地址
def get_audio_video_download_url_demo():
    try:
        data = {
            "signTaskId": "",
            "actorId": ""
        }

        res = SignTaskClient.get_audio_video_download_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取V3签署任务链接
def sign_task_actor_v3_get_url_demo():
    try:
        data = {
            "ownerId": {
                "idType": "person",
                "openId": "cf6c41520b6544f590b6e6909ca7d488"
            },
            "signTaskId": "039ae5431f284ea08cf1bbbddadd2bb9",
            "redirectUrl": "www.baidu.com"
        }
        res = SignTaskClient.sign_task_actor_v3_get_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取历史文件对比数据
def get_compare_result_url_demo():
    try:
        data = {
            "ownerId": {
                "idType": "person",
                "openId": "cf6c41520b6544f590b6e6909ca7d488"
            },
            "signTaskId": "039ae5431f284ea08cf1bbbddadd2bb9",
            "redirectUrl": "www.baidu.com"
        }
        res = SignTaskClient.get_compare_result_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 修改签署任务参与方
def sign_task_actor_modify_demo():
    try:
        data = {
            "signTaskId": "1689152903387132064",
            "actors": [
                {
                    "actorId": "企业方",
                    # "fillFields": null,
                    # "signFields": null,
                    "signConfigInfo": {
                        "requestVerifyFree": False,
                        "signerSignMethod": "",
                        "readingToEnd": True,
                        "readingTime": 100,
                        "requestMemberSign": False,
                        "resizeSeal": True
                    }
                }
            ]
        }
        res = SignTaskClient.sign_task_actor_modify(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 签署任务延期
def sign_task_extension_demo():
    try:
        data = {
            "signTaskId": "1690439883815110917",
            "extensionTime": "16903580165000"
        }
        res = SignTaskClient.sign_task_extension(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 签署任务驳回填写
def sign_task_ignore_demo():
    try:
        data = {
            "signTaskId": "1656657193146145802",
            "actors": [
                {
                    "actorId": "参与方1"
                }
            ]
        }
        res = SignTaskClient.sign_task_ignore(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())

# 获取送达查看报告下载地址
def sign_task_message_report_get_download_url_demo():
    try:
        data = {
            "signTaskId": "1690371219112140747"
        }
        res = SignTaskClient.sign_task_message_report_get_download_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())

# 查询审批流程详情
def approval_flow_get_list_demo():
    try:
        data = {
            "signTaskId": "1690371219112140747"
        }
        res = SignTaskClient.approval_flow_get_list(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())

# 查询审批流程详情
def approval_flow_get_detail_demo():
    try:
        data = {
            "signTaskId": "1690371219112140747"
        }
        res = SignTaskClient.approval_flow_get_detail(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取预填充链接
def sign_task_get_prefill_url_demo():
    try:
        data = {
            "signTaskId": "1690371219112140747"
        }
        res = SignTaskClient.sign_task_get_prefill_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())




if __name__ == '__main__':
    # 创建签署任务
    # create_demo()
    # # 创建签署任务（基于签署模板）
    # create_with_template_demo()

    # 添加签署任务文档
    # add_doc_demo()
    # 移除签署任务文档
    # delete_doc_demo()
    # # 添加签署任务控件
    # add_field_demo()
    # # 移除签署任务控件
    # delete_field_demo()
    # # 添加签署任务附件
    # add_attach_demo()
    # # 移除签署任务附件
    # delete_attach_demo()
    # # 添加签署任务参与方
    # add_actor_demo()
    # # 移除签署任务参与方
    # delete_actor_demo()
    #
    # # 查询企业签署任务文件夹
    # sign_task_cataloglist_demo()
    # # 查询签署任务控件信息
    # list_sign_task_field_demo()
    # # 查询签署任务参与方信息
    # list_sign_task_actor_demo()
    #
    # # 填写签署任务控件内容
    # fill_field_values_demo()
    # # 发起签署任务
    # start_demo()
    # # 定稿签署任务文档
    # finalize_doc_demo()
    #
    # # 撤销签署任务
    # cancel_demo()
    # # 阻塞签署任务
    # block_demo()
    # # 解阻签署任务
    # unblock_demo()
    # # 签署任务催办
    # sign_task_urge_demo()
    #
    # # 获取签署任务详情
    # get_detail_demo()
    # # 查询签署任务审批信息
    # get_approval_info_demo()
    # # 下载签署任务文档
    # get_owner_download_url_demo()
    # # 获取指定归属方的签署任务列表
    # get_owner_list_demo()
    #
    # # 获取批量签署链接
    # get_batch_sign_url_demo()
    #
    # # 获取参与方专属链接
    # sign_task_actor_get_url_demo()
    #
    # # 获取签署任务编辑链接
    # get_sign_task_edit_url_demo()
    #
    # # 获取签署任务预览链接
    # get_sign_task_preview_url_demo()
    # # 下载签署任务公证处保全报告
    # get_download_evidence_report_demo()
    # # 删除签署任务
    # delete_sign_task_demo()
    # # 结束签署任务
    # finish_sign_task_demo()
    # # 查询签署业务类型列表
    # get_sign_task_business_type_list_demo()
    # 查询参与方的签署刷脸底图
    # get_sign_task_face_picture_demo()

    # 作废签署任务
    # sign_task_abolish_demo()
    # 签署文档切图
    # get_sign_task_owner_slicing_ticket_id_demo()
    # 获取图片版签署文档下载地址
    # get_sign_task_owner_pic_download_url_demo()
    # 获取参与方签署音视频下载地址
    # get_audio_video_download_url_demo()
    # 获取V3签署任务链接
    # sign_task_actor_v3_get_url_demo()
    # 获取历史文件对比数据
    # get_compare_result_url_demo()
    # 修改签署任务参与方
    # sign_task_actor_modify_demo()
    # 签署任务延期
    # sign_task_extension_demo()
    # 签署任务驳回填写
    # sign_task_ignore_demo()
    # 获取送达查看报告下载地址
    # sign_task_message_report_get_download_url_demo()
    # 查询审批流程详情
    approval_flow_get_list_demo()
    # 查询审批流程详情
    approval_flow_get_detail_demo()
    # 获取预填充链接
    sign_task_get_prefill_url_demo()
