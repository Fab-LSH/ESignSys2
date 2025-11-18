from fasc_api.client.client import ApiClient
from fasc_api.client.service_client import ServiceClient
from fasc_api.exception.exceptions import ClientException
from fasc_api.exception.exceptions import ServerException
from fasc_api.client.doc_client import DocClient
from fasc_api.client.sign_task_client import SignTaskClient
from fasc_api.client.seal_client import SealClient

import os
import time

appId="80003971"
appSecret="7CCIHZRDAUNK2NYOPN6ALON7TOXQGITC"
REQUEST_URL="https://uat-api.fadada.com/api/v5"
ACCESS_TOKEN="811c8d2a0de44ac6aaec52e9d925c895"
FILE_TYPE="doc"
ID_TYPE="corp"
CORP_ID="631a2908bae74089965a8c96e3c99024"

BUSINESS_ID="92b6893f2ac6008c7697db7b61478438"

SEAL_IDS = ["1763437088500169298"]


# 指定请求 log 日志默认关闭
# api_client = ApiClient(appId, appSecret, request_url=REQUEST_URL, log=True)

# 设置超时时间 默认不设置 单位秒
api_client = ApiClient(appId, appSecret, request_url=REQUEST_URL, log=True, timeout=2)

### 获取access_token ###
def get_access_token_demo():
    try:
        result = ServiceClient.get_access_token(api_client)
        global ACCESS_TOKEN
        ACCESS_TOKEN = result['data']['accessToken']
        print(f"获取access_token成功, token = {result['data']['accessToken']}")
    except ClientException as  e:
        # 客户端初始化异常
        print("获取access_token失败!")
        print(e)
    except ServerException as e:
        # 服务端业务异常
        print(e)

    

def upload_local_file():
    print("### 获取上传文件url ###")
    ### 获取上传文件url ###
    try:
        data = {
            "fileType": FILE_TYPE,
            "accessToken": ACCESS_TOKEN
        }
        print(ACCESS_TOKEN)
        res = DocClient.file_get_upload_url(api_client, data)
        global upload_url, fddFile_url
        upload_url, fddFile_url = res['data']['uploadUrl'], res['data']['fddFileUrl']
        print(f"获取upload_url成功, upload_url = {upload_url}, fddFile_url = {fddFile_url}")
    except ClientException as e:
        print("获取uload_url失败!")
        print(e.__str__())
    except ServerException as e:
        print("获取uload_url失败!")
        print(e.__str__())
    
    time.sleep(2)
    
    ### 上传本地文件 ###
    print("### 上传本地文件 ###")
    try:
        import requests
        # 读取文件内容
        with open(FILE_PATH, 'rb') as f:
            file_content = f.read()
        # 使用 PUT 请求上传文件
        headers = {
            'Content-Type': 'application/octet-stream'
        }
        response = requests.put(
            upload_url,  # 使用获取到的上传地址
            data=file_content,
            headers=headers
        )
        if response.status_code == 200:
            print("文件上传成功")
        else:
            print(f"文件上传失败，状态码: {response.status_code}")
            print(f"错误信息: {response.text}")
    except FileNotFoundError:
        print("文件不存在，请检查文件路径")
    except Exception as e:
        print(f"上传文件时发生错误: {str(e)}")
    
    
### 文件处理 ###
def file_process_demo():
    print("### 文件处理 ###")
    try:
        file_name = os.path.basename(FILE_PATH)
        data = {
            "fddFileUrlList": [
                {
                    "fileType": "doc",
                    "fddFileUrl": fddFile_url,
                    "fileName": file_name
                }
            ]
        }
        res = DocClient.file_process(api_client, data)
        global fileId
        fileId = res['data']['fileIdList'][0]['fileId']
        print(f"获取fileId成功, fileId = {fileId}")
    except ClientException as e:
        print("文件处理失败")
        print(e.__str__())
    except ServerException as e:
        print("文件处理失败")
        print(e.__str__())
        
### 创建签署任务 ###
def create_demo():
    print("### 创建签署任务 ###")
    try:
        file_name = os.path.splitext(os.path.basename(FILE_PATH))[0]
        data = {
            "initiator": {
                "idType": "corp",
                "openId": CORP_ID
            },
            "signTaskSubject": file_name + "签署任务",
            "autoStart": True,
            "autoFinish": True,
            "autoFillFinalize": True,
            "signInOrder": False,
            "certCAOrg": "CFCA",
            "dueDate": "",
            "businessId": BUSINESS_ID,
            "docs": [
                {
                    "docId": "doc1",
                    "docName": file_name,
                    "docFileId": fileId,
                    "docFields": [
                        {
                            "fieldId": "field1",
                            "fieldName": "印章",
                            "moveable": True,
                            "position": {
                                "positionY": 108.32,
                                "positionMode": "pixel",
                                "positionPageNo": 1,
                                "positionX": 228.32
                            },
                            "fieldType": "corp_seal"
                        }
                    ]
                }
            ],
            "actors": [
                {
                    "actor": {
                        "actorId": "1",
                        "actorType": "corp",
                        "actorName": "甲方",
                        "actorOpenCorpId": "openCorpId",
                        "permissions": [
                            "sign",
                        ],
                    },
                    "signFields": [
                        {
                            "fieldDocId": "doc1",
                            "fieldId": "field1",
                        }
                    ],
                    "signConfigInfo": {
                        "requestVerifyFree": True
                    }
                }
            ],
        }
        res = SignTaskClient.create(api_client, data)
        global sign_Task_Id
        sign_Task_Id = res['data']['signTaskId']
        print(f"创建签署任务成功，签署任务id为: {sign_Task_Id}")
    except ClientException as e:
        print("创建签署任务失败")
        print(e.__str__())
    except ServerException as e:
        print("创建签署任务失败")
        print(e.__str__())
        
# 提交签署任务
def start_demo():
    try:
        data = {
            "signTaskId": sign_Task_Id,
            "accessToken": ACCESS_TOKEN
        }
        res = SignTaskClient.start(api_client, data)
        print("提交签署任务成功")
    except ClientException as e:
        print("提交签署任务失败")
        print(e.__str__())
    except ServerException as e:
        print("提交签署任务失败")
        print(e.__str__())
        
        
# 获取指定归属方的签署任务文档下载地址
def get_owner_download_url_demo():
    try:
        data = {
            "ownerId": {
                "idType": ID_TYPE,
                "openId": CORP_ID
            },
            "signTaskId": sign_Task_Id,
        }
        res = SignTaskClient.get_owner_download_url(api_client, data)
        download_url = res['data']['downloadUrl']
        print(f"下载链接为: {download_url}")
    except ClientException as e:
        print("获取下载链接失败")
        print(e.__str__())
    except ServerException as e:
        print("获取下载链接失败")
        print(e.__str__())
        
        
# 创建印章
def seal_create_by_template_demo():
    try:
        data = {
            "accessToken": ACCESS_TOKEN,
            "openCorpId": CORP_ID,
            "sealName": "接口测试印章"
        }
        res = SealClient.seal_create_by_template(api_client, data)
        seal_id = res['data']['sealId']
        print(f"创建seal成功, seal_id = {seal_id}")
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())

# 获取设置企业印章免验证签链接
def get_seal_free_sign_url_demo():
    try:
        data = {
            "openCorpId": CORP_ID,
            "clientUserId": CORP_ID,
            "sealIds": SEAL_IDS,
            "businessId": BUSINESS_ID
            
        }
        res = SealClient.get_seal_free_sign_url(api_client, data)
        freeSign_url = res['data']['freeSignUrl']
        print(f"印章免签链接获取成功, 链接为: {freeSign_url}")
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())

def main():
    import argparse
    parser = argparse.ArgumentParser(description="流程测试")
    parser.add_argument("--file_path", help="要上传的本地文件路径")
    args = parser.parse_args()

    global FILE_PATH
    FILE_PATH = args.file_path

    if not os.path.exists(FILE_PATH):
        print(f"文件不存在: {FILE_PATH}")
        return


    if ACCESS_TOKEN != "":
        upload_local_file()
        file_process_demo()
        if fileId != "":
            create_demo()
            time.sleep(2)
            # start_demo()
            time.sleep(2)
            get_owner_download_url_demo()
            



# python example.py --file_path ./测试合同.pdf

if __name__ == "__main__":
    get_access_token_demo()
    api_client.set_access_token(ACCESS_TOKEN)
    # main()
    # seal_create_by_template_demo()
    get_seal_free_sign_url_demo()