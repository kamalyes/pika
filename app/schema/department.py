# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  department.py
@Time    :  2022/9/15 11:01
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import Optional

from fastapi import Body

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.schema.base import BaseIPdSchema, BaseQuerySchema


class DepartmentFormSchema(BaseIPdSchema):
    sort_id: Optional[int] = Body(0, title="排序id")
    organization_id: Optional[int] = Body(..., title="组织id", gt=0)
    name: Optional[str] = Body(..., title="部门名称", min_length=2,
                               max_length=ByteSizeEnum.LENGTH_255)


class QueryDepartmentInSchema(DepartmentFormSchema, BaseQuerySchema):
    pass
