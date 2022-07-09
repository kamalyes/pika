# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  project_role
@Time    :  2022/7/9 2:55 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from fastapi import Depends

from app.core.handler.jsonres import PikaResponse
from app.crud.project.project import ProjectRoleDao
from app.models.project import ProjectRoleModel
from app.schema.project import ProjectRoleModelForm, ProjectRoleModelEditForm, ProjectDelForm
from app.service import Permission
from app.service.project.project import router


@router.post("/role/insert")
async def insert_project_role(role: ProjectRoleModelForm, user_info=Depends(Permission())):
    try:
        operator, identity = user_info["emp_no"], user_info["identity"]
        query = await ProjectRoleDao.query_record(emp_no=role.emp_no, project_id=role.project_id)
        if query is not None:
            raise Exception("该用户已存在")
        await ProjectRoleDao.has_permission(role.project_id, role.project_role, operator, user_info)
        model = ProjectRoleModel(**role.dict(), operator=operator)
        await ProjectRoleDao.insert_record(model, True)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))
    return PikaResponse.success()


@router.post("/role/update")
async def update_project_role(role: ProjectRoleModelEditForm, user_info=Depends(Permission())):
    operator, identity = user_info["emp_no"], user_info["identity"]
    await ProjectRoleDao.update_project_role(role, operator, identity)
    return PikaResponse.success()


@router.post("/role/delete")
async def delete_project_role(role: ProjectDelForm, user_info=Depends(Permission())):
    operator, identity = user_info["emp_no"], user_info["identity"]
    await ProjectRoleDao.delete_project_role(role.id, operator, identity)
    return PikaResponse.success()
