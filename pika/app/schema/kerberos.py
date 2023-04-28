# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  kerberos.py
@Time    :  2022/5/3 3:52 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import List, Optional

from fastapi import Body
from pydantic import BaseModel

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.schema.base import BaseBatchDelIdsSchema, BaseOnlyIdSchema, BaseQuerySchema, BaseQueryTypeSchema


class KerberosGlobalSchema(BaseOnlyIdSchema):
    question: Optional[str] = Body(
        None, title="密保问题", max_length=ByteSizeEnum.LENGTH_255)
    description: Optional[str] = Body(
        None, title="备注信息", max_length=ByteSizeEnum.LENGTH_255)


class EditKerberosItemSchema(BaseModel):
    security: List[KerberosGlobalSchema] = Body(..., title="密保信息")


class DelKerberosSchema(BaseBatchDelIdsSchema):
    pass


class QueryKerberosInSchema(BaseQuerySchema, BaseQueryTypeSchema, KerberosGlobalSchema):
    class Config:
        orm_mode = True


class QueryKerberosOutSchema(BaseQuerySchema, KerberosGlobalSchema):
    class Config:
        orm_mode = True
