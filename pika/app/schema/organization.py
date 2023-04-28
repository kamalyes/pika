# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  organization.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import Optional

from fastapi import Body

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.schema.base import BaseIPdSchema, BaseQuerySchema, BaseQueryTypeSchema


class OrganizationFormSchema(BaseIPdSchema):
    sort_id: Optional[int] = Body(0, title="排序id")
    name: Optional[str] = Body(None, title="用户组名称", max_length=ByteSizeEnum.LENGTH_255)


class QueryOrganizationSchema(BaseQuerySchema, OrganizationFormSchema):
  pass


class QueryOrganizationInSchema(QueryOrganizationSchema, BaseQueryTypeSchema):
    pass


class QueryOrganizationOutSchema(QueryOrganizationSchema):
    class Config:
        orm_mode = True
