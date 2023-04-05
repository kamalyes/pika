# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  testresult.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from datetime import datetime
from typing import List

from sqlalchemy import asc
from sqlalchemy.future import select
from app.core.handler.exceres import SystemException

from app.crud import PikaWrapper, PikaMdWrapper
from app.models import async_session
from app.models.api_test_case import ApiTestCaseModel
from app.models.api_test_result import ApiTestResultModel


@PikaMdWrapper(ApiTestResultModel)
class ApiTestResultDao(PikaWrapper):

    @classmethod
    async def insert_report(cls, report_id: str, case_id: str, case_name: str, status: int,
                            case_log: str, start_date: datetime, finished_date: datetime,
                            url: str, body: str, request_method: str, request_headers: str,
                            cost: str,
                            asserts: str, response_headers: str, response: str,
                            status_code: int, cookies: str, retry: int = None,
                            request_params: str = None, data_name: str = None, data_id: str = None,
                            ) -> None:
        try:
            async with async_session() as session:
                async with session.begin():
                    result = ApiTestResultModel(report_id, case_id, case_name, status,
                                                case_log, start_date, finished_date,
                                                url, body, request_method, request_headers, cost,
                                                asserts, response_headers, response, status_code,
                                                cookies, retry, request_params, data_name, data_id)
                    session.add(result)
                    await session.flush()
        except Exception as e:
            cls.__log__.error(f"新增测试结果失败, error: {e}")
            raise SystemException(detail="新增测试结果失败")

    @classmethod
    async def list(cls, report_id: str) -> List[ApiTestResultModel]:
        try:
            async with async_session() as session:
                sql = select(ApiTestResultModel, ApiTestCaseModel.directory_id).join(
                    ApiTestCaseModel,
                    ApiTestCaseModel.id == ApiTestResultModel.case_id). \
                    where(ApiTestResultModel.report_id == report_id,
                          ApiTestResultModel.delete_flag == 0).order_by(
                    asc(ApiTestResultModel.case_id), asc(ApiTestResultModel.start_date))
                data = await session.execute(sql)
                ans = []
                for res, directory_id in data.all():
                    res.directory_id = directory_id
                    ans.append(res)
                return ans
        except Exception as e:
            cls.__log__.error(f"获取测试用例执行记录失败, error: {e}")
            raise SystemException(detail="获取测试用例执行记录失败")
