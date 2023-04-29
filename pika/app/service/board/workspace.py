# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  workspace.py
@Time    :  2022/6/18 2:27 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends

from app.core.handler.jsonres import PikaResponse
from app.crud.board.statistics import DashboardDao
from app.crud.itst.api.testcase import ApiTestCaseDao
from app.crud.pmp.project import ProjectDao
from app.crud.pmp.testplan import ApiTestPlanDao
from app.models import async_db_session_iterator
from app.service import Permission
from app.utils.ws_manager import ws_manage

router = APIRouter()


@router.get("/", summary="获取工作台用户统计数据")
async def query_user_statistics(user_info=Depends(Permission()), session=Depends(async_db_session_iterator)):
    operator = user_info["emp_no"]
    count = await ProjectDao.query_user_project(operator)
    rank = await ApiTestCaseDao.query_user_case_list()
    now = datetime.now()
    weekly_case = await ApiTestCaseDao.query_weekly_user_case(operator, (now - timedelta(days=7)), now)
    case_count, user_rank = rank.get(operator, [0, 0])
    return PikaResponse.success(
        data={
            "project_count": count,
            "case_count": case_count,
            "weekly_case": weekly_case,
            "user_rank": user_rank,
            "total_user": len(rank),
        },
    )


@router.get("/testplan", summary="获取用户关注的测试计划执行数据")
async def query_follow_testplan(user_info=Depends(Permission())):
    operator = user_info["emp_no"]
    ans = await ApiTestPlanDao.query_user_follow_test_plan(operator)
    return PikaResponse.success(data=ans)


@router.get("/statistics", description="获取统计数据", summary="获取平台统计数据")
async def query_follow_testplan(user_info=Depends(Permission())):
    end = datetime.today()
    start = datetime.today() - timedelta(days=6)
    rank = await ApiTestCaseDao.query_user_case_rank()
    count, data = await DashboardDao.get_statistics_data(start, end)
    report_data = await DashboardDao.get_report_statistics(start, end)
    online = ws_manage.get_clients()
    return PikaResponse.success({"count": count, "data": data, "rank": rank, "clients": online, "report": report_data})
