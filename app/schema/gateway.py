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
from typing import Optional
from pydantic import validator
from app.exceptions.business.ParamsException import VariablesNullError
from app.schema.base import BaseOnlyEnvIdSchema, BaseOnlyIdSchema, PikaBaseModel


class PikaGatewaySchema(BaseOnlyIdSchema, BaseOnlyEnvIdSchema):
    name: Optional[str] = None
    address: Optional[str] = None

    # noinspection PyMethodParameters
    @validator('name')
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)

    # noinspection PyMethodParameters
    @validator('address', whole=True)
    def prefix_match(cls, v):
        if not v.startswith(("http://", "https://", "ws://", "wss://")):
            raise VariablesNullError("前缀不为http或ws")
        return v
