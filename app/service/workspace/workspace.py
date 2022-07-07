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
from app.crud.itst.testcase import TestCaseDao
from app.crud.project.project import ProjectDao
from app.crud.project.testplan import PikaTestPlanDao
from app.service import Permission

router = APIRouter()


@router.get("/", description="获取工作台用户统计数据")
async def query_user_statistics(user_info=Depends(Permission())):
    operator = user_info['emp_no']
    count = await ProjectDao.query_user_project(operator)
    rank = await TestCaseDao.query_user_case_list()
    now = datetime.now()
    weekly_case = await TestCaseDao.query_weekly_user_case(operator, (now - timedelta(days=15)), now)
    case_count, user_rank = rank.get(str(operator), [0, 0])
    return PikaResponse.success(data=dict(project_count=count, case_count=case_count,
                                            weekly_case=weekly_case,
                                            user_rank=user_rank, total_user=len(rank)))


@router.get("/testplan", description="获取用户关注的测试计划执行数据")
async def query_follow_testplan(user_info=Depends(Permission())):
    operator = user_info['emp_no']
    ans = await PikaTestPlanDao.query_user_follow_test_plan(operator)
    return PikaResponse.success(data=ans)
