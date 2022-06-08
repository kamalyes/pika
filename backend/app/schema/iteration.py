# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  iteration.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from typing import Optional

from fastapi import Query, Body
from pydantic import BaseModel

from app.enums.bytesize import ByteSizeEnum
from app.schema.base import PikaDeleteModel, PikaQueryModel


class EditIterateModel(BaseModel):
    iterate_id: Optional[int] = Body(0, title="迭代id")
    project_id: Optional[int] = Body(..., title="项目id")
    name: Optional[str] = Body(..., title="名称", max_length=ByteSizeEnum.LENGTH_30)
    description: Optional[str] = Body(None, title="描述", max_length=ByteSizeEnum.LENGTH_255)
    is_private: Optional[int] = Body(0, title="是否私有 1：私有 0：公开")
    is_enabled: Optional[int] = Body(1, title="禁用/启用 1：启用、0：禁用")

    class Config:
        orm_mode = True


class DelIterateModel(PikaDeleteModel):
    pass


class QueryIterateModel(PikaQueryModel):
    id: Optional[int] = Query(None, title="迭代id")
    name: Optional[str] = Query(None, title="迭代名称", max_length=ByteSizeEnum.LENGTH_30)
    is_private: Optional[int] = Query(0, title="是否私有 1：私有 0：公开")
    is_enabled: Optional[int] = Query(None, title="禁用/启用 1：启用、0：禁用")

    class Config:
        orm_mode = True


class EditUserIterateRelModel(BaseModel):
    iterate_rel_id: Optional[int] = Body(None, title="迭代关联id")
    iterate_id: Optional[int] = Body(None, title="迭代id")
    emp_no: Optional[int] = Body(None, title="员工编号")
    description: Optional[str] = Body(None, title="描述", max_length=ByteSizeEnum.LENGTH_255)

    class Config:
        orm_mode = True


class DelUserIterateRelModel(PikaDeleteModel):
    pass
