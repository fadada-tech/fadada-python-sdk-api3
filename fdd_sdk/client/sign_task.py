from fdd_sdk.client.client import CommonClient
from fdd_sdk.client.client import FddClient

"""
签署任务相关接口
"""

SIGNTASKS_CREATE_BY_FILE = '/signtasks/createByFile'
SIGNTASKS_CREATE_BY_DRAFT_ID = '/signtasks/createByDraftId'
GET_SIGN_URL = '/signtasks/getSignUrl'
GET_TASK_DETAIL_BY_TASK_ID = '/signtasks/getTaskDetailByTaskId'
CANCEL = '/signtasks/cancel'
GET_SENT_URL = '/signtasks/getSentUrl'
URGE_SIGN = '/signtasks/urgeSign'
GET_SIGN_PREVIEW_URL = '/signtasks/getSignPreviewUrl'


class SignTaskClient(FddClient):
    # 利用文件库id创建签署任务
    def signtasks_create_by_file(self, token, data={}):
        return CommonClient.post_json(self, SIGNTASKS_CREATE_BY_FILE, token, data)

    # 根据模板创建签署任务
    def signtasks_create_by_draft_id(self, token, data={}):
        return CommonClient.post_json(self, SIGNTASKS_CREATE_BY_DRAFT_ID, token, data)

    # 获取签署链接
    def get_sign_url(self, token, data={}):
        return CommonClient.post_json(self, GET_SIGN_URL, token, data)

    # 查询签署详情
    def get_task_detail_by_task_id(self, token, data={}):
        return CommonClient.post_json(self, GET_TASK_DETAIL_BY_TASK_ID, token, data)

    # 撤销签署任务
    def cancel(self, token, data={}):
        return CommonClient.post_json(self, CANCEL, token, data)

    # 获取签署任务发起链接
    def get_sent_url(self, token, data={}):
        return CommonClient.post_json(self, GET_SENT_URL, token, data)

    # 催签
    def urge_sign(self, token, data={}):
        return CommonClient.post_json(self, URGE_SIGN, token, data)

    # 获取预览链接
    def get_sign_preview_url(self, token, data={}):
        return CommonClient.post_json(self, GET_SIGN_PREVIEW_URL, token, data)
