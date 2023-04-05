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
from typing import List, Optional
from fastapi import Body
from pydantic import BaseModel, validator
from app.enums.ByteSizeEnum import ByteSizeEnum

from app.schema.base import BaseOnlyDirectoryIdSchema, BaseOnlyIdSchema, BaseOnlyProjectIdSchema, PikaBaseModel


class ApiTestCaseDirectorySchema(BaseOnlyIdSchema, BaseOnlyProjectIdSchema):
    name: str
    parent: Optional[str] = Body(
        None, title="parent", max_length=ByteSizeEnum.LENGTH_32)

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
