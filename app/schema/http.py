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

from app.excpetions.business.ParamsException import VariablesNullError


class HttpRequestForm(BaseModel):
    method: str
    url: str
    body: str = None
    body_type: int = 0
    headers: dict = {}

    # noinspection PyMethodParameters
    @validator('method', 'url')
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise VariablesNullError("不能为空")
        return v
