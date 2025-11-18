import logging

logging.basicConfig(format='%(asctime)s - '
                           '%(pathname)s[line:%(lineno)d] -'
                           ' %(levelname)s: %(message)s',
                    level=logging.ERROR)


class ApiClient():
    """
    app_id应用appId,
    app_secret 应用appSecret ,
    request_url服务请求地址，
    access_token请求返回的accessToken,
    log 是否日志
    timeout超时时间，默认不设置
    """
    app_id = ''
    app_secret = ''
    request_url = ''
    access_token = ''
    log = False
    timeout = None

    def __init__(self, app_id, app_key, request_url='', timeout=None, log=False):
        ApiClient.app_id = app_id
        ApiClient.app_secret = app_key
        ApiClient.timeout = timeout
        if request_url is not None and str.startswith(request_url, 'http:') or str.startswith(request_url, 'https:'):
            ApiClient.request_url = request_url
        ApiClient.log = log == True

    def set_access_token(self, token):
        self.access_token = token


from fasc_api.utils.globals_params import Params
from fasc_api.exception.exceptions import ClientException
from fasc_api.exception.exceptions import ServerException
from fasc_api.utils.https import HttpUtils


# 公共客户端
class CommonClient(ApiClient):

    def request(self, url, type='post_json', data={}, files={}):
        try:
            if type == 'post_json':
                result_json = HttpUtils.request_post_sign(self.request_url + url, self.app_id, self.app_secret,
                                                          self.access_token, data, files=files,
                                                          timeout=self.timeout, log=self.log).json()
            if type == 'get_json':
                result_json = HttpUtils.request_get_sign(self.request_url + url, self.app_id, self.app_secret,
                                                         self.access_token, data, timeout=self.timeout,
                                                         log=self.log).json()
            result = None
            if type == 'post_stream':
                result = HttpUtils.request_post_sign(self.request_url + url, self.app_id, self.app_secret,
                                                     self.access_token, data, timeout=self.timeout, log=self.log)
            if type == 'get_stream':
                result = HttpUtils.request_get_sign(self.request_url + url, self.app_id, self.app_secret,
                                                    self.access_token, data, timeout=self.timeout, log=self.log)

            if result is not None and result.headers['content-type'].__contains__('application/json'):
                result_json = result.json()
            elif result is not None:
                return result;

        except ClientException as e:
            if self.log:
                logging.error(e.log)
            raise e
        except Exception as e:
            if self.log:
                logging.error("request 请求失败%s" % e)
            raise ClientException('request', '请求失败')
        if result_json is None:
            if self.log:
                logging.error("request 请求失败%s" % result_json)
            raise ServerException('request', '请求失败')

        code = result_json[Params.REQUEST_DATA_CODE]
        if code != Params.REQUEST_SUCCESS_CODE:
            msg = result_json[Params.REQUEST_DATA_MSG]
            if self.log:
                logging.error(result_json)
            raise ServerException(code, msg)
        return result_json

    # post 请求 返回json
    @staticmethod
    def post_json(self, url, data={}, files={}):
        return CommonClient.request(self, url, "post_json", data, files)

    # get请求 返回json
    @staticmethod
    def get_json(self, url, data={}):
        return CommonClient.request(self, url, "get_json", data)

    # post 请求 返回stream
    @staticmethod
    def post_stream(self, url, data={}):
        return CommonClient.request(self, url, "post_stream", data)

    # get请求 返回stream
    @staticmethod
    def get_stream(self, url, data={}):
        return CommonClient.request(self, url, "get_stream", data)
