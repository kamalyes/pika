# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  http.py
@Time    :  2022/6/18 2:28 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from pydantic import BaseModel, validator

from app.enums.RequestBodyEnum import ReqBodyTypeEnum
from app.exceptions.business.ParamsException import VariablesNullError


class HttpRequestSchema(BaseModel):
    method: str
    url: str
    body: str = None
    body_type: ReqBodyTypeEnum = ReqBodyTypeEnum.none
    headers: dict = {}

    # noinspection PyMethodParameters
    @validator('method', 'url')
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise VariablesNullError("不能为空")
        return v
