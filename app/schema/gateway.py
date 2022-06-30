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

from app.excpetions.ParamsException import ParamsError
from app.schema.base import PikaBaseModel


class PikaGatewayForm(BaseModel):
    id: int = 0
    env_id: int = None
    name: str = ''
    address: str = ''

    @validator("env_id", 'name')
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)

    @validator('address', whole=True)
    def prefix_match(cls, v):
        if not v.startswith(("http://", "https://", "ws://", "wss://")):
            raise ParamsError("前缀不为http或ws")
        return v
