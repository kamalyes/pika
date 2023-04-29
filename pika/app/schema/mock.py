# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  mock.py
@Time    :  2022/6/18 2:19 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import Optional

from app.schema.base import (
    BaseBatchDelIdsSchema,
    BaseLargeEditSchema,
    BaseOnlyProjectIdSchema,
    BaseQuerySchema,
    BaseQueryTypeSchema,
)
from fastapi import Body


class MockGlobalSchema(BaseLargeEditSchema, BaseOnlyProjectIdSchema):
    url: Optional[str] = Body(None, title="url")
    method: Optional[str] = Body("GET", title="请求方式")
    headers: Optional[str] = Body(None, title="headers")
    match_type: Optional[str] = Body("0", title="类型:0:default,1:mockjs,2:faker")
    content_type: Optional[str] = Body(None, title="content_type")
    response_templates: Optional[str] = Body(..., title="响应模版")
    status_code: Optional[str] = Body("200", title="http 响应状态码:200(默认)")


class EditMockSchema(MockGlobalSchema):
    pass


class DelMockSchema(BaseBatchDelIdsSchema):
    pass


class QueryMockInSchema(BaseQuerySchema, BaseQueryTypeSchema, MockGlobalSchema):
    pass


class QueryMockOutSchema(BaseQuerySchema):
    pass
