from fasc_api.client.org_client import OrgClient
from fasc_api.client.service_client import ServiceClient
from fasc_api.exception.exceptions import ClientException
from fasc_api.exception.exceptions import ServerException

from init_demo_data import InitDemoData

api_client = InitDemoData.api_client
access_token = ServiceClient.get_access_token_value(api_client)
api_client.set_access_token(access_token)


# 查询部门列表
def get_corp_dept_list_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "parentDeptId": 1677068453000
        }
        res = OrgClient.get_corp_dept_list(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询部门详情
def get_corp_dept_detail_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "deptId": "19800001115"
        }
        res = OrgClient.get_corp_dept_detail(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 创建部门
def corp_dept_create_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "deptName": "销售部",
            "deptOrderNum": 1,
            "parentDeptId": 19800001115
        }
        res = OrgClient.corp_dept_create(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 修改部门基本信息
def corp_dept_modify_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "deptId": 19800001115,
            "deptOrderNum": 1,
            "deptName": "销售部"
        }
        res = OrgClient.corp_dept_modify(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 删除部门
def corp_dept_delete_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "deptId": 19800001115
        }
        res = OrgClient.corp_dept_delete(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询企业成员列表
def get_corp_member_list_demo():
    try:
        data = {
            "ownerId": "072ab28e646d4157adfe4b00009517d3",
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "listFilter": {
                "roleType": "super_admin",
                "deptId": 0,
                "fetchChild": False
            },
            "listPageNo": 0,
            "listPageSize": 10
        }
        res = OrgClient.get_corp_member_list(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询成员详情
def get_corp_member_detail_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "memberId": "1677068453000",
            "internalIdentifier": ""
        }
        res = OrgClient.get_corp_member_detail(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 创建成员
def corp_member_create_demo():
    try:
        data = {
            "employeeInfos": [
                {
                    "memberId": 1677068453000,
                    "memberName": "谢盛",
                    "internalIdentifier": "173000",
                    "memberEmail": "123@qq.com",
                    "memberMobile": "19800001115",
                    "memberStatus": "inactive",
                    "memberDeptIds": [
                        18438605689
                    ],
                    "roleType": [
                        "super_admin"
                    ]
                }
            ],
            "mergeMemberInfo": False,
            "redirectUrl": "",
            "notifyActiveByEmail": False
        }
        res = OrgClient.corp_member_create(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取成员激活链接
def get_corp_member_active_url_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "memberId": 1677068453000,
            "redirectUrl": ""
        }
        res = OrgClient.get_corp_member_active_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 修改成员基本信息
def corp_member_modify_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "memberId": 1677068453000,
            "memberName": "谢盛",
            "internalIdentifier": "173000",
            "memberEmail": "123@qq.com",
            "memberMobile": "19800001115",
            "memberDeptIds": [
                18438605689
            ]
        }
        res = OrgClient.corp_member_modify(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 设置成员所属部门
def corp_member_set_dept_demo():
    try:
        data = {
            "memberId": 1677068453000,
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "memberDeptIds": [
                1980000
            ],
            "model": "cover"
        }
        res = OrgClient.corp_member_set_dept(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 设置成员状态
def corp_member_set_status_demo():
    try:
        data = {
            "memberId": 1677068453000,
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "memberStatus": "enable"
        }
        res = OrgClient.corp_member_set_status(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 删除成员
def corp_member_delete_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "memberId": 1677068453000
        }
        res = OrgClient.corp_member_delete(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 企业管理链接
def get_org_manager_url_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "clientUserId": "AutoClientUserId1656985245",
            "modules": [
                "member"
            ],
            "redirectUrl": "http://www.baidu.com"
        }
        res = OrgClient.get_org_manager_url(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询企业主体列表
def corp_entity_get_list_demo():
    try:
        data = {
            "openCorpId": "cf6c41520b6544f590b6e6909ca7d488",
            "clientUserId": "AutoClientUserId1656985245",
            "modules": [
                "member"
            ],
            "redirectUrl": "http://www.baidu.com"
        }
        res = OrgClient.corp_entity_get_list(api_client, data)
        print(res)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


if __name__ == '__main__':
    # 查询部门列表
    # get_corp_dept_list_demo()
    # 查询部门详情
    # get_corp_dept_detail_demo()
    # 查询部门详情
    # corp_dept_create_demo()
    # 修改部门基本信息
    # corp_dept_modify_demo()
    # 删除部门
    # corp_dept_delete_demo()
    # 查询企业成员列表
    # get_corp_member_list_demo()
    # 查询成员详情
    # get_corp_member_detail_demo()
    # 创建成员
    # corp_member_create_demo()
    # 获取成员激活链接
    # get_corp_member_active_url_demo()
    # 修改成员基本信息
    # corp_member_modify_demo()
    # 设置成员所属部门
    # corp_member_set_dept_demo()
    # 设置成员状态
    # corp_member_set_status_demo()
    # 删除成员
    # corp_member_delete_demo()
    # 企业管理链接
    # get_org_manager_url_demo()
    # 查询企业主体列表
    corp_entity_get_list_demo()
