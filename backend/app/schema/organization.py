# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  organization.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import Optional

from fastapi import Body, Query
from pydantic import BaseModel

from app.enums.bytesize import ByteSizeEnum
from app.schema.base import PikaDeleteModel, PikaQueryModel, PikaLargeEditModel


class EditUserGroupModel(PikaLargeEditModel):
    group_id: int = Body(0, title="用户组id")
    group_name: Optional[str] = Body(..., title="用户组名称", min_length=2, max_length=ByteSizeEnum.LENGTH_255)

    class Config:
        orm_mode = True


class DelUserGroupModel(PikaDeleteModel):
    pass


class EditDeptModel(BaseModel):
    dept_id: int = Body(0, title="部门id")
    group_id: int = Body(..., title="用户组id")
    dept_name: Optional[str] = Body(..., title="部门名称", min_length=2, max_length=ByteSizeEnum.LENGTH_255)
    description: Optional[str] = Body(None, title="备注信息", max_length=ByteSizeEnum.LENGTH_255)
    is_enabled: int = Body(1, title="禁用/启用 1：启用、0：禁用")

    class Config:
        orm_mode = True


class DelDeptModel(PikaDeleteModel):
    pass


class EditDeptRelModel(BaseModel):
    rel_id: Optional[int] = Body(0, title="应用id")
    dept_id: int = Body(..., title="部门id")
    emp_no: Optional[str] = Body(..., title="员工编号", max_length=ByteSizeEnum.LENGTH_20)
    description: Optional[str] = Body(None, title="备注信息", max_length=ByteSizeEnum.LENGTH_255)
    create_emp_no: Optional[str] = Body(None, title="创建者员工编号", max_length=ByteSizeEnum.LENGTH_20)
    update_emp_no: Optional[str] = Body(None, title="修改者员工编号", max_length=ByteSizeEnum.LENGTH_20)

    class Config:
        orm_mode = True


class DelDeptRelModel(PikaDeleteModel):
    pass


class QueryDeptRelModel(PikaQueryModel):
    rel_id: int = Query(None, title="组织应用id")
    dept_id: int = Query(None, title="部门id")
    emp_no: Optional[str] = Query(None, title="员工编号", max_length=ByteSizeEnum.LENGTH_20)

    class Config:
        orm_mode = True
