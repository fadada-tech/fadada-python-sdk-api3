from fdd_sdk.client.client import CommonClient
from fdd_sdk.client.client import FddClient

'''
定稿任务相关接口
'''

CREATE_REVISE_TASK = '/reviseTask/createReviseTask'
GET_FILL_FILE_URL = '/reviseTask/getFillFileUrl'
CANCEL_REVISE_TASK = '/reviseTask/cancelReviseTask'
REVISE_TASK_DETAIL = '/reviseTask/reviseTaskDetail'
SAVE_FILL_VALUES = '/reviseTask/saveFillValues'


class ReviseTaskClient(FddClient):
    # 创建定稿任务
    def create_revise_task(self, data={}):
        return CommonClient.post_json(self, CREATE_REVISE_TASK, data)

    # 获取填充链接
    def get_fill_file_url(self, data={}):
        return CommonClient.post_json(self, GET_FILL_FILE_URL, data)

    # 定稿任务撤销
    def cancel_revise_task(self, data={}):
        return CommonClient.post_json(self, CANCEL_REVISE_TASK, data)

    # 定稿任务详请
    def revise_task_detail(self, data={}):
        return CommonClient.post_json(self, REVISE_TASK_DETAIL, data)

    # 接口填充
    def save_fill_values(self, data={}):
        return CommonClient.post_json(self, SAVE_FILL_VALUES, data)
