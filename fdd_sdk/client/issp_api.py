from fdd_sdk.client.client import CommonClient
from fdd_sdk.client.client import FddClient

'''
ISSP云端接口
'''

SYNC_CONTRACT_FILE_INFO = '/documents/sdk/syncContractFileInfo'
SYNC_TEMPLATE_FILE_INFO = '/documents/sdk/syncTemplateFileInfo'
WITNESS = '/documents/sdk/witness'


class IsspApiClient(FddClient):
    # 同步合同文件数据
    def sync_contract_file_info(self, data={}):
        return CommonClient.post_json(self, SYNC_CONTRACT_FILE_INFO, data)

    # 同步模板文件数据
    def sync_template_file_info(self, data={}):
        return CommonClient.post_json(self, SYNC_TEMPLATE_FILE_INFO, data)

    # 合同文件归档
    def witness(self, data={}):
        return CommonClient.post_json(self, WITNESS, data)
