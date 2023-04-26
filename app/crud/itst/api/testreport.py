# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  testreport.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from datetime import datetime

from sqlalchemy import select, desc
from app.core.handler.exceres import KeyUndefinedException, SystemException

from app.crud import PikaWrapper, PikaMdWrapper
from app.crud.itst.api.testresult import ApiTestResultDao
from app.models import async_session
from app.models.api_test_report import ApiTestReportModel
from app.models.api_testplan import ApiTestPlanModel


@PikaMdWrapper(ApiTestReportModel)
class ApiTestReportDao(PikaWrapper):

    @classmethod
    async def start(cls, executor: str, env: str, mode: int = 0, plan_id: str = None) -> int:
        """
        生成buildId,开始执行任务,任务完成后通过回调方法更新报告
        :return: 返回report_id
        """
        try:
            async with async_session() as session:
                async with session.begin():
                    report = ApiTestReportModel(executor, env, mode=mode, plan_id=plan_id)
                    session.add(report)
                    await session.flush()
                    return report.id
        except Exception as e:
            cls.__log__.error(f"新增报告失败, error: {e}")
            raise SystemException(detail="新增报告失败")

    @classmethod
    async def update(cls, report_id: str, status) -> None:
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = select(ApiTestReportModel).where(
                        ApiTestReportModel.id == report_id)
                    data = await session.execute(sql)
                    report = data.scalars().first()
                    if report is None:
                        raise SystemException(detail="更新报告失败")
                    report.status = status
        except Exception as e:
            cls.__log__.error(f"更新报告失败, error: {e}")
            raise SystemException(detail="更新报告失败")

    @classmethod
    async def end(cls, report_id: str, success_count: int, failed_count: int,
                  error_count: int, skipped_count: int, status: int,
                  cost: str) -> ApiTestReportModel:
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = select(ApiTestReportModel).where(
                        ApiTestReportModel.id == report_id)
                    data = await session.execute(sql)
                    report = data.scalars().first()
                    if report is None:
                        raise Exception("更新报告失败")
                    report.status = status
                    report.success_count = success_count
                    report.failed_count = failed_count
                    report.error_count = error_count
                    report.skipped_count = skipped_count
                    report.cost = cost
                    report.finished_date = datetime.now()
                    await session.flush()
                    session.expunge(report)
                    return report
        except Exception as e:
            cls.__log__.error(f"更新报告失败, error: {e}")
            raise SystemException(detail="更新报告失败")

    @classmethod
    async def query(cls, report_id: str):
        """
        根据报告id查询报告
        Args:
            report_id:

        Returns:

        """
        try:
            async with async_session() as session:
                sql = select(ApiTestReportModel, ApiTestPlanModel.name) \
                    .outerjoin(ApiTestPlanModel,
                               ApiTestPlanModel.id == ApiTestReportModel.plan_id
                               ).where(
                    ApiTestReportModel.id == report_id)
                data = await session.execute(sql)
                if data is None:
                    raise Exception("报告不存在")
                report, plan_name = data.first()
                test_data = await ApiTestResultDao.list(report_id)
                return report, test_data, plan_name
        except Exception as e:
            cls.__log__.error(f"查询报告失败: {e}")
            raise SystemException(detail=f"查询报告失败: {e}")

    @classmethod
    async def list_report(cls, paging, start_date: datetime, finished_date: datetime,
                          executor: str = None):
        """
        获取报告列表
        Args:
            paging:
            start_date:
            finished_date:
            executor:

        Returns:

        """
        try:
            async with async_session() as session:
                sql = select(ApiTestReportModel).where(
                    ApiTestReportModel.start_date.between(start_date, finished_date)).order_by(
                    desc(ApiTestReportModel.start_date))
                if executor is not None:
                    sql = sql.where(ApiTestReportModel.executor == executor)
                data = await session.execute(sql)
                total = data.raw.rowcount
                if total == 0:
                    return [], 0
                sql = sql.offset((paging.page_index - 1) *
                                 paging.page_size).limit(paging.page_size)
                data = await session.execute(sql)
                return data.scalars().all(), total
        except Exception as e:
            cls.__log__.error(f"查询构建记录失败: {e}")
            raise SystemException(detail=f"查询构建记录失败: {e}")
