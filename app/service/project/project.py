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
from app.crud.project.project import ProjectDao, ProjectRoleDao
from app.crud.project.testplan import ApiTestPlanDao
from app.enums.RbacEnum import RoleEnum
from app.middleware.oss import OssClient
from app.models import async_db_session
from app.schema.project import ProjectEditSchema, ProjectSchema
from app.service import Permission

router = APIRouter()


@router.get("/list")
async def list_project(page: int = 1, size: int = 8, name: str = "",
                       escarole=Depends(Permission(escarole=True))):
    """
    获取项目列表
    Args:
        page:
        size:
        name:
        escarole:

    Returns:

    """
    operator_emp_no, operator_identity = escarole
    result, total = await ProjectDao.list_project(operator_emp_no, operator_identity, page, size, name)
    return PikaResponse.success_with_size(data=result, total=total)


@router.post("/insert")
async def insert_project(data: ProjectSchema, escarole=Depends(Permission(RoleEnum.MANAGER, True))):
    operator_emp_no, operator_identity = escarole
    await ProjectDao.add_project(operator_emp_no=operator_emp_no, **data.dict())
    return PikaResponse.success()


@router.post("/avatar/{project_id}", summary="上传项目头像")
async def update_project_avatar(project_id: int, file: UploadFile = File(...),
                                escarole=Depends(Permission(escarole=True))):
    try:
        operator_emp_no, operator_identity = escarole
        file_content = await file.read()
        suffix = file.filename.split(".")[-1]
        filepath = f"project_{project_id}.{suffix}"
        client = OssClient.get_oss_client()
        file_url, _ = await client.create_file(filepath, file_content, base_path="avatar")
        await ProjectDao.update_avatar(project_id, operator_emp_no, operator_identity, file_url)
        return PikaResponse.success(data=file_url)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/update")
async def update_project(data: ProjectEditSchema, escarole=Depends(Permission(escarole=True))):
    operator_emp_no, operator_identity = escarole
    await ProjectDao.update_project(operator_emp_no=operator_emp_no, operator_identity=operator_identity, **data.dict())
    return PikaResponse.success()


@router.get("/query")
async def query_project(project_id: int, escarole=Depends(Permission(escarole=True))):
    try:
        operator_emp_no, operator_identity = escarole
        result = dict()
        data, roles = await ProjectDao.query_project(project_id)
        await ProjectRoleDao.access(operator_emp_no, operator_identity, roles, data)
        result.update({"project": data, "roles": roles})
        return PikaResponse.success(data=result)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.delete("/delete", summary="删除项目")
async def query_project(project_id: int, escarole=Depends(Permission(RoleEnum.MANAGER, True)),
                        session=Depends(async_db_session)):
    operator_emp_no, operator_identity = escarole
    try:
        async with session.begin():
            # 事务开始
            owner = await ProjectDao.is_project_admin(session, project_id, operator_emp_no)
            if not owner and operator_identity != RoleEnum.ADMIN:
                return PikaResponse.forbidden()
            await ProjectDao.delete_record_by_id(session, operator_emp_no, project_id, session_begin=True)
            await ApiTestPlanDao.delete_record_by_id(session, operator_emp_no, project_id,
                                                     key="project_id",
                                                     exists=False, session_begin=True)
        return PikaResponse.success()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))
