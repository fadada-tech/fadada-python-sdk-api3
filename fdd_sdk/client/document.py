from .client import CommonClient
from .client import FddClient

"""
文件相关接口
"""

GET_TEMPLATE_DETAIL_BY_ID = '/documents/getTemplateDetailById'
UPLOAD_FILE = '/documents/uploadFile'
GET_BY_SIGN_FILE_ID = '/documents/getBySignFileId'
GET_BY_DRAFT_ID = '/documents/getByDraftId'
CREATE_BY_TEMPLATE_ID = '/documents/createByTemplate'
LOOK_UP_COORDINATES = '/documents/lookUpCoordinates'
VERIFY_SIGNATURE = '/documents/verifySignature'
CONTRACT_REPORT_DOWNLOAD = '/documents/professionalContractReportDownload'
DOWNLOAD_EVIDENCE_REPORT = '/documents/downloadEvidenceReport'


class DocumentClient(FddClient):
    # 查询模板详情
    def get_template_detail_by_id(self, token, data={}):
        return CommonClient.post_json(self, GET_TEMPLATE_DETAIL_BY_ID, token, data)

    # 上传文件
    def upload_file(self, token, file, data={}):
        files = {}
        files['fileContent'] = file
        return CommonClient.post_json(self, UPLOAD_FILE, token, data, files)

    # 下载签署文档
    def get_by_sign_file_id(self, token, data={}):
        return CommonClient.post_stream(self, GET_BY_SIGN_FILE_ID, token, data)

    # 下载草稿文档
    def get_by_draft_id(self, token, data={}):
        return CommonClient.post_stream(self, GET_BY_DRAFT_ID, token, data)

    # 填充模板
    def create_by_template_id(self, token, data={}):
        return CommonClient.post_json(self, CREATE_BY_TEMPLATE_ID, token, data)

    # 关键字查询坐标
    def look_up_coordinates(self, token, data={}):
        return CommonClient.post_json(self, LOOK_UP_COORDINATES, token, data)

    # 合同文件验签
    def verify_signature(self, token, file, data={}):
        files = {}
        files['file'] = file
        return CommonClient.post_json(self, VERIFY_SIGNATURE, token, data, files)

    # 下载合同技术报告
    def contract_report_download(self, token, data={}):
        return CommonClient.post_stream(self, CONTRACT_REPORT_DOWNLOAD, token, data)

    # 下载公证处报告
    def download_evidence_report(self, token, data={}):
        return CommonClient.post_stream(self, DOWNLOAD_EVIDENCE_REPORT, token, data)
