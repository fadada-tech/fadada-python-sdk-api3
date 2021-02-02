from fdd_sdk.client.client import CommonClient
from fdd_sdk.client.client import FddClient

'''
签署任务相关接口
'''

SIGNTASKS_CREATE_BY_FILE = '/signtasks/createByFile'
SIGNTASKS_CREATE_BY_DRAFT_ID = '/signtasks/createByDraftId'
GET_SIGN_URL = '/signtasks/getSignUrl'
GET_TASK_DETAIL_BY_TASK_ID = '/signtasks/getTaskDetailByTaskId'
CANCEL = '/signtasks/cancel'
GET_SENT_URL = '/signtasks/getSentUrl'
URGE_SIGN = '/signtasks/urgeSign'
GET_SIGN_PREVIEW_URL = '/signtasks/getSignPreviewUrl'
CREATE_TASK_BY_FILE = '/signtasks/createTaskByFile'
CREATE_TASK_BY_DRAFT_ID = '/signtasks/createTaskByDraftId'
UNLOCK = '/signtasks/unlock'
GET_QUICK_SIGN_URL = '/signtasks/getQuickSignUrl'

# 批量签署接口
BATCH_CREATE_BY_DRAFT_ID = '/batch/signtasks/createByDraftId'
BATCH_SENT = '/batch/signtasks/sent'
BATCH_ADD_BY_DRAFT_ID = '/batch/signtasks/addByDraftId'
BATCH_GET_SIGN_URL = '/batch/signtasks/getSignUrl'
BATCH_GET_SIGNTASKS_BY_BATCH_NO = '/batch/signtasks/getSigntasksByBatchNo'


class SignTaskClient(FddClient):
    # 利用文件库id创建签署任务
    def signtasks_create_by_file(self, data={}):
        return CommonClient.post_json(self, SIGNTASKS_CREATE_BY_FILE, data)

    # 根据模板创建签署任务
    def signtasks_create_by_draft_id(self, data={}):
        return CommonClient.post_json(self, SIGNTASKS_CREATE_BY_DRAFT_ID, data)

    # 获取签署链接
    def get_sign_url(self, data={}):
        return CommonClient.post_json(self, GET_SIGN_URL, data)

    # 查询签署详情
    def get_task_detail_by_task_id(self, data={}):
        return CommonClient.post_json(self, GET_TASK_DETAIL_BY_TASK_ID, data)

    # 撤销签署任务
    def cancel(self, data={}):
        return CommonClient.post_json(self, CANCEL, data)

    # 获取签署任务发起链接
    def get_sent_url(self, data={}):
        return CommonClient.post_json(self, GET_SENT_URL, data)

    # 催签
    def urge_sign(self, data={}):
        return CommonClient.post_json(self, URGE_SIGN, data)

    # 获取预览链接
    def get_sign_preview_url(self, data={}):
        return CommonClient.post_json(self, GET_SIGN_PREVIEW_URL, data)

    # 依据原始文件创建签署任务
    def create_task_by_file(self, data={}):
        return CommonClient.post_json(self, CREATE_TASK_BY_FILE, data)

    # 草稿文件创建签署任务
    def create_task_by_draft_id(self, data={}):
        return CommonClient.post_json(self, CREATE_TASK_BY_DRAFT_ID, data)

    # 解锁签署任务
    def unlock(self, data={}):
        return CommonClient.post_json(self, UNLOCK, data)

    # 依据草稿id批量创建签署任务
    def batch_create_by_draft_id(self, data={}):
        return CommonClient.post_json(self, BATCH_CREATE_BY_DRAFT_ID, data)

    # 根据批次号批量发起签署任务
    def batch_sent(self, data={}):
        return CommonClient.post_json(self, BATCH_SENT, data)

    # 根据批次号添加签署任务（依据草稿id创建）
    def batch_add_by_draft_id(self, data={}):
        return CommonClient.post_json(self, BATCH_ADD_BY_DRAFT_ID, data)

    # 根据批次号获取签署链接
    def batch_get_sign_url(self, data={}):
        return CommonClient.post_json(self, BATCH_GET_SIGN_URL, data)

    # 根据批次号查询签署任务
    def batch_get_signtasks_by_batch_no(self, data={}):
        return CommonClient.post_json(self, BATCH_GET_SIGNTASKS_BY_BATCH_NO, data)

    # 获取快捷签署链接
    def get_quick_sign_url(self, data={}):
        return CommonClient.post_json(self, GET_QUICK_SIGN_URL, data)
