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
from fastapi import Body
from app.schema.base import BaseOnlyCaseIdSchema, BaseOnlyEnvIdSchema, BaseOnlyIdSchema, PikaBaseModel


class ApiTestCaseDataSchema(BaseOnlyIdSchema, BaseOnlyCaseIdSchema, BaseOnlyEnvIdSchema):
    name: Optional[str]
    json_data: Optional[str]

    # noinspection PyMethodParameters
    @validator("name", "json_data")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)
