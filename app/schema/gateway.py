# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  gateway.py
@Time    :  2022/6/18 2:28 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from pydantic import validator, BaseModel

from app.excpetions.business.ParamsException import VariablesNullError
from app.schema.base import PikaBaseModel


class PikaGatewaySchema(BaseModel):
    id: int = 0
    env: int = None
    name: str = ''
    gateway: str = ''

    # noinspection PyMethodParameters
    @validator("env", 'name')
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)

    # noinspection PyMethodParameters
    @validator('gateway', whole=True)
    def prefix_match(cls, v):
        if not v.startswith(("http://", "https://", "ws://", "wss://")):
            raise VariablesNullError("前缀不为http或ws")
        return v
