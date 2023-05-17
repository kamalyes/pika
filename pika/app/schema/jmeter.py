from typing import Optional
from fastapi import Body
from pydantic import BaseModel
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.schema.base import BaseOnlyDescSchema, BaseOnlyIdSchema, BaseOnlyNameSchema, BaseOnlyPointDateSchema


class JmeterBatchNoSchema(BaseModel):
    batch_no: Optional[str] = Body(None, title="用例批次编号", max_length=ByteSizeEnum.LENGTH_50)


class JmeterRunTypeSchema(BaseModel):
    run_type: Optional[int] = Body(0, title="构建类型")


class JmeterLatestBuildSchema(BaseModel):
    project: Optional[str] = Body(None, title="项目名称", max_length=ByteSizeEnum.LENGTH_50)
    env: Optional[str] = Body(None, title="环境", max_length=ByteSizeEnum.LENGTH_50)


class JmeterChartDataSchema(
    BaseOnlyIdSchema,
    BaseOnlyDescSchema,
    BaseOnlyNameSchema,
    BaseOnlyPointDateSchema,
    JmeterLatestBuildSchema,
    JmeterRunTypeSchema,
):
    ...


class JmeterSummarySchema(JmeterLatestBuildSchema, BaseOnlyPointDateSchema, JmeterBatchNoSchema):
    pass_rate: Optional[int] = Body(0, title="通过率")
    result: Optional[bool] = Body(0, title="测试结果")
