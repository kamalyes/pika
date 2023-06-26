# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  jmeter.py
@Time    :  2022/6/18 2:19 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  jmeter服务
"""

from uuid import uuid4
from app.core.handler.logger import PikaLogger
from app.crud import PikaWrapper
from app.schema.jmeter import (
    JmeterUploadResultSchema,
    JmeterLatestBuildSchema,
    JmeterChartDataSchema,
    JmeterSummaryListSchema,
    JmeterCaseDetailSchema,
)
from app.crud import PikaMdWrapper
from app.models.jmeter import JmeterTestCaseModel, JmeterTestSummaryModel
from sqlalchemy import or_, and_, select, desc
from app.models import async_session, async_db_session_generator
from app.core.handler.jsonres import PikaModelEncoder


@PikaMdWrapper(JmeterTestSummaryModel, JmeterTestCaseModel)
class JmeterDao(PikaWrapper, PikaModelEncoder):
    log = PikaLogger("JmeterDao")

    @classmethod
    async def upload_result(cls, request: JmeterUploadResultSchema):
        test_summary, test_cases = request.test_summary, request.test_cases
        try:
            async with async_session() as session:
                async with session.begin():
                    test_summary_ = JmeterTestSummaryModel(**test_summary.dict())
                    session.add(test_summary_)
                    test_cases_ = [
                        cls.model_to_dict(
                            JmeterTestCaseModel(batch_no=test_summary.batch_no, id=str(uuid4()), **tc.dict())
                        )
                        for tc in test_cases
                    ]
                    if test_cases_:
                        await session.execute(
                            JmeterTestCaseModel.__table__.insert(), [test_case for test_case in test_cases_]
                        )
        except Exception as e:
            err_detail = f"Jmeter测试报告上传失败, {e}"
            cls.__log__.error(err_detail)
            raise Exception(err_detail)

    @classmethod
    async def query_base_info(cls) -> JmeterLatestBuildSchema:
        try:
            async with async_db_session_generator() as session:
                async with session.begin():
                    env_sql = select(JmeterTestSummaryModel.env).distinct(JmeterTestSummaryModel.env)
                    project_sql = select(JmeterTestSummaryModel.project).distinct(JmeterTestSummaryModel.project)
                    query_env = await session.execute(env_sql)
                    query_project = await session.execute(project_sql)
                    env_data = query_env.scalars().all()
                    project_data = query_project.scalars().all()
            return {"env": cls.model_to_list(env_data), "project": cls.model_to_list(project_data)}
        except Exception as e:
            err_detail = f"查询JmeterTestSummaryBaseInfo失败, {e}"
            cls.__log__.error(err_detail)
            raise Exception(err_detail)

    @classmethod
    async def query_latest_build(cls, request: JmeterLatestBuildSchema):
        try:
            filters = []
            if request.env and request.project:
                filters = [JmeterTestSummaryModel.env == request.env, JmeterTestSummaryModel.project == request.project]
            async with async_db_session_generator() as session:
                async with session.begin():
                    _sql = (
                        select(JmeterTestSummaryModel).where(*filters).order_by(desc(JmeterTestSummaryModel.end_time))
                    )
                    query_data = await session.execute(_sql)
                    result = query_data.scalars().first()
            return result
        except Exception as e:
            err_detail = f"查询JmeterTestSummaryLatestBuild失败, {e}"
            cls.__log__.error(err_detail)
            raise Exception(err_detail)

    @classmethod
    async def query_chart_data(cls, request: JmeterChartDataSchema) -> JmeterTestSummaryModel:
        try:
            async with async_db_session_generator() as session:
                async with session.begin():
                    chart_type = 1 if request.chart_type not in (1, 2) else request.chart_type
                    _sql = (
                        select(
                            (
                                JmeterTestSummaryModel.id,
                                JmeterTestSummaryModel.batch_no,
                                JmeterTestSummaryModel.os_type,
                                JmeterTestSummaryModel.success,
                                JmeterTestSummaryModel.failure,
                                JmeterTestSummaryModel.total,
                            )
                            if chart_type == 1
                            else (
                                JmeterTestSummaryModel.id,
                                JmeterTestSummaryModel.batch_no,
                                JmeterTestSummaryModel.pass_rate,
                            )
                        )
                        .where(
                            and_(
                                JmeterTestSummaryModel.env == request.env,
                                JmeterTestSummaryModel.project == request.project,
                            )
                            if request.env and request.project
                            else or_(
                                JmeterTestSummaryModel.start_time >= request.start_time,
                                JmeterTestSummaryModel.end_time <= request.end_time,
                            )
                        )
                        .order_by(desc(JmeterTestSummaryModel.end_time))
                        .offset(0)
                        .limit(20)
                    )
                    query_data = await session.execute(_sql)
            return query_data.all()
        except Exception as e:
            err_detail = f"查询JmeterChartData失败, {e}"
            cls.__log__.error(err_detail)
            raise Exception(err_detail)

    @classmethod
    async def query_summary_list(cls, request: JmeterSummaryListSchema):
        try:
            os_type_ = [1, 2] if request.os_type == 0 else [request.os_type]
            filters = [JmeterTestSummaryModel.os_type.in_(os_type_)]
            if request.env and request.project:
                filters += [
                    JmeterTestSummaryModel.env == request.env,
                    JmeterTestSummaryModel.project == request.project,
                ]
            async with async_session() as session:
                sql = select(JmeterTestSummaryModel).where(*filters).order_by(JmeterTestSummaryModel.end_time.desc())
                result, total = await cls.pagination(request.page_index, request.page_size, session, sql, True)
                return result, total
        except Exception as e:
            err_detail = f"获取JmeterSummary失败, error: {str(e)}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)
            raise Exception(err_detail)

    @classmethod
    async def query_case_detail(cls, request: JmeterCaseDetailSchema):
        try:
            async with async_db_session_generator() as session:
                async with session.begin():
                    jts_sql = select(JmeterTestSummaryModel).where(JmeterTestSummaryModel.id == request.id)
                    jts_exec = await session.execute(jts_sql)
                    summary_info = jts_exec.scalars().first()
                    if summary_info is None:
                        raise Exception("数据不存在")
                    jtc_sql = (
                        select(JmeterTestCaseModel)
                        .where(JmeterTestCaseModel.batch_no == summary_info.batch_no)
                        .order_by(JmeterTestCaseModel.error_count.desc(), JmeterTestCaseModel.end_time.desc())
                    )
                    jtc_exec = await session.execute(jtc_sql)
                    case_info = jtc_exec.scalars().all()
            return {"summary_info": summary_info, "case_info": case_info}
        except Exception as e:
            err_detail = f"查询JmeterTestCaseDetail失败, {e}"
            cls.__log__.error(err_detail)
            raise Exception(err_detail)
