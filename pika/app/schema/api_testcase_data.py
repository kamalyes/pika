# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  api_testcase_data.py
@Time    :  2022/9/15 11:01
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import Optional
from pydantic import validator
from app.core.handler.jsonres import PikaJsonEncoder
from app.schema.base import BaseOnlyCaseIdSchema, BaseOnlyEnvIdSchema, BaseOnlyIdSchema, PikaBaseModel


class ApiTestCaseDataSchema(BaseOnlyIdSchema, BaseOnlyCaseIdSchema, BaseOnlyEnvIdSchema):
    name: Optional[str]
    json_data: Optional[str]

    # noinspection PyMethodParameters
    @validator("name")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)

    @validator("json_data")
    def assert_json_type(cls, v):
        return PikaJsonEncoder.safe_json_loads(v,err_detail='请检查数据是否为JSON格式')