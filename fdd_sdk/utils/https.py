import requests

from .hashs import HashUtils

from requests import Response
from ..exception.exceptions import ClientException


class HttpUtils:

    @staticmethod
    def request_get(url='', params={}, headers={}) -> Response:
        try:
            response = requests.get(url, params=params, headers=headers)
            return response
        except Exception as e:
            raise ClientException('request_get', 'GET请求失败', 'request_get 请求失败：%s' % e)

    @staticmethod
    def request_post(url='', params={}, headers={}) -> Response:
        try:
            response = requests.post(url, data=params, headers=headers)
            return response
        except Exception as e:
            raise ClientException('request_post', 'POST请求失败', 'request_post 请求失败：%s' % e)

    # post方法（无需签名，内部已处理）
    @staticmethod
    def request_get_sign(url, app_id, app_key, token=None, data={}) -> Response:
        try:
            headers, params = HashUtils.get_sign(app_id, app_key, token, data)
            response = requests.get(url, params=params, headers=headers)
            return response
        except Exception as e:
            raise ClientException('request_get_sign', 'GET请求失败', 'request_get_sign 请求失败：%s' % e)

    # post方法（无需签名，内部已处理）
    @staticmethod
    def request_post_sign(url, app_id, app_key, token=None, data={}, files={}) -> Response:
        try:
            headers, params = HashUtils.get_sign(app_id, app_key, token, data)
            if files is None or len(files) == 0:
                response = requests.post(url, data=params, headers=headers)
            else:
                response = requests.post(url, data=params, headers=headers, files=files)
            return response
        except ClientException as e:
            raise e
        except Exception as e:
            raise ClientException('request_post_sign', 'POST请求失败', 'request_post_sign 请求失败：%s' % e)
