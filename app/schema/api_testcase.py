# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  api_testcase.py
@Time    :  2022/9/15 11:01
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import List, Optional
from fastapi import Body, UploadFile, File
from pydantic import BaseModel, validator
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.ConvertorEnum import CaseConvertorTypeEnum
from app.enums.ProtocolEnum import ProtocolTypeEnum
from app.schema.api_testcase_data import ApiTestCaseDataSchema
from app.schema.api_testcase_out_parameters import ApiTestCaseOutParametersSchema
from app.schema.base import BaseOnlyCaseIdSchema, BaseOnlyDirectoryIdSchema, BaseOnlyIdSchema, BaseOnlyProtocolSchema, PikaBaseModel
from app.schema.constructor import ConstructorSchema
from app.schema.request import RequestInfoSchema


class ListTestCaseSchema(BaseOnlyDirectoryIdSchema):
    name: str = Body("", title="name")


class DeleteTestCaseSchema(BaseModel):
    data: List[str]


class TestCaseSchema(BaseOnlyIdSchema, BaseOnlyDirectoryIdSchema, BaseOnlyProtocolSchema):
    priority: str = Body(None, title="用例优先级: P0-P3",
                         max_length=ByteSizeEnum.LENGTH_03)
    url: str = Body("", title="请求url", max_length=ByteSizeEnum.LENGTH_1W)
    name: str = Body("", title="名称", max_length=ByteSizeEnum.LENGTH_32)
    case_type: int = Body(0, title="0: 普通用例 1: 前置用例 2: 数据工厂")
    base_path: str = Body(None, title="请求base_path")
    tag: str = Body(None, title="用例标签", max_length=ByteSizeEnum.LENGTH_64)
    request_body: str = Body(None, title="请求body", max_length=ByteSizeEnum.LENGTH_1W)
    content_type: int = Body(
        0, title="请求类型, 0: none 1: json 2: form 3: x-form 4: binary 5: GraphQL")
    request_headers: str = Body(
        None, title="请求头,可为空", max_length=ByteSizeEnum.LENGTH_15W)
    request_method: str = Body(
        None, title="请求方式, 如果非http可为空", max_length=ByteSizeEnum.LENGTH_12)
    status: int = Body(0, title="用例状态: 1: 调试中 2: 暂时关闭 3: 正常运作")
    out_parameters: List[ApiTestCaseOutParametersSchema] = Body(
        [], title="用例出参")

    # noinspection PyMethodParameters
    @validator("priority", "status", "directory_id", "protocol", "url", "name")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)


class TestCaseAssertsSchema(BaseOnlyIdSchema, BaseOnlyCaseIdSchema):
    name: str
    assert_type: str
    expected: str
    actually: str

    # noinspection PyMethodParameters
    @validator("name", "assert_type", "expected", "actually")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)


class TestCaseInfoSchema(BaseModel):
    case: Optional[TestCaseSchema] = None
    asserts: List[TestCaseAssertsSchema] = []
    data: List[ApiTestCaseDataSchema] = []
    constructor: List[ConstructorSchema] = []
    out_parameters: List[ApiTestCaseOutParametersSchema] = []

    # noinspection PyMethodParameters
    @validator("case")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)


class TestCaseGeneratorSchema(BaseOnlyDirectoryIdSchema, BaseOnlyProtocolSchema):
    requests: List[RequestInfoSchema]
    name: str


class TestCaseImportSchema(BaseModel):
    import_type: CaseConvertorTypeEnum = Body(0, title="导入类型")
    file: UploadFile = File(None)
    api_docs_url: str = Body(None, title="在线接口文档地址")
    is_cover: int = Body(0, title="是否叠加")
