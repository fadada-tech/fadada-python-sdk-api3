from .client import FddClient
from .client import CommonClient

"""
获取token
"""
GET_TOKEN_PATH = '/oauth2/accessToken'


class Oauth2Client(FddClient):

    def get_token(self, data={}):
        return CommonClient.post_json(self, GET_TOKEN_PATH)
