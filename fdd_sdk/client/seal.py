from .client import CommonClient
from .client import FddClient

ADD_COMPANY_SEAL = '/seal/addCompanySeal'
DEL_COMPANY_SEAL = '/seal/delCompanySeal'
SEAL_AUTH = '/seal/sealAuth'
CANCEL_SEAL_AUTH = '/seal/cancelSealAuth'
COMPANY_SEAL_LIST = '/seal/companySealList'
COMPANY_SEAL_DETAIL = '/seal/companySealDetail'


class SealClient(FddClient):
    # 上传企业印章
    def add_company_seal(self, token, file,data={}):
        files = {}
        files['image'] = file
        return CommonClient.post_json(self, ADD_COMPANY_SEAL, token, data, files)

    # 删除企业印章
    def del_company_seal(self, token, data={}):
        return CommonClient.post_json(self, DEL_COMPANY_SEAL, token, data)

    # 印章授权
    def seal_auth(self, token, data={}):
        return CommonClient.post_json(self, SEAL_AUTH, token, data)

    # 印章取消授权
    def cancel_seal_auth(self, token, data={}):
        return CommonClient.post_json(self, CANCEL_SEAL_AUTH, token, data)

    # 企业印章列表
    def company_seal_list(self, token, data={}):
        return CommonClient.post_json(self, COMPANY_SEAL_LIST, token, data)

    # 企业印章详请
    def company_seal_detail(self, token, data={}):
        return CommonClient.post_json(self, COMPANY_SEAL_DETAIL, token, data)
