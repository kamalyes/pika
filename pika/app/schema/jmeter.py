from typing import List, MutableSequence, Optional
from fastapi import Body
from pydantic import BaseModel
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.schema.base import BaseOnlyDescSchema, BaseOnlyIdSchema, BaseOnlyNameSchema, BaseOnlyPointTimeStampSchema


class JmeterBatchNoSchema(BaseModel):
    batch_no: Optional[str] = Body(None, title="用例批次编号", max_length=ByteSizeEnum.LENGTH_200)


class JmeterRunTypeSchema(BaseModel):
    os_type: Optional[int] = Body(0, title="os类型")


class JmeterLatestBuildSchema(BaseModel):
    project: Optional[str] = Body(None, title="项目名称", max_length=ByteSizeEnum.LENGTH_200)
    env: Optional[str] = Body(None, title="环境", max_length=ByteSizeEnum.LENGTH_200)


class JmeterSummarySchema(JmeterLatestBuildSchema, BaseOnlyPointTimeStampSchema, JmeterBatchNoSchema):
    pass_rate: Optional[str] = Body(None, title="通过率")
    duration: Optional[int] = Body(0, title="持续时间")
    failure: Optional[int] = Body(0, title="失败数")
    success: Optional[int] = Body(0, title="成功数")
    total: Optional[int] = Body(0, title="用例总数")
    result: Optional[int] = Body(0, title="测试结果")


class TestCaseInfoSchema(BaseOnlyPointTimeStampSchema):
    module_name: Optional[str] = Body(..., title="模块名称", max_length=ByteSizeEnum.LENGTH_200)
    case_name: Optional[str] = Body(..., title="用例名称", max_length=ByteSizeEnum.LENGTH_200)
    request_url: Optional[str] = Body(..., title="请求地址")
    request_method: Optional[str] = Body(..., title="请求方法", max_length=ByteSizeEnum.LENGTH_200)
    request_header: Optional[str] = Body(None, title="请求头")
    request_body: Optional[str] = Body(None, title="请求体")
    response_code: Optional[str] = Body(None, title="响状态码", max_length=ByteSizeEnum.LENGTH_200)
    response_header: Optional[str] = Body(None, title="响应头")
    response_body: Optional[str] = Body(None, title="响应体")
    test_result: Optional[bool] = Body(False, title="测试结果")
    fail_message: Optional[str] = Body(None, title="错误信息")


class JmeterUploadResultSchema(BaseModel):
    test_cases: List[TestCaseInfoSchema] = Body(None, title="Test Case Information")
    test_summary: JmeterSummarySchema = Body(None, title="Test Summary")


class JmeterChartDataSchema(
    BaseOnlyIdSchema,
    BaseOnlyDescSchema,
    BaseOnlyNameSchema,
    BaseOnlyPointTimeStampSchema,
    JmeterLatestBuildSchema,
    JmeterRunTypeSchema,
):
    ...
