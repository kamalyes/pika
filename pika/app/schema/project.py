# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  project.py
@Time    :  2023/3/30 2:28 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.schema.base import BaseOnlyIdSchema, BaseOnlyProjectIdSchema
from fastapi import Body
from pydantic import BaseModel


class ProjectSchema(BaseModel):
    name: str = Body(..., name="项目名称", max_length=ByteSizeEnum.LENGTH_16)
    app: str = Body(..., name="项目名称", max_length=ByteSizeEnum.LENGTH_32)
    owner: str = Body(..., name="项目名称", max_length=ByteSizeEnum.LENGTH_16)
    private: bool = Body(False, name="项目名称")
    description: str = Body(None, name="项目名称", max_length=ByteSizeEnum.LENGTH_600)
    dingtalk_url: str = Body(None, name="项目名称", max_length=ByteSizeEnum.LENGTH_128)
    qy_wx_url: str = Body(None, name="项目名称", max_length=ByteSizeEnum.LENGTH_128)


class ProjectEditSchema(ProjectSchema, BaseOnlyIdSchema):
    pass


class ProjectDelSchema(BaseOnlyIdSchema):
    pass


class ProjectRoleSchema(BaseOnlyProjectIdSchema):
    member_no: str = Body(..., name="项目成员(emp_no)", max_length=ByteSizeEnum.LENGTH_32)
    project_role: int = Body(..., name="项目角色")


class ProjectRoleEditSchema(ProjectRoleSchema, BaseOnlyIdSchema):
    pass
