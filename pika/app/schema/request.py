# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  request.py
@Time    :  2022/6/18 2:19 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  translate mitmproxy request and response data
"""
from typing import Optional, TypeVar

from app.core.handler.jsonres import PikaJsonEncoder
from app.enums.ByteSizeEnum import ByteSizeEnum
from fastapi import Body
from loguru import logger
from pydantic import BaseModel

request_body = TypeVar("request_body", bytes, str)


class RequestInfoSchema(BaseModel, PikaJsonEncoder):
    url: Optional[str] = Body(None, name="url", max_length=ByteSizeEnum.LENGTH_256)
    request_body: Optional[str] = Body(None, name="request_body", max_length=ByteSizeEnum.LENGTH_2W)
    request_method: Optional[str] = Body(None, name="请求方式", max_length=ByteSizeEnum.LENGTH_12)
    request_headers: Optional[dict] = Body(None, name="请求头部信息")
    response_headers: Optional[dict] = Body(None, name="响应头部信息")
    cookies: Optional[dict] = Body(None, name="响应Cookies")
    request_cookies: Optional[dict] = Body(None, name="请求Cookies")
    response_content: Optional[str] = Body(None, name="响应Content")
    status_code: Optional[int] = Body(None, name="状态码")

    def __init__(self, flow=None, **kwargs):
        if flow:
            kwargs.update(
                {
                    "status_code": flow.response.status_code,
                    "url": flow.request.url,
                    "request_method": flow.request.method,
                    "request_headers": dict(flow.request.headers),
                    "response_headers": dict(flow.response.headers),
                    "response_content": self.get_response(flow.response),
                    "request_body": self.get_body(flow.request),
                    "cookies": dict(flow.response.cookies),
                    "request_cookies": dict(flow.request.cookies),
                },
            )
        super().__init__(**kwargs)

    def from_dict(self, **kwargs):
        for k, v in kwargs:
            if not hasattr(self, k):
                raise Exception(f"set RequestInfoSchema error, no field: {k}")
            setattr(self, k, v)

    @classmethod
    def translate_json(cls, text):
        try:
            return cls.safe_json_dumps(cls.safe_json_loads(text), indent=4, ensure_ascii=False)
        except Exception as e:
            logger.bind(name=None).warning(f"解析json格式请求失败: {e}")
            return text

    @classmethod
    def get_response(cls, response):
        content_type = response.headers.get("Content-Type")
        if "json" in content_type.lower():
            return cls.translate_json(response.text)
        if "text" in content_type.lower() or "xml" in content_type.lower():
            return response.text
        return response.data.decode("utf-8")

    @classmethod
    def get_body(cls, request):
        if len(request.content) == 0:
            return ""
        content_type = request.headers.get("Content-Type")
        if "json" in content_type.lower():
            return cls.translate_json(request.text)
        if "text" in content_type.lower() or "xml" in content_type.lower():
            return request.text
        return request.data.decode("utf-8")

    @classmethod
    def dumps(cls):
        return cls.safe_json_dumps(cls.dict(), ensure_ascii=False)
