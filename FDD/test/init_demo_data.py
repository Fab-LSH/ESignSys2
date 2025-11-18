from fasc_api.client.client import ApiClient


class InitDemoData():
    # ApiClient初始化
    api_client =  ApiClient('AppId值', 'AppSecret值',request_url='请求api地址')

    # 测试数据 ---------------------------------
    clientCorpId = "企业主体在应用中的唯一标识";
    openCorpId = "企业id";
    clientUserId = "个人主体在应用中的唯一标识";
    openUserId = "个人id";
    docTemplateId = "文档模板id";
    signTemplateId = "签署模板id";
    docFileId = "文档fileId";
    attachFileId = "附件fileId";
    signTaskId = "签署任务id";
