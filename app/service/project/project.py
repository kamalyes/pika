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
from app.models import get_async_session
from app.schema.project import ProjectEditForm, ProjectForm
from app.service import Permission

router = APIRouter()


@router.get("/list")
async def list_project(page: int = 1, size: int = 8, name: str = "",
                       user_info=Depends(Permission())):
    """
    获取项目列表
    Args:
        page:
        size:
        name:
        user_info:

    Returns:

    """
    user_role, emp_no = user_info["identity"], user_info["emp_no"]
    result, total = await ProjectDao.list_project(emp_no, user_role, page, size, name)
    return PikaResponse.success_with_size(data=result, total=total)


@router.post("/insert")
async def insert_project(data: ProjectForm, user_info=Depends(Permission(RoleEnum.MANAGER))):
    operator = user_info["emp_no"]
    await ProjectDao.add_project(operator=operator, **data.dict())
    return PikaResponse.success()


@router.post("/avatar/{project_id}", summary="上传项目头像")
async def update_project_avatar(project_id: int, file: UploadFile = File(...),
                                user_info=Depends(Permission())):
    try:
        operator, identity = user_info["emp_no"], user_info["identity"]
        file_content = await file.read()
        suffix = file.filename.split(".")[-1]
        filepath = f"project_{project_id}.{suffix}"
        client = OssClient.get_oss_client()
        file_url, _ = await client.create_file(filepath, file_content, base_path="avatar")
        await ProjectDao.update_avatar(project_id, operator, identity, file_url)
        return PikaResponse.success(data=file_url)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/update")
async def update_project(data: ProjectEditForm, user_info=Depends(Permission())):
    operator, identity = user_info["emp_no"], user_info["identity"]
    await ProjectDao.update_project(update_emp_no=operator, identity=identity, **data.dict())
    return PikaResponse.success()


@router.get("/query")
async def query_project(project_id: int, user_info=Depends(Permission())):
    try:
        operator, identity = user_info["emp_no"], user_info["identity"]
        result = dict()
        data, roles = await ProjectDao.query_project(project_id)
        await ProjectRoleDao.access(operator, identity, roles, data)
        result.update({"project": data, "roles": roles})
        return PikaResponse.success(data=result)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.delete("/delete", summary="删除项目")
async def query_project(project_id: int, user_info=Depends(Permission(RoleEnum.MANAGER)),
                        session=Depends(get_async_session)):
    operator = user_info["emp_no"]
    try:
        async with session.begin():
            # 事务开始
            owner = await ProjectDao.is_project_admin(session, project_id, operator)
            if not owner and user_info["identity"] != RoleEnum.ADMIN:
                return PikaResponse.forbidden()
            await ProjectDao.delete_record_by_id(session, operator, project_id, session_begin=True)
            await ApiTestPlanDao.delete_record_by_id(session, operator, project_id,
                                                     key="project_id",
                                                     exists=False, session_begin=True)
        return PikaResponse.success()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))
