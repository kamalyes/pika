from typing import List, MutableSequence, Optional
from fastapi import Body
from pydantic import BaseModel
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.schema.base import (
    BaseOnlyDescSchema,
    BaseOnlyIdSchema,
    BaseOnlyNameSchema,
    BaseOnlyPointTimeStampSchema,
    BaseOnlyPagingSchema,
)


class JmeterBatchNoSchema(BaseModel):
    batch_no: Optional[str] = Body(None, title="用例批次编号", max_length=ByteSizeEnum.LENGTH_200)


class JmeterCaseDetailSchema(BaseOnlyIdSchema, BaseOnlyPagingSchema): ...


class JmeterRunTypeSchema(BaseModel):
    os_type: Optional[int] = Body(0, title="os类型")


class JmeterLatestBuildSchema(BaseModel):
    project: Optional[str] = Body(None, title="项目名称", max_length=ByteSizeEnum.LENGTH_200)
    env: Optional[str] = Body(None, title="环境", max_length=ByteSizeEnum.LENGTH_200)


class JmeterSummarySchema(
    JmeterRunTypeSchema,
    JmeterLatestBuildSchema,
    BaseOnlyPointTimeStampSchema,
    JmeterBatchNoSchema,
):
    pass_rate: Optional[str] = Body(None, title="通过率")
    duration: Optional[int] = Body(0, title="持续时间")
    failure: Optional[int] = Body(0, title="失败数")
    success: Optional[int] = Body(0, title="成功数")
    total: Optional[int] = Body(0, title="用例总数")
    result: Optional[int] = Body(0, title="测试结果")


class JmeterSummaryListSchema(BaseOnlyPagingSchema, JmeterSummarySchema): ...


class TestCaseInfoSchema(BaseOnlyPointTimeStampSchema):
    module_name: Optional[str] = Body(..., title="模块名称", max_length=ByteSizeEnum.LENGTH_200)
    case_name: Optional[str] = Body(..., title="用例名称", max_length=ByteSizeEnum.LENGTH_200)
    request_url: Optional[str] = Body(..., title="请求地址")
    request_method: Optional[str] = Body(..., title="请求方法", max_length=ByteSizeEnum.LENGTH_200)
    request_header: Optional[str] = Body(None, title="请求头")
    request_query: Optional[str] = Body(None, title="请求体(Query、一般是get请求)")
    request_body: Optional[str] = Body(None, title="请求体(Body、一般是post请求)")
    response_code: Optional[str] = Body(None, title="响状态码", max_length=ByteSizeEnum.LENGTH_200)
    response_time: Optional[int] = Body(0, title="响应时间")
    response_size: Optional[int] = Body(0, title="响应包体大小")
    response_header: Optional[str] = Body(None, title="响应头")
    response_body: Optional[str] = Body(None, title="响应体")
    fail_message: Optional[str] = Body(None, title="错误信息")
    cookies: Optional[str] = Body(None, title="cookies")
    body_size: Optional[int] = Body(0, title="请求数据大小")
    request_size: Optional[int] = Body(0, title="请求数据大小")
    headers_size: Optional[int] = Body(0, title="headers大小")
    error_count: Optional[int] = Body(0, title="失败数量")
    successful: Optional[bool] = Body(False, title="是否通过、成功（符合预期断言）")
    connect_time: Optional[int] = Body(0, title="连接时间")
    latency: Optional[int] = Body(0, title="延迟")
    group_threads: Optional[int] = Body(0, title="线程组数")
    all_threads: Optional[int] = Body(0, title="所有线程数")
    data_encoding: Optional[str] = Body(None, title="数据编码类型")
    ignore: Optional[bool] = Body(False, title="是否忽略")
    total_assertions: Optional[int] = Body(0, title="断言点总数")
    pass_assertions: Optional[int] = Body(0, title="断言成功数量")
    assertions: Optional[list] = Body([], title="断言详情")


class JmeterUploadResultSchema(BaseModel):
    test_cases: List[TestCaseInfoSchema] = Body(None, title="Test Case Information")
    test_summary: JmeterSummarySchema = Body(None, title="Test Summary")


class JmeterChartDataSchema(
    BaseOnlyIdSchema,
    BaseOnlyDescSchema,
    BaseOnlyNameSchema,
    BaseOnlyPointTimeStampSchema,
    JmeterLatestBuildSchema,
):
    chart_type: Optional[int] = Body(0, title="chart类型")
