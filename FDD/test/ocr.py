from fasc_api.client.ocr_client import OcrClient
from fasc_api.client.service_client import ServiceClient
from fasc_api.exception.exceptions import ClientException
from fasc_api.exception.exceptions import ServerException

from init_demo_data import InitDemoData

api_client = InitDemoData.api_client
access_token = ServiceClient.get_access_token_value(api_client)
api_client.set_access_token(access_token)


# 获取文件对比页面链接
def get_ocr_edit_compare_url_demo():
    try:
        data = {
            "initiator": {
                "idType": "person",
                "openId": "19800001115"
            },
            "originFileId": "f7b9ff6851e81",
            "targetFileId": "0078ff6851e81"
        }
        res = OcrClient.get_ocr_edit_compare_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取历史文件对比页面链接
def get_ocr_edit_result_compare_url_demo():
    try:
        data = {
            "initiator": {
                "idType": "person",
                "openId": "19800001115"
            },
            "compareId": "f7b9ff6851e81"
        }
        res = OcrClient.get_ocr_edit_result_compare_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取合同智审页面链接
def get_ocr_edit_examine_url_demo():
    try:
        data = {
            "initiator": {
                "idType": "person",
                "openId": "19800001115"
            },
            "fileId": "f7b9ff6851e81",
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = OcrClient.get_ocr_edit_examine_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取历史合同智审页面链接
def get_ocr_edit_result_examine_url_demo():
    try:
        data = {
            "initiator": {
                "idType": "person",
                "openId": "19800001115"
            },
            "examineId": "f7b9ff6851e81",
            "accessToken": "ed6aaa63d7b147a393ef0a95cf7d476b"
        }
        res = OcrClient.get_ocr_edit_result_examine_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取历史合同智审数据
def get_ocr_edit_examine_result_data_demo():
    try:
        data = {
            "url": "https://uat-api.fadada.com/api/v5/ocr/edit/examine-result-data",
            "initiator": {
                "idType": "corp",
                "openId": "9fed3e48760e45ea8a80a47db9fbe407"
            },
            "examineId": "1664468879791009794"
        }
        res = OcrClient.get_ocr_edit_examine_result_data(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


if __name__ == '__main__':
    # 获取文件对比页面链接
    get_ocr_edit_compare_url_demo()
    # 获取历史文件对比页面链接
    get_ocr_edit_result_compare_url_demo()
    # 获取合同智审页面链接
    get_ocr_edit_examine_url_demo()
    # 获取历史合同智审页面链接
    get_ocr_edit_result_examine_url_demo()
    # 获取历史合同智审数据
    get_ocr_edit_examine_result_data_demo()
