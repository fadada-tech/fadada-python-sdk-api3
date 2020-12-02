from .client import CommonClient
from .client import FddClient

'''
组织相关接口
'''

GET_CHILD_COMPANY_LIST = '/org/group/getChildCompanyList'
GET_EMPLOYEE = '/org/group/getEmployee'
GET_ADD_EMPLOYEE_URL = '/org/group/getAddEmployeeUrl'
DEL_EMPLOYEE = '/org/group/delEmployee'
GET_ADD_SUB_COMPANY_URL = '/org/group/getAddSubCompanyUrl'
REMOVE_SUB_COMPANY = '/org/group/removeSubCompany'
GET_CHANGE_COMPANY_MAJOR_URL = '/org/group/getChangeCompanyMajorUrl'


class OrgClient(FddClient):
    # 获取子公司列表
    def get_child_company_list(self, data={}):
        return CommonClient.post_json(self, GET_CHILD_COMPANY_LIST, data)

    # 获取公司员工列表
    def get_employee(self, data={}):
        return CommonClient.post_json(self, GET_EMPLOYEE, data)

    # 获取确认添加员工url
    def get_add_employee_url(self, data={}):
        return CommonClient.post_json(self, GET_ADD_EMPLOYEE_URL, data)

    # 移除员工
    def del_employee(self, data={}):
        return CommonClient.post_json(self, DEL_EMPLOYEE, data)

    # 确认添加子公司url
    def get_add_sub_company_url(self, data={}):
        return CommonClient.post_json(self, GET_ADD_SUB_COMPANY_URL, data)

    # 移除子公司
    def remove_sub_company(self, data={}):
        return CommonClient.post_json(self, REMOVE_SUB_COMPANY, data)

    # 获取变更公司管理员url
    def get_change_company_major_url(self, data={}):
        return CommonClient.post_json(self, GET_CHANGE_COMPANY_MAJOR_URL, data)
