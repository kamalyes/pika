# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  iteration.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from typing import Optional
from fastapi import Query, Body
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.schema.base import BaseBatchDelIdsSchema, BaseOnlyEmpNoSchema, BaseOnlyIdSchema, BaseOnlyIterateIdSchema, BasePPdSchema, BaseQuerySchema


class EditIterateSchema(BasePPdSchema):
    name: Optional[str] = Body(..., title="名称", max_length=ByteSizeEnum.LENGTH_30)
    description: Optional[str] = Body(None, title="描述", max_length=ByteSizeEnum.LENGTH_255)
    is_private: Optional[int] = Body(0, title="是否私有 1:私有 0:公开")
    enabled_flag: Optional[int] = Body(1, title="启用标识 1:启用、0:禁用")

    class Config:
        orm_mode = True


class DelIterateSchema(BaseBatchDelIdsSchema):
    pass


class QueryIterateSchema(BaseQuerySchema):
    name: Optional[str] = Query(None, title="迭代名称", max_length=ByteSizeEnum.LENGTH_30)
    is_private: Optional[int] = Query(0, title="是否私有 1:私有 0:公开")
    enabled_flag: Optional[int] = Query(None, title="禁用/启用 1:启用、0:禁用")

    class Config:
        orm_mode = True


class EditUserIterateRelSchema(BaseOnlyIterateIdSchema, BaseOnlyEmpNoSchema):
    iterate_rel_id: Optional[int] = Body(None, title="迭代关联id")
    description: Optional[str] = Body(None, title="描述", max_length=ByteSizeEnum.LENGTH_255)

    class Config:
        orm_mode = True


class DelUserIterateRelSchema(BaseBatchDelIdsSchema):
    pass
