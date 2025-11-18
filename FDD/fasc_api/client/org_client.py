from .client import CommonClient
from .client import ApiClient
from ..utils.url_params import OpenApiUrlParams

"""
OrgClient
组织架构管理
"""


class OrgClient(ApiClient):

    # 查询部门列表
    def get_corp_dept_list(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CORP_DEPT_GET_LIST, data)

    # 查询部门详情
    def get_corp_dept_detail(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CORP_DEPT_GET_DETAIL, data)

    # 创建部门
    def corp_dept_create(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CORP_DEPT_CREATE, data)

    # 修改部门基本信息
    def corp_dept_modify(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CORP_DEPT_MODIFY, data)

    # 删除部门
    def corp_dept_delete(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CORP_DEPT_DELETE, data)

    # 查询企业成员列表
    def get_corp_member_list(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CORP_MEMBER_GET_LIST, data)

    # 查询成员详情
    def get_corp_member_detail(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CORP_MEMBER_GET_DETAIL, data)

    # 创建成员
    def corp_member_create(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CORP_MEMBER_CREATE, data)

    # 获取成员激活链接
    def get_corp_member_active_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CORP_MEMBER_ACTIVE_URL, data)

    # 修改成员基本信息
    def corp_member_modify(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CORP_MEMBER_MODIFY, data)

    # 设置成员所属部门
    def corp_member_set_dept(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CORP_MEMBER_SET_DEPT, data)

    # 设置成员状态
    def corp_member_set_status(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CORP_MEMBER_SET_STATUS, data)

    # 删除成员
    def corp_member_delete(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CORP_MEMBER_DELETE, data)

    # 获取组织管理链接
    def get_org_manager_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.GET_ORG_MANAGER_URL, data)

    # 查询企业主体列表
    def corp_entity_get_list(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.CORP_ENTITY_GET_LIST, data)
