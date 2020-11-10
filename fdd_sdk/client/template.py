from .client import CommonClient
from .client import FddClient

"""
模板相关接口
"""


UPLOAD_COMPANY_TEMPLATE_FILE = '/template/uploadCompanyTemplateFile'
UPDATE_COMPANY_TEMPLATE = '/template/updateCompanyTemplate'
GET_EDIT_COMPANY_TEMPLATE_URL = '/template/getEditCompanyTemplateUrl'
DEL_COMPANY_TEMPLATE_FILE = '/template/delCompanyTemplateFile'
GET_COMPANY_TEMPLATE_PREVIEW_URL = '/template/getCompanyTemplatePreviewUrl'
QUERY_COMPANY_TEMPLATE_LIST = '/template/queryCompanyTemplateList'
DOWNLOAD_COMPANY_TEMPLATE_FILE = '/template/downloadCompanyTemplateFile'
GET_TEMPLATE_DETAIL_BY_ID = 'documents/getTemplateDetailById'
CREATE_BY_TEMPLATE_ID = 'documents/createByTemplate'


class TemplateClient(FddClient):
    # 上传企业模板文件
    def upload_company_template_file(self, file, data={}):
        files = {}
        files['file'] = file
        return CommonClient.post_json(self, UPLOAD_COMPANY_TEMPLATE_FILE, data, files)

    # 修改企业模板信息
    def update_company_template(self, data={}):
        return CommonClient.post_json(self, UPDATE_COMPANY_TEMPLATE, data)

    # 获取合同模板控件维护链接
    def get_edit_company_template_url(self, data={}):
        return CommonClient.post_json(self, GET_EDIT_COMPANY_TEMPLATE_URL, data)

    # 删除合同模板文件
    def del_company_template_file(self, data={}):
        return CommonClient.post_json(self, DEL_COMPANY_TEMPLATE_FILE, data)

    # 获取模板预览链接
    def get_company_template_preview_url(self, data={}):
        return CommonClient.post_json(self, GET_COMPANY_TEMPLATE_PREVIEW_URL, data)

    # 模板列表
    def query_company_template_list(self, data={}):
        return CommonClient.post_json(self, QUERY_COMPANY_TEMPLATE_LIST, data)

    # 模板文件下载
    def download_company_template_file(self, data={}):
        return CommonClient.post_stream(self, DOWNLOAD_COMPANY_TEMPLATE_FILE, data)

    # 查询模板详情
    def get_template_detail_by_id(self, data={}):
        return CommonClient.post_json(self, GET_TEMPLATE_DETAIL_BY_ID, data)

    # 填充模板
    def create_by_template_id(self, data={}):
        return CommonClient.post_json(self, CREATE_BY_TEMPLATE_ID, data)
