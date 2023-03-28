from typing import List

from fastapi import Body, UploadFile, File
from pydantic import BaseModel, validator

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.ConvertorEnum import CaseConvertorTypeEnum
from app.exceptions.business.ParamsException import VariablesNullError
from app.schema.api_testcase_data import ApiTestCaseDataSchema
from app.schema.api_testcase_out_parameters import ApiTestCaseOutParametersSchema
from app.schema.base import BaseOnlyIdSchema, PikaBaseModel
from app.schema.constructor import ConstructorSchema
from app.schema.request import RequestInfoSchema


class ListTestCaseSchema(BaseModel):
    directory_id: int = Body(None, title="directory_id")
    name: str = Body("", title="name")


class DeleteTestCaseSchema(BaseModel):
    data: List[int]


class TestCaseSchema(BaseOnlyIdSchema):
    priority: str = Body(None, title="用例优先级: p0-p3",
                         max_length=ByteSizeEnum.LENGTH_03)
    url: str = Body("", title="请求url", max_length=ByteSizeEnum.LENGTH_1W)
    name: str = Body("", title="名称", max_length=ByteSizeEnum.LENGTH_32)
    case_type: int = Body(0, title="0: 普通用例 1: 前置用例 2: 数据工厂")
    base_path: str = Body(None, title="请求base_path")
    tag: str = Body(None, title="用例标签", max_length=ByteSizeEnum.LENGTH_64)
    body: str = Body(None, title="请求body", max_length=ByteSizeEnum.LENGTH_1W)
    body_type: int = Body(
        0, title="请求类型, 0: none 1: json 2: form 3: x-form 4: binary 5: GraphQL")
    request_headers: str = Body(
        None, title="请求头，可为空", max_length=ByteSizeEnum.LENGTH_15W)
    request_method: str = Body(
        None, title="请求方式, 如果非http可为空", max_length=ByteSizeEnum.LENGTH_12)
    status: int = Body(0, title="用例状态: 1: 调试中 2: 暂时关闭 3: 正常运作")
    out_parameters: List[ApiTestCaseOutParametersSchema] = Body(
        [], title="用例出参")
    directory_id: int = Body(0, title="所属目录")
    request_type: int = Body(0, title="请求类型 1: http 2: grpc 3: dubbo")

    # noinspection PyMethodParameters
    @validator("priority", "status", "directory_id", "request_type", "url", "name")
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise VariablesNullError("不能为空")
        return v


class TestCaseAssertsSchema(BaseModel):
    id: int = None
    name: str
    case_id: int = None
    assert_type: str
    expected: str
    actually: str

    # noinspection PyMethodParameters
    @validator("name", "assert_type", "expected", "actually")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)


class TestCaseInfoSchema(BaseModel):
    case: TestCaseSchema = None
    asserts: List[TestCaseAssertsSchema] = []
    data: List[ApiTestCaseDataSchema] = []
    constructor: List[ConstructorSchema] = []
    out_parameters: List[ApiTestCaseOutParametersSchema] = []

    # noinspection PyMethodParameters
    @validator("case")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)


class TestCaseGeneratorSchema(BaseModel):
    directory_id: int
    requests: List[RequestInfoSchema]
    name: str


class TestCaseImportSchema(BaseModel):
    import_type: CaseConvertorTypeEnum = Body(0, title="导入类型")
    file: UploadFile = File(None)
    api_docs_url: str = Body(None, title="在线接口文档地址")
    is_cover: int = Body(0, title="是否叠加")
