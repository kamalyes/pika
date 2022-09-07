# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  statistics
@Time    :  2022/8/9 11:25 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from datetime import datetime, timedelta

from fastapi import Depends, APIRouter

from app.core.handler.jsonres import PikaResponse
from app.crud.itst.api.testcase import ApiTestCaseDao
from app.crud.statistics.dashboard import DashboardDao
from app.service import Permission
from app.utils.ws_manager import ws_manage

router = APIRouter()


@router.get("/statistics", description="获取统计数据", summary="获取平台统计数据")
async def query_follow_testplan(user_info=Depends(Permission())):
    end = datetime.today()
    start = datetime.today() - timedelta(days=6)
    rank = await ApiTestCaseDao.query_user_case_rank()
    count, data = await DashboardDao.get_statistics_data(start, end)
    report_data = await DashboardDao.get_report_statistics(start, end)
    online = ws_manage.get_clients()
    return PikaResponse.success(
        dict(count=count, data=data, rank=rank, clients=online, report=report_data))
