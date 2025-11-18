from .client import CommonClient
from .client import ApiClient
from ..utils.url_params import OpenApiUrlParams

"""
SignTaskClient
签署任务管理
"""


class SignTaskClient(ApiClient):

    # 创建签署任务
    def create(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_CREATE, data)

    # 创建签署任务（基于签署模板）
    def create_with_template(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_CREATE_WITH_TEMPLATE, data)

    # 添加签署任务文档
    def add_doc(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_DOC_ADD, data)

    # 移除签署任务文档
    def delete_doc(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_DOC_DELETE, data)

    # 添加签署任务控件
    def add_field(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_FIELD_ADD, data)

    # 移除签署任务控件
    def delete_field(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_FIELD_DELETE, data)

    # 添加签署任务附件
    def add_attach(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_ATTACH_ADD, data)

    # 移除签署任务附件
    def delete_attach(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_ATTACH_DELETE, data)

    # 添加签署任务参与方
    def add_actor(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_ACTOR_ADD, data)

    # 移除签署任务参与方
    def delete_actor(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_ACTOR_DELETE, data)

    # 发起签署任务
    def start(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_START, data)

    # 填写签署任务控件内容
    def fill_field_values(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_FIELD_FILL_VALUES, data)

    # 定稿签署任务
    def finalize_doc(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_DOC_FINALIZE, data)

    # 阻塞签署任务
    def block(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_BLOCK, data)

    # 解阻签署任务
    def unblock(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_UNBLOCK, data)

    # 撤销签署任务
    def cancel(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_CANCEL, data)

    # 获取应用的签署任务详情
    def get_detail(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_GET_DETAIL, data)

    # 获取指定归属方的签署任务列表
    def get_owner_list(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_OWNER_GET_LIST, data)

    # 获取指定归属方的签署任务文档下载地址
    def get_owner_download_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_OWNER_GET_DOWNLOAD_URL, data)

    # 获取参与方专属链接
    def sign_task_actor_get_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_ACTOR_GET_URL, data)

    # 查询企业签署任务文件夹
    def sign_task_cataloglist(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_CATALOG_LIST, data)

    # 查询签署任务控件信息
    def list_sign_task_field(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_FIELD_LIST, data)

    # 查询签署任务参与方信息
    def list_sign_task_actor(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_ACTOR_LIST, data)

    # 查询签署任务审批信息
    def get_approval_info(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_GET_APPROVAL_INFO, data)

    # 获取批量签署链接
    def get_batch_sign_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_GET_BATCH_SIGN_URL, data)

    # 获取签署任务编辑链接
    def get_sign_task_edit_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_GET_EDIT_URL, data)

    # 获取签署任务预览链接
    def get_sign_task_preview_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_GET_PREVIEW_URL, data)

    # 催办签署任务
    def sign_task_urge(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_URGE, data)

    # 获取签署任务公证处保全报告
    def get_download_evidence_report(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.GET_SIGN_TASK_DOWNLOAD_EVIDENCE_REPORT_URL, data)

    # 删除签署任务
    def delete_sign_task(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_DELETE, data)

    # 结束签署任务
    def finish_sign_task(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_FINISH, data)

    # 查询签署业务类型列表
    def get_sign_task_business_type_list(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.GET_SIGN_TASK_BUSINESS_TYPE_LIST, data)

    # 查询参与方的签署刷脸底图
    def get_sign_task_face_picture(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.GET_SIGN_TASK_FACE_PICTURE, data)

    # 作废签署任务
    def sign_task_abolish(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_ABOLISH, data)

    # 签署文档切图
    def get_sign_task_owner_slicing_ticket_id(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.GET_SIGN_TASK_OWNER_SLICING_TICKET_ID, data)

    # 获取图片版签署文档下载地址
    def get_sign_task_owner_pic_download_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.GET_SIGN_TASK_OWNER_PIC_DOWNLOAD_URL, data)

    # 获取参与方签署音视频下载地址
    def get_audio_video_download_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.GET_AUDIO_VIDEO_DOWNLOAD_URL, data)

    # 获取V3签署任务链接
    def sign_task_actor_v3_get_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_ACTOR_V3_GET_URL, data)

    # 获取历史文件对比数据
    def get_compare_result_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.GET_COMPARE_RESULT_URL, data)

    # 修改签署任务参与方
    def sign_task_actor_modify(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_ACTOR_MODIFY, data)

    # 签署任务延期
    def sign_task_extension(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_EXTENSION, data)

    # 签署任务驳回填写
    def sign_task_ignore(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_IGNORE, data)

    # 获取送达查看报告下载地址
    def sign_task_message_report_get_download_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_MESSAGE_REPORT_GET_DOWNLOAD_URL, data)

    # 查询审批流程详情
    def approval_flow_get_list(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.APPROVAL_FLOW_GET_LIST, data)

    # 查询审批流程详情
    def approval_flow_get_detail(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.APPROVAL_FLOW_GET_DETAIL, data)

    # 获取预填充链接
    def sign_task_get_prefill_url(self, data):
        return CommonClient.post_json(self, OpenApiUrlParams.SIGN_TASK_GET_PREFILL_URL, data)
