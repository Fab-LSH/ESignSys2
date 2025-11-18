import requests
from requests import Response

from .hashs import HashUtils
from ..exception.exceptions import ClientException


class HttpUtils:

    @staticmethod
    def request_get(url='', params={}, headers={}, timeout=None, log=False) -> Response:
        try:
            # print for testing
            if log:
                print('-------------------------')
                print('url: ' + url)
                print('headers: ' + str(headers))
                print('params: ' + str(params))
                print('-------------------------')
            response = requests.get(url, params=params, headers=headers, timeout=timeout)
            return response
        except Exception as e:
            raise ClientException('request_get', 'GET请求失败', log='request_get 请求失败：%s' % e.__str__())

    @staticmethod
    def request_post(url='', params={}, headers={}, timeout=None, log=False) -> Response:
        try:
            # print for testing
            if log:
                print('-------------------------')
                print('url: ' + url)
                print('headers: ' + str(headers))
                print('params: ' + str(params))
                print('-------------------------')
            response = requests.post(url, data=params, headers=headers, timeout=timeout)
            return response
        except Exception as e:
            raise ClientException('request_post', 'POST请求失败', log='request_post 请求失败：%s' % e.__str__())

    # get方法
    @staticmethod
    def request_get_sign(url, app_id, app_secret, access_token=None, data={},
                         timeout=None, log=False) -> Response:
        try:
            headers, params = HashUtils.get_sign(app_id, app_secret, access_token, data)
            # print for testing
            if log:
                print('-------------------------')
                print('url: ' + url)
                print('headers: ' + str(headers))
                print('params: ' + str(params))
                print('-------------------------')
            response = requests.get(url, params=params, headers=headers, timeout=timeout)
            return response
        except Exception as e:
            raise ClientException('request_get_sign', 'GET请求失败', log='request_get_sign 请求失败：%s' % e.__str__())

    # post方法
    @staticmethod
    def request_post_sign(url, app_id, app_secret, access_token=None, data={}, files={},
                          timeout=None, log=False) -> Response:
        try:
            headers, params = HashUtils.get_sign(app_id, app_secret, access_token, data)
            # print for testing
            if log:
                print('--------request-----------------')
                print('url: ' + url)
                print('headers: ' + str(headers))
                print('params: ' + str(params))
                print('-------------------------')
            response = requests.post(url, data=params, headers=headers, files=files, timeout=timeout)
            if log:
                print('---------response----------------')
                print('headers: ' + str(response.headers))
                print('response: ' + str(response.text))
                print('-------------------------')
            return response
        except ClientException as e:
            raise e
        except Exception as e:
            raise ClientException('request_post_sign', 'POST请求失败', log='request_post_sign 请求失败：%s' % e.__str__())
