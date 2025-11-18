import hashlib
import hmac
import json
import time
import uuid

from .globals_params import Params
from ..exception.exceptions import ClientException


class HashUtils:

    # 使用HmacSHA256算法哈希(哈希秘钥为secret)，再对hash值使用Base64加密得到最终的签名值sign
    @staticmethod
    def hmac256_hex(secret, data):
        try:
            return hmac.new(secret, data, digestmod='sha256').hexdigest()
        except Exception as e:
            raise ClientException('hmac256_hex', '获取hmac256hex数据失败',
                                  log='hmac256_hex 获取hmac256hex数据失败：%s' % e.__str__())

    # hmc256返回字节
    @staticmethod
    def hmac256_bytes(secret, data):
        try:
            return hmac.new(secret, data, digestmod='sha256').digest()
        except Exception as e:
            raise ClientException('hmac256_bytes', '获取hmac256bytes数据失败',
                                  log='hmac256_bytes 获取hmac256bytes数据失败：%s' % e.__str__())

    # sha256获取hex字符串
    @staticmethod
    def sha256_hex(data):
        try:
            data = data.encode()
            return hashlib.sha256(data).hexdigest();
        except Exception as e:
            raise ClientException('sha256_hex', '字符串sha256失败', log='sha256_hex 字符串sha256失败：%s' % e.__str__())

    # 获取签名信息
    @staticmethod
    def sign(params, timestamp, secret):
        try:
            paramsHex = HashUtils.sha256_hex(params);
            secretBytes = secret.encode(Params.ENCODE_TYPE)
            timestampBytes = timestamp.encode(Params.ENCODE_TYPE)
            firstHmac = HashUtils.hmac256_bytes(secretBytes, timestampBytes);
            paramsHexBytes = paramsHex.encode(Params.ENCODE_TYPE)
            return HashUtils.hmac256_hex(firstHmac, paramsHexBytes);
        except Exception as e:
            raise ClientException('sign', '签名失败', log='sign 签名失败：%s' % e.__str__())

    # 字典排序后拼接成字符串
    @staticmethod
    def sort_params(params_dict={}):
        try:
            result_str = ""
            sort_dict = sorted(params_dict.items())
            for param_key, param_value in sort_dict:
                result_str += Params.DICT_TO_STR % (param_key, param_value)
            return result_str[:-1]
        except Exception as e:
            raise ClientException('sort_params', '字典数据排序拼接失败', log='sort_params 字典数据排序拼接失败：%s' % e.__str__())

    # 字典排序后拼接成字符串,过滤值为空的对象
    @staticmethod
    def sort_params_skip_empty(params_dict={}):
        try:
            result_str = ""
            sort_dict = sorted(params_dict.items())
            for param_key, param_value in sort_dict:
                if param_value != '':
                    result_str += Params.DICT_TO_STR % (param_key, param_value)
            return result_str[:-1]
        except Exception as e:
            raise ClientException('sort_params', '字典数据排序拼接失败', log='sort_params 字典数据排序拼接失败：%s' % e.__str__())

    # 获取签名后的请求头字典
    @staticmethod
    def get_sign(app_id, app_secret, access_token=None, data={}):
        try:
            params_heacer_dict = {}
            params_dict = {}
            header_dict = {}
            # 如果是字符串就不json化，字典就json化
            if type(data) is str:
                params_dict[Params.DATA_KEY] = data
                params_heacer_dict.update(params_dict)
            elif data is not None:
                params_dict[Params.DATA_KEY] = json.dumps(data)
                params_heacer_dict.update(params_dict)

            # 设置默认参数
            time_stamp = str(int(round(time.time() * 1000)))
            header_dict[Params.TIMESTAMP] = time_stamp
            header_dict[Params.NONCE] = uuid.uuid4().__str__().replace('-', '')
            header_dict[Params.APP_ID] = app_id
            # 设置FASC.API子版本号
            header_dict[Params.SUB_VERSION] = '5.1'

            header_dict[Params.SIGN_TYPE] = Params.SIGN_TYPE_SHA
            # token不为空就放入请求头里面
            if access_token is not None and len(access_token) != 0:
                header_dict[Params.ACCESS_TOKEN] = access_token
            else:
                header_dict[Params.GRANT_TYPE] = Params.GRANT_TYPE_CLIENT
            # 把请求头更新到请求参数字典里面
            params_heacer_dict.update(header_dict)
            # 请求头和请求参数拼接
            sort_params_str = HashUtils.sort_params(params_heacer_dict)
            sign_str = HashUtils.sign(sort_params_str, time_stamp, app_secret)
            # 在请求头字典中加入签名值
            header_dict[Params.SIGN] = sign_str
            return header_dict, params_dict
        except Exception as e:
            raise ClientException('get_sign', '获取签名值失败', log='get_sign 获取签名值失败：%s' % e.__str__())

    # 文件字节sha256 hex值
    @staticmethod
    def sha256_bytes_hex(res):
        try:
            sh = hashlib.sha256()
            sh.update(res)
            return sh.hexdigest()
        except Exception as e:
            raise ClientException('sha256_bytes_hex', 'bytes类型数据sha256失败',
                                  log='sha256_bytes_hex bytes类型数据sha256失败：%s' % e.__str__())

    # 文件sha256 hex值
    @staticmethod
    def sha256_file_hex(file_path):
        try:
            with open(file_path, 'rb') as f:
                res = f.read()
            return HashUtils.sha256_bytes_hex(res)
        except Exception as e:
            raise ClientException('sha256_file_hex', '文件sha256失败', log='sha256_file_hex 文件sha256失败：%s' % e.__str__())
