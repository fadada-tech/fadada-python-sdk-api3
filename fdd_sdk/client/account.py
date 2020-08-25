from .client import FddClient
from .client import CommonClient

"""
账号相关请求
"""

GET_AUTHORIZE_URL_PATH = '/oauth2/getAuthorizeUrl'
GET_PERSON_UNIONID_URL_PATH = '/accounts/getPersonUnionIdUrl'
GET_PERSON_INFO_PATH = '/accounts/getPersonInfo'
GET_COMPANY_UNIONID_URL_PATH = '/accounts/getCompanyUnionIdUrl'
GET_COMPANY_INFO_PATH = '/accounts/getCompanyInfo'
CHECK_ACCOUNT_INFO_PATH = '/accounts/checkAccountInfo'


class AccountClient(FddClient):

    # 获取授权地址
    def get_authorize_url(self, token, data):
        return CommonClient.post_json(self, GET_AUTHORIZE_URL_PATH, token, data)

    # 获取个人unionid链接
    def get_person_unionid_url(self, token, data):
        return CommonClient.post_json(self, GET_PERSON_UNIONID_URL_PATH, token, data)

    # 获取个人信息
    def get_person_info(self, token, data):
        return CommonClient.post_json(self, GET_PERSON_INFO_PATH, token, data)

    # 获取企业unionid链接
    def get_company_unionid_url(self, token, data):
        return CommonClient.post_json(self, GET_COMPANY_UNIONID_URL_PATH, token, data)

    # 获取企业信息
    def get_company_info(self, token, data):
        return CommonClient.post_json(self, GET_COMPANY_INFO_PATH, token, data)

    # 账号信息校验
    def check_account_info(self, token, data):
        return CommonClient.post_json(self, CHECK_ACCOUNT_INFO_PATH, token, data)
