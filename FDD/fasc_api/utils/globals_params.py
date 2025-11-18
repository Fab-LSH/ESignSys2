'''
公共全局参数
'''


class Params:
    APP_ID = 'X-FASC-App-Id'
    SIGN_TYPE = 'X-FASC-Sign-Type'
    SIGN = 'X-FASC-Sign'
    TIMESTAMP = 'X-FASC-Timestamp'
    NONCE = 'X-FASC-Nonce'
    ACCESS_TOKEN = 'X-FASC-AccessToken'
    DATA_KEY = 'bizContent'
    GRANT_TYPE = 'X-FASC-Grant-Type'
    REQEUST_ID = 'X-FASC-Request-Id'
    SUB_VERSION = 'X-FASC-Api-SubVersion'

    # 签名方式
    SIGN_TYPE_SHA = 'HMAC-SHA256'
    GRANT_TYPE_CLIENT = 'client_credential'
    # 编码类型
    ENCODE_TYPE = 'utf-8'

    # 字典拼接填充
    DICT_TO_STR = '%s=%s&'

    # 接口请求成功code
    REQUEST_SUCCESS_CODE = '100000'

    # 响应数据data里面 code key
    REQUEST_DATA_CODE = 'code'

    # 响应数据data里面 msg key
    REQUEST_DATA_MSG = 'msg'
