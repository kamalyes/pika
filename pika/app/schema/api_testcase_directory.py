# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  api_testcase_directory.py
@Time    :  2022/9/15 11:01
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import List

from app.schema.base import (
    BaseOnlyDirectoryIdSchema,
    BaseOnlyIdSchema,
    BaseOnlyParentIdSchema,
    BaseOnlyProjectIdSchema,
    PikaBaseModel,
)
from pydantic import validator


class ApiTestCaseDirectorySchema(BaseOnlyIdSchema, BaseOnlyProjectIdSchema, BaseOnlyParentIdSchema):
    name: str

    # noinspection PyMethodParameters
    @validator("name")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)


class MoveApiTestCaseSchema(BaseOnlyProjectIdSchema, BaseOnlyDirectoryIdSchema):
    id_list: List[str]

    # noinspection PyMethodParameters
    @validator("id_list")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)
