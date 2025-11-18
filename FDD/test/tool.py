from fasc_api.client.service_client import ServiceClient
from fasc_api.client.tool_client import ToolClient
from fasc_api.exception.exceptions import ClientException
from fasc_api.exception.exceptions import ServerException

from init_demo_data import InitDemoData

api_client = InitDemoData.api_client
access_token = ServiceClient.get_access_token_value(api_client)
api_client.set_access_token(access_token)


#  获取三要素校验
def get_three_element_verify_url_demo():
    try:
        data = {
            "clientUserId": "clientUserId00032131231",
            # "clientUserId": "clientUserIdabcabc0005",
            "userName": "周福成",
            "userIdentNo": "440981199904038619",
            "mobile": "13138799005",
            "redirectUrl": "http://www.baidu.com"
        }
        res = ToolClient.get_three_element_verify_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


#  获取四要素校验
def get_four_element_verify_url_demo():
    try:
        data = {
            "clientUserId": "clientUserId0003{{$timestamp}}",
            "userName": "周福成",
            "userIdentNo": "440981199904038619",
            "bankAccountNo": "6226080030571308",
            "mobile": "13138799005",
            "redirectUrl": "http://www.baidu.com"
        }
        res = ToolClient.get_four_element_verify_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


#  获取要素校验身份证图片下载链接
def get_user_idcard_image_download_url_demo():
    try:
        data = {
            "verifyId": "1231312"
        }
        res = ToolClient.get_user_idcard_image_download_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 个人认证授权管理-身份证OCR
def user_get_ocr_idcard_demo():
    try:
        data = {
            "faceSide": "",
            "nationalEmblemSide": ""
        }
        res = ToolClient.user_get_ocr_idcard(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 个人运营商三要素校验接口版
def telecom_there_element_verify_demo():
    try:
        data = {
            "initiator": {
                "idType": "person",
                "openId": "19800001115"
            },
            "faceSide": "",
            "nationalEmblemSide": ""
        }
        res = ToolClient.telecom_there_element_verify(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 个人银行卡四要素校验接口版
def bank_four_element_verify_demo():
    try:
        data = {
            "initiator": {
                "idType": "person",
                "openId": "19800001115"
            },
            "faceSide": "",
            "nationalEmblemSide": ""
        }
        res = ToolClient.bank_four_element_verify(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 个人二要素校验接口版
def bank_two_element_verify_demo():
    try:
        data = {
            "userName": "李明",
            "userIdentNo": "41133019991105010"
        }
        res = ToolClient.bank_two_element_verify(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 个人银行卡三要素校验
def user_identity_bank_three_element_verify_demo():
    try:
        data = {
            "userName": "李明",
            "userIdentNo": "41133019991105010",
            "bankAccountNo": "6226332186472271"
        }
        res = ToolClient.user_identity_bank_three_element_verify(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 人脸图片比对校验
def user_identity_idcard_three_element_verify_demo():
    try:
        data = {
            "userName": "李明",
            "userIdentNo": "41133019991105010",
            "imgBase64": "",
        }
        res = ToolClient.user_identity_idcard_three_element_verify(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取人脸核验链接
def user_verify_face_recognition_demo():
    try:
        data = {
            "userName": "李明",
            "userIdentNo": "41133019991105010",
            "faceAuthMode": "",
            "redirectUrl": ""
        }
        res = ToolClient.user_verify_face_recognition(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询人脸核验结果
def user_verify_face_status_query_demo():
    try:
        data = {
            "userName": "李明",
            "userIdentNo": "41133019991105010",
            "imgBase64": ""
        }
        res = ToolClient.user_verify_face_status_query(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 个人认证授权管理-营业执照OCR
def user_get_ocr_biz_license_demo():
    try:
        data = {
            "serialNo": "B3EBF23CB53143D6BB24C0B55B655280",
            "getFile": 0
        }
        res = ToolClient.user_get_ocr_biz_license(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 个人认证授权管理-驾驶证OCR
def user_get_ocr_driving_license_demo():
    try:
        data = {
            "serialNo": "B3EBF23CB53143D6BB24C0B55B655280",
            "getFile": 0
        }
        res = ToolClient.user_get_ocr_driving_license(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 个人认证授权管理-行驶证OCR
def user_get_ocr_vehicle_license_demo():
    try:
        data = {
            "serialNo": "B3EBF23CB53143D6BB24C0B55B655280",
            "getFile": 0
        }
        res = ToolClient.user_get_ocr_vehicle_license(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 个人认证授权管理-行驶证OCR
def user_get_ocr_mainland_permit_demo():
    try:
        data = {
            "serialNo": "B3EBF23CB53143D6BB24C0B55B655280",
            "getFile": 0
        }
        res = ToolClient.user_get_ocr_mainland_permit(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 企业组织三要素校验
def corp_identity_business_three_element_verify_demo():
    try:
        data = {
            "corpName": "测试企业",
            "corpIdentNo": "41133019991105010",
            "legalRepName": "李明"
        }
        res = ToolClient.corp_identity_business_three_element_verify(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 企业组织四要素校验
def corp_identity_business_four_element_verify_demo():
    try:
        data = {
            "corpName": "测试企业",
            "corpIdentNo": "41133019991105010",
            "legalRepName": "李明",
            "legalRepIdCertNo": "41133019991105010"
        }
        res = ToolClient.corp_identity_business_four_element_verify(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 企业工商信息查询
def corp_identity_business_info_query_demo():
    try:
        data = {
            "corpName": "测试企业",
            "corpIdentNo": "41133019991105010"
        }
        res = ToolClient.corp_identity_business_info_query(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())

# 银行卡四要素核验
def user_verify_bankcard_four_element_create_demo():
    try:
        data = {
            "userName": "周成",
            "userIdentNo": "440981198904038519",
            "bankAccountNo": "6226080130571208",
            "mobile": "13138718005"
        }
        res = ToolClient.user_verify_bankcard_four_element_create(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 手机号三要素核验
def user_verify_telecom_three_element_create_demo():
    try:
        data = {
            "userName": "周成",
            "userIdentNo": "440981198904038519",
            "mobile": "13138718005"
        }
        res = ToolClient.user_verify_telecom_three_element_create(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 验证码校验
def user_verify_auth_code_check_demo():
    try:
        data = {
            "transactionId": "B3EBF23CB53143D6BB24C0B55B655280",
            "authCode": "578568"
        }
        res = ToolClient.user_verify_auth_code_check(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取验证码
def user_verify_auth_code_get_demo():
    try:
        data = {
            "transactionId": "B3EBF23CB53143D6BB24C0B55B655280"
        }
        res = ToolClient.user_verify_auth_code_get(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取身份核验详情
def user_verify_get_detail_demo():
    try:
        data = {
            "transactionId": "B3EBF23CB53143D6BB24C0B55B655280"
        }
        res = ToolClient.user_verify_get_detail(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())



if __name__ == '__main__':
    # # 获取三要素校验
    # get_three_element_verify_url_demo()
    # # 获取四要素校验
    # get_four_element_verify_url_demo()
    # # 获取要素校验身份证图片下载链接
    # get_user_idcard_image_download_url_demo()
    # # 个人认证授权管理-身份证OCR
    # user_get_ocr_idcard_demo()
    # # 个人运营商三要素校验接口版
    # telecom_there_element_verify_demo()
    # # 个人银行卡四要素校验接口版
    # bank_four_element_verify_demo()
    # # 个人银行卡二要素校验接口版
    # bank_two_element_verify_demo()
    # # 个人银行卡三要素校验
    # user_identity_bank_three_element_verify_demo()
    # # 人脸图片比对校验
    # user_identity_idcard_three_element_verify_demo()
    # # 获取人脸核验链接
    # user_verify_face_recognition_demo()
    # # 查询人脸核验结果
    # user_verify_face_status_query_demo()
    # # 个人认证授权管理-营业执照OCR
    # user_get_ocr_biz_license_demo()
    # # 个人认证授权管理-驾驶证OCR
    # user_get_ocr_driving_license_demo()
    # # 个人认证授权管理-行驶证OCR
    # user_get_ocr_vehicle_license_demo()
    # # 个人认证授权管理-行驶证OCR
    # user_get_ocr_mainland_permit_demo()
    # # 企业组织三要素校验
    # corp_identity_business_three_element_verify_demo()
    # # 企业工商信息查询
    # corp_identity_business_four_element_verify_demo()
    # # 企业工商信息查询
    # corp_identity_business_info_query_demo()
    # 银行卡四要素核验
    user_verify_bankcard_four_element_create_demo()
    # 手机号三要素核验
    user_verify_telecom_three_element_create_demo()
    # 验证码校验
    user_verify_auth_code_check_demo()
    # 获取验证码
    user_verify_auth_code_get_demo()
    # 获取身份核验详情
    user_verify_get_detail_demo()