from .client import FddClient
from .client import CommonClient

"""
授权
"""
GET_TOKEN_PATH = '/oauth2/accessToken'
GET_AUTHORIZE_URL_PATH = '/oauth2/getAuthorizeUrl'

GET_AUTO_SIGN_AUTH_URL = "/oauth2/getAutoSignAuthUrl";
CANCEL_AUTH_SIGN_AUTH = "/oauth2/cancelAuthSignAuth";


class Oauth2Client(FddClient):

    # 获取token
    def get_token(self, data={}):
        return CommonClient.post_json(self, GET_TOKEN_PATH, None)

    # 获取授权地址
    def get_authorize_url(self, data):
        return CommonClient.post_json(self, GET_AUTHORIZE_URL_PATH, data)

    # 获取自动签署授权地址
    def get_auto_sign_auth_url(self, data):
        return CommonClient.post_json(self, GET_AUTO_SIGN_AUTH_URL, data)

    # 取消自动签署授权
    def cancel_auth_sign_auth(self, data):
        return CommonClient.post_json(self, CANCEL_AUTH_SIGN_AUTH, data)
