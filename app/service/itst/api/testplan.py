# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  testplan.py
@Time    :  2022/6/18 2:27 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import asyncio

from apscheduler.jobstores.base import JobLookupError
from fastapi import Depends, APIRouter

from app.core.handler.executor import Executor
from app.core.handler.jsonres import PikaResponse
from app.crud.project.testplan import ApiTestPlanDao
from app.enums.RbacEnum import RoleEnum
from app.models import async_db_session
from app.schema.api_testplan import ApiTestPlanSchema
from app.service import Permission
from app.utils.scheduler import Scheduler

router = APIRouter()


@router.get("/list", summary="测试计划列表查询")
async def list_test_plan(page: int, size: int, project_id: int = None, name: str = "",
                         priority: str = '',
                         operator: str = None, follow: bool = None,
                         escarole=Depends(Permission(escarole=True))):
    try:
        operator_emp_no, operator_identity = escarole
        data, total = await ApiTestPlanDao.list_test_plan(page, size, project_id=project_id,
                                                          name=name,
                                                          follow=follow, priority=priority,
                                                          operator_identity=operator_identity,
                                                          operator=operator,
                                                          operator_emp_no=operator_emp_no)

        ans = Scheduler.list_test_plan(data)
        return PikaResponse.success_with_size(data=ans, total=total)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/insert", summary="添加定时任务&测试计划")
async def insert_test_plan(form: ApiTestPlanSchema, user_info=Depends(Permission(RoleEnum.MANAGER))):
    try:
        plan = await ApiTestPlanDao.insert_test_plan(form, user_info['emp_no'])
        # 添加定时任务
        Scheduler.add_test_plan(plan.id, plan.name, plan.cron)
        return PikaResponse.success()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/update", summary="更新定时任务&测试计划")
async def update_test_plan(form: ApiTestPlanSchema, user_info=Depends(Permission(RoleEnum.MANAGER))):
    try:
        await ApiTestPlanDao.update_test_plan(form, user_info['emp_no'], True)
        Scheduler.edit_test_plan(form.id, form.name, form.cron)
        return PikaResponse.success()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.get("/delete", summary="删除定时任务&测试计划")
async def delete_test_plan(id: int, user_info=Depends(Permission(RoleEnum.MANAGER)),
                           session=Depends(async_db_session)):
    try:
        await ApiTestPlanDao.delete_record_by_id(session, user_info['emp_no'], id)
        Scheduler.remove(id)
    except JobLookupError:
        # 说明没找到job
        pass
    except Exception as e:
        return PikaResponse.failed(detail=str(e))
    return PikaResponse.success()


@router.get("/switch", summary="暂停或恢复测试计划")
async def switch_test_plan(id: int, status: bool, user_info=Depends(Permission(RoleEnum.MANAGER))):
    try:
        Scheduler.pause_resume_test_plan(id, status)
        return PikaResponse.success()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.get("/execute", summary="执行测试计划")
async def run_test_plan(id: int, user_info=Depends(Permission(RoleEnum.MANAGER))):
    try:
        asyncio.create_task(Executor.run_test_plan(id, user_info['emp_no']))
        return PikaResponse.success("开始执行，请耐心等待")
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.get("/follow", summary="关注测试计划")
async def follow_test_plan(id: int, user_info=Depends(Permission(RoleEnum.MANAGER))):
    try:
        await ApiTestPlanDao.follow_test_plan(id, user_info['emp_no'])
        return PikaResponse.success(message="关注成功")
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.get("/unfollow", summary="取消关注测试计划")
async def unfollow_test_plan(id: int, user_info=Depends(Permission(RoleEnum.MANAGER))):
    try:
        await ApiTestPlanDao.unfollow_test_plan(id, user_info['emp_no'])
        return PikaResponse.success(message="取关成功")
    except Exception as e:
        return PikaResponse.failed(detail=str(e))
