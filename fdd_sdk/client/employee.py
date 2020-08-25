from .client import CommonClient
from .client import FddClient

"""
员工相关接口
"""
ADD_EMPLOYEE = '/org/employee/addEmployee'
DEL_EMPLOYEE = '/org/employee/delEmployee'


class EmployeeClient(FddClient):
    # 新增员工
    def add_employee(self, token, data={}):
        return CommonClient.post_json(self, ADD_EMPLOYEE, token, data)

    # 删除员工
    def del_employee(self, token, data={}):
        return CommonClient.post_json(self, DEL_EMPLOYEE, token, data)
