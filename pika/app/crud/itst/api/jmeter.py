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
from app.schema.jmeter import JmeterUploadResultSchema
from app.crud import PikaMdWrapper
from app.models.jmeter import JmeterTestCaseModel, JmeterTestSummaryModel
from sqlalchemy import asc, select, and_
from app.models import async_session
from app.core.handler.jsonres import PikaResponse


@PikaMdWrapper(JmeterTestSummaryModel, JmeterTestCaseModel)
class JmeterDao(PikaWrapper):
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
                        PikaResponse.model_to_dict(
                            JmeterTestCaseModel(batch_no=test_summary.batch_no, id=str(uuid4()), **tc.dict())
                        )
                        for tc in test_cases
                    ]
                    await session.execute(
                        JmeterTestCaseModel.__table__.insert(), [test_case for test_case in test_cases_]
                    )
        except Exception as e:
            cls.__log__.error(f"新增前/后置条件: {test_summary.batch_no}失败, {e}")
            raise Exception(f"新增前/后置条件失败, {e}")

    @classmethod
    async def query_latest_build(cls):
        # TODO document why this method is empty
        pass

    @classmethod
    async def query_chart_data(cls):
        # TODO document why this method is empty
        pass

    @classmethod
    async def query_summary_list(cls):
        # TODO document why this method is empty
        pass

    @classmethod
    async def query_case_detail(cls):
        # TODO document why this method is empty
        pass

    @classmethod
    async def query_base_info(cls):
        # TODO document why this method is empty
        pass
