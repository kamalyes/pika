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
from fastapi import Depends, APIRouter

from app.core.handler.jsonres import PikaResponse
from app.crud.project.project import ProjectRoleDao
from app.models.project import ProjectRoleModel
from app.schema.project import ProjectRoleSchema, ProjectRoleEditSchema, ProjectDelSchema
from app.service import Permission

router = APIRouter()


@router.post("/role/insert", summary="添加项目成员")
async def insert_project_role(role: ProjectRoleSchema, escarole=Depends(Permission(escarole=True))):
    try:
        operator, operator_identity = escarole
        query = await ProjectRoleDao.query_record(emp_no=role.emp_no, project_id=role.project_id)
        if query is not None:
            raise Exception("该用户已存在")
        await ProjectRoleDao.has_permission(project_id=role.project_id,
                                            project_role=role.project_role,
                                            operator=operator,
                                            operator_identity=operator_identity)
        model = ProjectRoleModel(**role.dict(), operator=operator)
        await ProjectRoleDao.insert(model=model, log=True)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))
    return PikaResponse.success()


@router.post("/role/update", summary="更新项目成员")
async def update_project_role(prole: ProjectRoleEditSchema,
                              escarole=Depends(Permission(escarole=True))):
    operator, operator_identity = escarole
    await ProjectRoleDao.update_project_role(prole, operator, operator_identity)
    return PikaResponse.success()


@router.post("/role/delete", summary="删除项目成员")
async def delete_project_role(prole: ProjectDelSchema, escarole=Depends(Permission(escarole=True))):
    operator, operator_identity = escarole
    await ProjectRoleDao.delete_project_role(prole.id, operator, operator_identity)
    return PikaResponse.success()
