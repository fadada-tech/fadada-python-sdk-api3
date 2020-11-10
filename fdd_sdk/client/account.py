from .client import FddClient
from .client import CommonClient

'''
账号相关请求
'''

GET_PERSON_UNIONID_URL_PATH = '/accounts/getPersonUnionIdUrl'
GET_PERSON_INFO_PATH = '/accounts/getPersonInfo'
GET_COMPANY_UNIONID_URL_PATH = '/accounts/getCompanyUnionIdUrl'
GET_COMPANY_INFO_PATH = '/accounts/getCompanyInfo'
CHECK_ACCOUNT_INFO_PATH = '/accounts/checkAccountInfo'
GET_ACCESS_OBJECT_INFO = 'accounts/getAccessObjectInfo'

# 第三方服务相关接口
GET_OPEN_SERVER_URL = 'thirdUser/getOpenServerUrl'
GET_USER_TOKEN = 'thirdUser/getUserToken'
CANCE_SERVER = 'thirdUser/cancel'


class AccountClient(FddClient):

    # 获取个人unionid链接
    def get_person_unionid_url(self, data):
        return CommonClient.post_json(self, GET_PERSON_UNIONID_URL_PATH, data)

    # 获取个人信息
    def get_person_info(self, data):
        return CommonClient.post_json(self, GET_PERSON_INFO_PATH, data)

    # 获取企业unionid链接
    def get_company_unionid_url(self, data):
        return CommonClient.post_json(self, GET_COMPANY_UNIONID_URL_PATH, data)

    # 获取企业信息
    def get_company_info(self, data):
        return CommonClient.post_json(self, GET_COMPANY_INFO_PATH, data)

    # 账号信息校验
    def check_account_info(self, data):
        return CommonClient.post_json(self, CHECK_ACCOUNT_INFO_PATH, data)

    # 获取接入方信息
    def get_access_object_info(self, data):
        return CommonClient.post_json(self, GET_ACCESS_OBJECT_INFO, data)

    # 获取第三方授权地址
    def get_open_server_url(self, data):
        return CommonClient.post_json(self, GET_OPEN_SERVER_URL, data)

    # 获取userToken
    def get_user_token(self, data):
        return CommonClient.post_json(self, GET_USER_TOKEN, data)

    # 取消第三方授权
    def cancel_server(self, data):
        return CommonClient.post_json(self, CANCE_SERVER, data)
