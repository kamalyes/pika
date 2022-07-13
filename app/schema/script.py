# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  script
@Time    :  2022/6/18 7:06 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import Optional

from pydantic import BaseModel, validator

from app.schema.base import PikaBaseModel


class PyScriptSchema(BaseModel):
    command: Optional[str]
    value: Optional[str]

    # noinspection PyMethodParameters
    @validator("command")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)
