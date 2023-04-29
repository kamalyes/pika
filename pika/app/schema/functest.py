# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  functest.py
@Time    :  2022/6/18 2:28 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  功能测试
"""

from app.schema.base import BaseBatchDelIdsSchema, BaseQuerySchema, BaseQueryTypeSchema
from pydantic import BaseModel


class FuncCaseGlobalSchema(BaseModel):
    class Config:
        orm_mode = True


class EditFuncCaseSchema(FuncCaseGlobalSchema):
    pass


class DelFuncCaseSchema(BaseBatchDelIdsSchema):
    pass


class QueryFuncCaseInSchema(BaseQuerySchema, BaseQueryTypeSchema, FuncCaseGlobalSchema):
    pass


class QueryFuncCaseOutSchema(BaseQuerySchema, FuncCaseGlobalSchema):
    pass
