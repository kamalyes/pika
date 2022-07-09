# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  online.py
@Time    :  2022/6/18 2:28 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import Optional

from pydantic import BaseModel, validator

from app.schema.base import PikaBaseModel


class OnlineSQLForm(BaseModel):
    id: Optional[int] = None
    sql: Optional[str]

    # noinspection PyMethodParameters
    @validator("sql", 'id')
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)


class OnlineRedisForm(BaseModel):
    id: Optional[int] = None
    command: Optional[str]

    # noinspection PyMethodParameters
    @validator('id', 'command')
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)
