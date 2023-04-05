# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  database.py
@Time    :  2022/6/18 7:18 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import Optional

from pydantic import BaseModel, validator

from app.schema.base import PikaBaseModel, BaseOnlyIdSchema


class DatabaseSchema(BaseOnlyIdSchema):
    name: Optional[str]
    host: Optional[str]
    port: Optional[int] = None
    username: Optional[str]
    password: Optional[str]
    database: Optional[str]
    sql_type: int
    env: str

    # noinspection PyMethodParameters
    @validator("name", "host", "port", "username", "password", "sql_type", "env")
    def data_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)
