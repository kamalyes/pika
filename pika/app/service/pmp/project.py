# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  project.py
@Time    :  2022/6/18 2:27 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from fastapi import APIRouter, Depends, File, UploadFile

from app.core.handler.jsonres import PikaResponse
from app.crud.pmp.project import ProjectDao, ProjectRoleDao
from app.crud.pmp.testplan import ApiTestPlanDao
from app.enums.RbacEnum import RoleEnum
from app.middleware.oss import OssClient
from app.models import async_db_session_iterator
from app.schema.base import BaseOnlyPagingSchema
from app.schema.project import ProjectEditSchema, ProjectSchema
from app.service import Permission
from app.models.project import ProjectRoleModel
from app.schema.project import ProjectDelSchema, ProjectRoleEditSchema, ProjectRoleSchema

router = APIRouter()


@router.post("/insert", summary="增加项目")
async def insert_project(data: ProjectSchema, escarole=Depends(Permission(RoleEnum.MANAGER, True))):
    operator, operator_identity = escarole
    await ProjectDao.add_project(operator=operator, **data.dict())
    return PikaResponse.success()


@router.delete("/delete", summary="删除项目")
async def delete_project(
    project_id: str,
    escarole=Depends(Permission(RoleEnum.MANAGER, True)),
    session=Depends(async_db_session_iterator),
):
    operator, operator_identity = escarole
    try:
        async with session.begin():
            # 事务开始
            owner = await ProjectDao.is_project_admin(session, project_id, operator)
            if not owner and operator_identity != RoleEnum.ADMIN:
                return PikaResponse.forbidden()
            await ProjectDao.delete_record_by_id(session, operator, project_id, session_begin=True)
            await ApiTestPlanDao.delete_record_by_id(
                session=session,
                operator=operator,
                project_id=project_id,
                key=project_id,
                session_begin=True,
            )
        return PikaResponse.success()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/update", summary="更新项目")
async def update_project(data: ProjectEditSchema, escarole=Depends(Permission(escarole=True))):
    operator, operator_identity = escarole
    await ProjectDao.update_project(operator=operator, operator_identity=operator_identity, **data.dict())
    return PikaResponse.success()


@router.get("/query", summary="查询项目")
async def query_project(project_id: str, escarole=Depends(Permission(escarole=True))):
    try:
        operator, operator_identity = escarole
        result = {}
        data, roles = await ProjectDao.query_project(project_id)
        await ProjectRoleDao.access(operator, operator_identity, roles, data)
        result.update({"project": data, "roles": roles})
        return PikaResponse.success(data=result)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.get("/list", summary="查询/获取项目列表")
async def list_project(
    paging: BaseOnlyPagingSchema = Depends(),
    name: str = None,
    escarole=Depends(Permission(escarole=True)),
):
    operator, operator_identity = escarole
    result, total = await ProjectDao.list_project(operator, operator_identity, paging, name)
    return PikaResponse.success_with_size(data=result, total=total)


@router.post("/avatar/{project_id}", summary="上传项目头像")
async def update_project_avatar(
    project_id: str,
    file: UploadFile = File(...),
    escarole=Depends(Permission(escarole=True)),
):
    try:
        operator, operator_identity = escarole
        file_content = await file.read()
        suffix = file.filename.split(".")[-1]
        filepath = f"project_{project_id}.{suffix}"
        client = OssClient.get_oss_client()
        file_url, _ = await client.upload_file(filepath, file_content, base_path="avatar")
        await ProjectDao.update_avatar(project_id, operator, operator_identity, file_url)
        return PikaResponse.success(data=file_url)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/role/insert", summary="添加项目成员")
async def insert_project_role(role: ProjectRoleSchema, escarole=Depends(Permission(escarole=True))):
    try:
        operator, operator_identity = escarole
        query = await ProjectRoleDao.query_record(member_no=role.member_no, project_id=role.project_id)
        if query is not None:
            raise Exception("该用户已存在")
        await ProjectRoleDao.has_permission(
            project_id=role.project_id,
            project_role=role.project_role,
            operator=operator,
            operator_identity=operator_identity,
        )
        model = ProjectRoleModel(**role.dict(), operator=operator)
        await ProjectRoleDao.insert(model=model, log=True)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))
    return PikaResponse.success()


@router.post("/role/update", summary="更新项目成员")
async def update_project_role(prole: ProjectRoleEditSchema, escarole=Depends(Permission(escarole=True))):
    operator, operator_identity = escarole
    await ProjectRoleDao.update_project_role(prole, operator, operator_identity)
    return PikaResponse.success()


@router.post("/role/delete", summary="删除项目成员")
async def delete_project_role(prole: ProjectDelSchema, escarole=Depends(Permission(escarole=True))):
    operator, operator_identity = escarole
    await ProjectRoleDao.delete_project_role(prole.id, operator, operator_identity)
    return PikaResponse.success()
