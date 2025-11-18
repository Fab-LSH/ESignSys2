from fasc_api.client.doc_client import DocClient
from fasc_api.client.service_client import ServiceClient
from fasc_api.exception.exceptions import ClientException
from fasc_api.exception.exceptions import ServerException
from init_demo_data import InitDemoData

api_client = InitDemoData.api_client
access_token = ServiceClient.get_access_token_value(api_client)
api_client.set_access_token(access_token)


# 通过网络文件地址上传
def file_upload_by_url_demo():
    try:
        data = {
            "fileType": "doc",
            "fileUrl": "http://www.xxx.com"
        }
        res = DocClient.file_upload_by_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取文件上传地址
def file_get_upload_url_demo():
    try:
        data = {
            "fileType": "String",
            "accessToken": "String"
        }
        res = DocClient.file_get_upload_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 文件处理
def file_process_demo():
    try:
        data = {
            "fddFileUrlList": [
                {
                    "fileType": "doc",
                    "fddFileUrl": "",
                    "fileName": "资料"
                }
            ]
        }
        res = DocClient.file_process(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 文档验签
def file_verify_sign_demo():
    try:
        data = {
            "fileId":"19800001115",
            "fileHash":"072ab2072ab28e646d4157072ab28e646d4157adfe4b00009517d3adfe4b00009517d38e646d4157adf072ab28e646d4157adfe4b00009517d3e4b00009517d3"
        }
        res = DocClient.file_verify_sign(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 关键字坐标查询
def file_get_keyword_positions_demo():
    try:
        data = {
            "fileId":"19800001115",
            "fileHash":"072ab2072ab28e646d4157072ab28e646d4157adfe4b00009517d3adfe4b00009517d38e646d4157adf072ab28e646d4157adfe4b00009517d3e4b00009517d3"
        }
        res = DocClient.file_get_keyword_positions(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


if __name__ == '__main__':
    # 通过网络文件地址上传
    file_upload_by_url_demo()
    file_get_upload_url_demo()
    file_process_demo()
    # 文档验签
    file_verify_sign_demo()
