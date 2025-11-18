class OpenApiUrlParams:
    # ServiceClient
    # ServiceClient 获取服务访问凭证
    SERVICE_GET_ACCESS_TOKEN = '/service/get-access-token'
    # ServiceClient 获取应用级资源访问凭证(暂不对外开放)。
    # SERVICE_GET_APP_ACCESS_TICKET = '/service/get-app-access-ticket'
    # ServiceClient 获取用户级资源访问凭证(暂不对外开放)。
    # SERVICE_GET_USER_ACCESS_TICKET = '/service/get-user-access-ticket'

    # UserClient 应用的个人用户帐号管理
    USER_DISABLE = '/user/disable'
    USER_ENABLE = '/user/enable'
    USER_UNBIND = '/user/unbind'
    USER_GET = '/user/get'
    USER_GET_IDENTITY_INFO = '/user/get-identity-info'

    # CorpClient 应用的企业用户帐号管理
    CORP_DISABLE = '/corp/disable'
    CORP_ENABLE = '/corp/enable'
    CORP_UNBIND = '/corp/unbind'
    CORP_GET_DETAIL = '/corp/get'
    CORP_GET_IDENTITY_INFO = '/corp/get-identity-info'
    CORP_GET_IDENTIFIED_STATUS = '/corp/get-identified-status'

    COUNTERPART_GET_LIST = "/counterpart/get-list"

    # OrgClient 组织管理
    CORP_DEPT_GET_LIST = "/corp/dept/get-list"
    CORP_DEPT_GET_DETAIL = "/corp/dept/get-detail"
    CORP_DEPT_CREATE = "/corp/dept/create"
    CORP_DEPT_MODIFY = "/corp/dept/modify"
    CORP_DEPT_DELETE = "/corp/dept/delete"
    CORP_MEMBER_GET_LIST = "/corp/member/get-list"
    CORP_MEMBER_GET_DETAIL = "/corp/member/get-detail"
    CORP_MEMBER_CREATE = "/corp/member/create"
    CORP_MEMBER_ACTIVE_URL = "/corp/member/get-active-url"
    CORP_MEMBER_MODIFY = "/corp/member/modify"
    CORP_MEMBER_SET_DEPT = "/corp/member/set-dept"
    CORP_MEMBER_SET_STATUS = "/corp/member/set-status"
    CORP_MEMBER_DELETE = "/corp/member/delete"
    GET_ORG_MANAGER_URL = "/corp/organization/manage/get-url"
    CORP_ENTITY_GET_LIST = "/corp/entity/get-list"

    # SealClient 印章管理
    SEAL_GET_LIST = "/seal/get-list"
    SEAL_GET_USER_LIST = "/seal/get-user-list"
    SEAL_GET_DETAIL = "/seal/get-detail"
    SEAL_GET_APPOINTED_URL = "/seal/manage/get-appointed-seal-url"
    GET_USER_SEAL_LIST = "/seal/user/get-list"
    SEAL_GET_CREATE_URL = "/seal/create/get-url"
    SEAL_GET_VERIFY_LIST = "/seal/verify/get-list"
    SEAL_MODIFY = "/seal/modify"
    SEAL_GET_GRANT_URL = "/seal/grant/get-url"
    SEAL_CANCEL_GRANT = "/seal/grant/cancel"
    SEAL_SET_STATUS = "/seal/set-status"
    SEAL_DELETE = "/seal/delete"
    SEAL_GET_MANAGE_URL = "/seal/manage/get-url"
    SEAL_GET_FREE_SIGN_URL = "/seal/free-sign/get-url"
    PERSONAL_SEAL_GET_LIST = "/personal-seal/get-list"
    PERSONAL_SEAL_GET_FREE_SIGN_URL = "/personal-seal/free-sign/get-url"
    CANCEL_SEAL_FREE_SIGN = "/seal/free-sign/cancel"
    PERSONAL_SEAL_FREE_SIGN_CANCEL = "/personal-seal/free-sign/cancel"
    PERSONAL_SEAL_GET_MANAGE_URL = "/personal-seal/manage/get-url";
    PERSONAL_SEAL_GET_CREATE_URL = "/personal-seal/create/get-url";
    PERSONAL_SEAL_DELETE = "/personal-seal/delete";
    SEAL_CREATE_BY_TEMPLATE = "/seal/create-by-template";
    SEAL_CREATE_BY_IMAGE = "/seal/create-by-image";
    SEAL_CREATE_LEGAL_REPRESENTATIVE_BY_TEMPLATE = "/seal/create-legal-representative-by-template";
    SEAL_CREATE_LEGAL_REPRESENTATIVE_BY_IMAGE = "/seal/create-legal-representative-by-image";
    PERSONAL_SEAL_CREATE_BY_TEMPLATE = "/personal-seal/create-by-template";
    PERSONAL_SEAL_CREATE_BY_IMAGE = "/personal-seal/create-by-image";


    # DocClient 文档
    FILE_UPLOAD_BY_URL = '/file/upload-by-url'
    FILE_GET_UPLOAD_URL = '/file/get-upload-url'
    FILE_PROCESS = '/file/process'
    OCR_EDIT_GET_COMPARE_URL = "/ocr/edit/get-compare-url"
    OCR_EDIT_GET_RESULT_COMPARE_URL = "/ocr/edit/compare-result-url"
    OCR_EDIT_GET_EXAMINE_URL = "/ocr/edit/get-examine-url"
    OCR_EDIT_GET_RESULT_EXAMINE_URL = "/ocr/edit/examine-result-url"
    OCR_EDIT_GET_EXAMINE_RESULT_DATA = "/ocr/edit/examine-result-data"
    DOC_POST_FILE_VERIFY_SIGN = "/file/verify-sign"
    FILE_GET_KEYWORD_POSITIONS = "/file/get-keyword-positions"

    # TemplateClient 文档模板
    DOC_TEMPLATE_GET_LIST = "/doc-template/get-list"
    DOC_TEMPLATE_GET_DETAIL = "/doc-template/get-detail"
    SIGN_TEMPLATE_GET_LIST = "/sign-template/get-list"
    SIGN_TEMPLATE_GET_DETAIL = "/sign-template/get-detail"
    SIGN_TEMPLATE_GET_CREATE_URL = "/template/create/get-url"
    SIGN_TEMPLATE_GET_EDIT_URL = "/template/edit/get-url"
    SIGN_TEMPLATE_GET_PREVIEW_URL = "/template/preview/get-url"
    SIGN_TEMPLATE_GET_MANAGE_URL = "/template/manage/get-url"
    APP_DOC_TEMPLATE_GET_LIST = "/app-doc-template/get-list"
    APP_DOC_TEMPLATE_GET_DETAIL = "/app-doc-template/get-detail"
    APP_SIGN_TEMPLATE_GET_LIST = "/app-sign-template/get-list"
    APP_SIGN_TEMPLATE_GET_DETAIL = "/app-sign-template/get-detail"
    APP_TEMPLATE_CREATE_GET_URL = "/app-template/create/get-url"
    APP_TEMPLATE_EDIT_GET_URL = "/app-template/edit/get-url"
    APP_TEMPLATE_PREVIEW_GET_URL = "/app-template/preview/get-url"
    APP_FIELD_CREATE = "/app-field/create"
    APP_FIELD_MODIFY = "/app-field/modify"
    APP_FIELD_SET_STATUS = "/app-field/set-status"
    APP_FIELD_GET_LIST = "/app-field/get-list"
    APP_DOC_TEMPLATE_SET_STATUS = "/app-doc-template/set-status"
    APP_DOC_TEMPLATE_DELETE = "/app-doc-template/delete"
    APP_DOC_SIGN_TEMPLATE_SET_STATUS = "/app-sign-template/set-status"
    APP_DOC_SIGN_TEMPLATE_DELETE = "/app-sign-template/delete"
    DOC_TEMPLATE_SET_STATUS = "/doc-template/set-status"
    DOC_TEMPLATE_DELETE = "/doc-template/delete"
    SIGN_TEMPLATE_SET_STATUS = "/sign-template/set-status"
    SIGN_TEMPLATE_DELETE = "/sign-template/delete"
    CREATE_CORP_FIELD = "/corp-field/create"
    GET_CORP_FIELD_LIST = "/corp-field/get-list"
    DELETE_CORP_FIELD = "/corp-field/delete"
    SEAL_TAG_GET_LIST = "/seal/tag/get-list"
    DOC_TEMPLATE_CREATE = "/doc-template/create"
    DOC_TEMPLATE_COPY_CREATE = "/doc-template/copy-create"
    DOC_TEMPLATE_FILL_VALUES = "/doc-template/fill-values"

    # SignTaskClient 签署任务
    SIGN_TASK_CREATE = "/sign-task/create"
    SIGN_TASK_CREATE_WITH_TEMPLATE = "/sign-task/create-with-template"
    SIGN_TASK_DOC_ADD = "/sign-task/doc/add"
    SIGN_TASK_DOC_DELETE = "/sign-task/doc/delete"
    SIGN_TASK_FIELD_ADD = "/sign-task/field/add"
    SIGN_TASK_FIELD_DELETE = "/sign-task/field/delete"
    SIGN_TASK_FIELD_FILL_VALUES = "/sign-task/field/fill-values"
    SIGN_TASK_ATTACH_ADD = "/sign-task/attach/add"
    SIGN_TASK_ATTACH_DELETE = "/sign-task/attach/delete"
    SIGN_TASK_ACTOR_ADD = "/sign-task/actor/add"
    SIGN_TASK_ACTOR_DELETE = "/sign-task/actor/delete"
    SIGN_TASK_START = "/sign-task/start"
    SIGN_TASK_CANCEL = "/sign-task/cancel"
    SIGN_TASK_DOC_FINALIZE = "/sign-task/doc-finalize"
    SIGN_TASK_BLOCK = "/sign-task/block"
    SIGN_TASK_UNBLOCK = "/sign-task/unblock"
    SIGN_TASK_URGE = "/sign-task/urge"
    SIGN_TASK_GET_DETAIL = "/sign-task/app/get-detail"
    SIGN_TASK_OWNER_GET_LIST = "/sign-task/owner/get-list"
    SIGN_TASK_OWNER_GET_DOWNLOAD_URL = "/sign-task/owner/get-download-url"
    SIGN_TASK_ACTOR_GET_URL = "/sign-task/actor/get-url"
    SIGN_TASK_CATALOG_LIST = "/sign-task-catalog/list"
    SIGN_TASK_FIELD_LIST = "/sign-task/field/list"
    SIGN_TASK_ACTOR_LIST = "/sign-task/actor/list"
    SIGN_TASK_GET_APPROVAL_INFO = "/sign-task/get-approval-info"
    SIGN_TASK_GET_BATCH_SIGN_URL = "/sign-task/get-batch-sign-url"
    SIGN_TASK_GET_EDIT_URL = "/sign-task/get-edit-url"
    SIGN_TASK_GET_PREVIEW_URL = "/sign-task/get-preview-url"
    GET_SIGN_TASK_DOWNLOAD_EVIDENCE_REPORT_URL = "/sign-task/evidence-report/get-download-url"
    SIGN_TASK_DELETE = "/sign-task/delete"
    SIGN_TASK_FINISH = "/sign-task/finish"
    GET_SIGN_TASK_BUSINESS_TYPE_LIST = "/sign-task/business-type/get-list"
    GET_SIGN_TASK_FACE_PICTURE = "/sign-task/actor/get-face-picture"
    SIGN_TASK_ABOLISH = "/sign-task/abolish"
    GET_SIGN_TASK_OWNER_SLICING_TICKET_ID = "/sign-task/owner/get-slicing-ticket-id"
    GET_SIGN_TASK_OWNER_PIC_DOWNLOAD_URL = "/sign-task/owner/get-pic-download-url"
    GET_AUDIO_VIDEO_DOWNLOAD_URL = "/sign-task/actor/get-audio-video-download-url"
    SIGN_TASK_ACTOR_V3_GET_URL = "/sign-task/actor/v3/get-url"
    GET_COMPARE_RESULT_URL = "/ocr/edit/compare-result-data"
    SIGN_TASK_ACTOR_MODIFY = "/sign-task/actor/modify"
    SIGN_TASK_EXTENSION = "/sign-task/extension"
    SIGN_TASK_IGNORE = "/sign-task/ignore"
    SIGN_TASK_MESSAGE_REPORT_GET_DOWNLOAD_URL = "/sign-task/message-report/get-download-url"
    APPROVAL_FLOW_GET_LIST = "/approval-flow/get-list"
    APPROVAL_FLOW_GET_DETAIL = "/approval-flow/get-detail"
    SIGN_TASK_GET_PREFILL_URL = "/sign-task/get-prefill-url"

    # EUIClient  对EUI页面链接进行管理操作，如获取个人授权链接、构造新企业授权链接、获取计费链接、获取签署编辑链接等
    # EUIClient 获取应用级资源链接
    APP_PAGE_RESOURCE_GET_URL = '/app-page-resource/get-url'
    # EUIClient 获取用户级资源链接
    USER_PAGE_RESOURCE_GET_URL = '/user-page-resource/get-url'

    # EUIClient  获取个人授权链接
    USER_GET_AUTH_URL = '/user/get-auth-url'
    # EUIClient  获取企业授权链接
    CORP_GET_AUTH_URL = '/corp/get-auth-url'

    USER_GET_OCR_IDCARD = "/user/ocr/id-card"
    telecom_there_element_verify = "/user/telecom/three-element-verify"
    bank_four_element_verify = "/user/bank/four-element-verify"
    bank_two_element_verify = "/user/identity/two-element-verify"
    user_identity_bank_three_element_verify = "/user/identity/bank-three-element-verify"
    user_identity_idcard_three_element_verify = "/user/identity/idcard-three-element-verify"
    corp_identity_business_three_element_verify = "/corp/identity/business-three-element-verify"
    corp_identity_business_four_element_verify = "/corp/identity/business-four-element-verify"
    corp_identity_business_info_query = "/corp/identity/business-info-query"
    USER_VERIFY_FACE_RECOGNITION = "/user/verify/face-recognition"
    USER_VERIFY_FACE_STATUS_QUERY = "/user/verify/face-status-query"
    USER_OCR_BANKCARD = "/user/ocr/bankcard"
    USER_GET_OCR_BIZ_LICENSE = "/user/ocr/license"
    USER_GET_OCR_DRIVING_LICENSE = "/user/ocr/drivinglicense"
    USER_GET_OCR_VEHICLE_LICENSE = "/user/ocr/vehiclelicense"
    USER_GET_OCR_MAINLAND_PERMIT = "/user/ocr/mainland-permit"
    USER_VERIFY_BANKCARD_FOUR_ELEMENT_CREATE = "/user/verify/bankcard-four-element/create"
    USER_VERIFY_TELECOM_THREE_ELEMENT_CREATE = "/user/verify/telecom-three-element/create"
    USER_VERIFY_AUTH_CODE_CHECK = "/user/verify/auth-code/check"
    USER_VERIFY_AUTH_CODE_GET = "/user/verify/auth-code/get"
    USER_VERIFY_GET_DETAIL = "/user/verify/get-detail"


    # EUIClient  获取计费链接
    BILLING_GET_BILL_URL = '/billing/get-bill-url'

    # 审批
    APPROVAL_GET_URL = "/approval/get-url"
    APPROVAL_GET_LIST = "/approval/get-list"
    APPROVAL_GET_DETAIL = "/approval/get-detail"

    # 回调
    GET_CALL_BACK_LIST = "/callback/get-list"

    # ToolClient
    # 获取三要素校验
    USER_GET_THREE_ELEMENT_VERIFY_URL = "/user/three-element-verify/get-url"
    # 获取四要素校验
    USER_GET_FOUR_ELEMENT_VERIFY_URL = "/user/four-element-verify/get-url"
    # 获取要素校验身份证图片下载链接
    USER_GET_IDCARD_IMAGE_DOWNLOAD_URL = "/user/element-verify/get-idcard-image-download-url"

    # 单据
    voucher_task_create = "/voucher-sign-task/create"
    voucher_task_detail = "/voucher-sign-task/app/get-detail"
    voucher_task_list = "/voucher-sign-task/owner/get-list"
    voucher_task_download = "/voucher-sign-task/owner/get-download-url"
    voucher_task_cancel = "/voucher-sign-task/cancel"
    voucher_task_actor_get_url = "/voucher-sign-task/actor/get-url"
