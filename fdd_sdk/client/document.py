from .client import CommonClient
from .client import FddClient

"""
文件相关接口
"""

UPLOAD_FILE = '/documents/uploadFile'
GET_BY_SIGN_FILE_ID = '/documents/getBySignFileId'
GET_BY_DRAFT_ID = '/documents/getByDraftId'
LOOK_UP_COORDINATES = '/documents/lookUpCoordinates'
VERIFY_SIGNATURE = '/documents/verifySignature'
CONTRACT_REPORT_DOWNLOAD = '/documents/professionalContractReportDownload'
DOWNLOAD_EVIDENCE_REPORT = '/documents/downloadEvidenceReport'
UPLOAD_FILE_BY_URL = "/documents/uploadFileByUrl";


class DocumentClient(FddClient):
    # 上传文件
    def upload_file(self, file, data={}):
        files = {}
        files['fileContent'] = file
        return CommonClient.post_json(self, UPLOAD_FILE, data, files)

    # 下载签署文档
    def get_by_sign_file_id(self, data={}):
        return CommonClient.post_stream(self, GET_BY_SIGN_FILE_ID, data)

    # 下载草稿文档
    def get_by_draft_id(self, data={}):
        return CommonClient.post_stream(self, GET_BY_DRAFT_ID, data)

    # 关键字查询坐标
    def look_up_coordinates(self, data={}):
        return CommonClient.post_json(self, LOOK_UP_COORDINATES, data)

    # 合同文件验签
    def verify_signature(self, file, data={}):
        files = {}
        files['file'] = file
        return CommonClient.post_json(self, VERIFY_SIGNATURE, data, files)

    # 下载合同技术报告
    def contract_report_download(self, data={}):
        return CommonClient.post_stream(self, CONTRACT_REPORT_DOWNLOAD, data)

    # 下载公证处报告
    def download_evidence_report(self, data={}):
        return CommonClient.post_stream(self, DOWNLOAD_EVIDENCE_REPORT, data)

    # 文件上传通过链接
    def upload_file_by_url(self, data={}):
        return CommonClient.post_stream(self, UPLOAD_FILE_BY_URL, data)
