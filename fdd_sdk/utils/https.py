import requests

from .hashs import HashUtils

from requests import Response
from ..exception.exceptions import ClientException


class HttpUtils:

    @staticmethod
    def request_get(url='', params={}, headers={}, timeout=None) -> Response:
        try:
            response = requests.get(url, params=params, headers=headers, timeout=timeout)
            return response
        except Exception as e:
            raise ClientException('request_get', 'GET请求失败', log='request_get 请求失败：%s' % e.__str__())

    @staticmethod
    def request_post(url='', params={}, headers={}, timeout=None) -> Response:
        try:
            response = requests.post(url, data=params, headers=headers, timeout=timeout)
            return response
        except Exception as e:
            raise ClientException('request_post', 'POST请求失败', log='request_post 请求失败：%s' % e.__str__())

    # post方法（无需签名，内部已处理）
    @staticmethod
    def request_get_sign(url, app_id, app_key, token=None, user_token=None, data={}, timeout=None) -> Response:
        try:
            headers, params = HashUtils.get_sign(app_id, app_key, token, user_token, data)
            response = requests.get(url, params=params, headers=headers, timeout=timeout)
            return response
        except Exception as e:
            raise ClientException('request_get_sign', 'GET请求失败', log='request_get_sign 请求失败：%s' % e.__str__())

    # post方法（无需签名，内部已处理）
    @staticmethod
    def request_post_sign(url, app_id, app_key, token=None, user_token=None, data={}, files={},
                          timeout=None) -> Response:
        try:
            headers, params = HashUtils.get_sign(app_id, app_key, token, user_token, data)
            response = requests.post(url, data=params, headers=headers, files=files, timeout=timeout)
            return response
        except ClientException as e:
            raise e
        except Exception as e:
            raise ClientException('request_post_sign', 'POST请求失败', log='request_post_sign 请求失败：%s' % e.__str__())


