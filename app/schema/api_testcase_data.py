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
from pydantic import BaseModel, validator
from fastapi import Body
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.schema.base import BaseOnlyCaseIdSchema, BaseOnlyIdSchema, PikaBaseModel


class ApiTestCaseDataSchema(BaseOnlyIdSchema, BaseOnlyCaseIdSchema):
    name: str
    json_data: str
    env: str

    # noinspection PyMethodParameters
    @validator("env", "name", "json_data")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)
