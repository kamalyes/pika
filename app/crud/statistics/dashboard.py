# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  dashboard
@Time    :  2022/8/9 11:09 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from datetime import datetime, timedelta

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import db_connect, PikaWrapper
from app.middleware.xredis import RedisHelper
from app.models.admin import SysUserAdminModel
from app.models.api_test_case import ApiTestCaseModel
from app.models.api_testplan import ApiTestPlanModel
from app.models.project import ProjectModel
from app.models.user import UserModel


class Item(object):
    def __init__(self, name, model):
        self.name = name
        self.model = model


class DashboardDao(PikaWrapper):

    @classmethod
    @db_connect
    async def get_statistics_data(cls, start: datetime, end: datetime,
                                  session: AsyncSession = None):
        return await cls.get_model_statistic_data(start, end, session,
                                                  Item("project", ProjectModel),
                                                  Item("testcase", ApiTestCaseModel),
                                                  Item("testplan", ApiTestPlanModel),
                                                  Item("useradmin", SysUserAdminModel))

    @classmethod
    @RedisHelper.cache("report_statistics")
    @db_connect
    async def get_report_statistics(cls, start: datetime, end: datetime,
                                    session: AsyncSession = None):
        result, idx = await cls.get_date_data(start, end)
        sql = cls.create_sql(ApiTestPlanModel, start, end, field="create_date")
        data = await session.execute(sql)
        count, success, failed, skip, error, total, total_pass = 0, 0, 0, 0, 0, 0, 0
        for item in data.scalars().all():
            date = item.start_at.strftime("%Y-%m-%d")
            count += 1
            total_pass += item.success_count
            total += item.success_count + item.failed_count + item.error_count
            success += item.success_count
            failed += item.failed_count
            error += item.error_count
            skip += item.skipped_count
            result[idx[date]]["count"] = result[idx[date]].get("count", 0) + 1
            result[idx[date]]["success"] = result[idx[date]].get("success", 0) + item.success_count
            result[idx[date]]["failed"] = result[idx[date]].get("failed", 0) + item.failed_count
            result[idx[date]]["error"] = result[idx[date]].get("error", 0) + item.error_count
            result[idx[date]]["skip"] = result[idx[date]].get("skip", 0) + item.skipped_count
            total = result[idx[date]]["success"] + result[idx[date]]["failed"] + result[idx[date]][
                "error"]
            if total == 0:
                result[idx[date]]["rate"] = 0.00
            else:
                result[idx[date]]["rate"] = round(result[idx[date]]["success"] / total * 100, 2)
        rate = round(total_pass / total, 2) if total > 0 else 0.00
        return dict(count=count, success=success, failed=failed, skip=skip, error=error,
                    data=result, rate=rate)

    @classmethod
    async def get_model_statistic_data(cls, start: datetime, end: datetime,
                                       session: AsyncSession = None, *names: Item):
        result, idx = await cls.get_date_data(start, end)
        data = dict()
        for n in names:
            query = await session.execute(cls.create_sql(n.model, start, end))
            # 找到未删除的所有项目数据
            counts = await session.execute(
                select(func.count(n.model.id)).where(n.model.delete_flag is False))
            for r in query.scalars().all():
                date = r.create_date.strftime("%Y-%m-%d")
                if result[idx[date]].get(n.name) is None:
                    result[idx[date]][n.name] = 1
                else:
                    result[idx[date]][n.name] += 1
            data[n.name] = counts.first().count
        return data, result

    @classmethod
    def create_sql(cls, model, start: datetime, end: datetime, *condition, field='create_date'):
        start_str = start.replace(hour=0, minute=0, second=0, microsecond=0)
        end_str = end.replace(hour=23, minute=59, second=59)
        return select(model).where(getattr(model, field) >= start_str,
                                   getattr(model, field) <= end_str,
                                   *condition)

    @classmethod
    async def get_date_data(cls, start: datetime, end: datetime):
        ans = []
        date_index = dict()
        start_time = start.replace(hour=0, minute=0, second=0, microsecond=0)
        while start_time <= end:
            date = start_time.strftime("%Y-%m-%d")
            ans.append({"date": date})
            date_index[date] = len(ans) - 1
            start_time += timedelta(days=1)
        return ans, date_index
