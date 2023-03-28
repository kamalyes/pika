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

from typing import Optional

from app.enums.RequestBodyEnum import ReqBodyTypeEnum
from app.schema.base import PikaBaseModel
from pydantic import BaseModel, validator


class HttpRequestSchema(BaseModel):
    method: Optional[str] = None
    url: Optional[str] = None
    request_body: Optional[str] = None
    content_type: ReqBodyTypeEnum = ReqBodyTypeEnum.none
    headers: dict = {}

    # noinspection PyMethodParameters
    @validator("method", "url")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)
