# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  lexicon.py
@Time    :  2022/6/7 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import Optional

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.schema.base import BaseBatchDelIdsSchema, BaseLargeEditSchema, BaseQuerySchema, BaseQueryTypeSchema
from fastapi import Body


# 敏感词
class SensitiveWordGlobalSchema(BaseLargeEditSchema):
    name: Optional[str] = Body(..., max_length=ByteSizeEnum.LENGTH_64, title="名词")
    genre: Optional[int] = Body(0, title="类型")

    class Config:
        orm_mode = True


class DelSensitiveWordSchema(BaseBatchDelIdsSchema):
    pass


class QuerySensitiveWordInSchema(BaseQuerySchema, BaseQueryTypeSchema, SensitiveWordGlobalSchema):
    pass


class QuerySensitiveWordOutSchema(BaseQuerySchema, SensitiveWordGlobalSchema):
    pass


# 化名
class AliasGlobalSchema(BaseLargeEditSchema):
    pass


class EditAliasWordSchema(AliasGlobalSchema):
    pass


class DelAliasWordSchema(BaseBatchDelIdsSchema):
    pass


class QueryAliasWordInSchema(BaseQuerySchema, BaseQueryTypeSchema, AliasGlobalSchema):
    pass


class QueryAliasWordOutSchema(BaseQuerySchema, AliasGlobalSchema):
    pass
