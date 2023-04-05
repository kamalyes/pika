# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  api_testcase_out_parameters.py
@Time    :  2022/9/15 11:01
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import Optional
from fastapi import Body
from pydantic import BaseModel, validator
from app.enums.ByteSizeEnum import ByteSizeEnum

from app.schema.base import PikaBaseModel, BaseOnlyIdSchema


class ApiTestCaseOutParametersSchema(BaseOnlyIdSchema):
    name: Optional[str] = None
    expression: Optional[str] = None
    match_index: Optional[str] = None
    source: int = 0

    # noinspection PyMethodParameters
    @validator("name", "source")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)


class ApiTestCaseId(BaseModel):
    case_id: Optional[str] = Body(
        None, title="case_id", max_length=ByteSizeEnum.LENGTH_32)


class ApiTestCaseParametersSchema(ApiTestCaseOutParametersSchema, ApiTestCaseId):
  pass


class ApiTestCaseVariablesSchema(ApiTestCaseId):
    step_name: str
