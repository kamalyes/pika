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

from app.core.handler.logger import PikaLogger
from app.models import async_session
from app.models.api_test_case import ApiTestCaseModel
from app.models.api_test_result import ApiTestResultModel


class ApiTestResultDao(object):
    log = PikaLogger("ApiTestResultDao")

    @staticmethod
    async def insert(report_id: int, case_id: int, case_name: str, status: int,
                     case_log: str, start_at: datetime, finished_at: datetime,
                     url: str, body: str, request_method: str, request_headers: str, cost: str,
                     asserts: str, response_headers: str, response: str,
                     status_code: int, cookies: str, retry: int = None,
                     request_params: str = '', data_name: str = '', data_id: int = None,
                     ) -> None:
        try:
            async with async_session() as session:
                async with session.begin():
                    result = ApiTestResultModel(report_id, case_id, case_name, status,
                                                case_log, start_at, finished_at,
                                                url, body, request_method, request_headers, cost,
                                                asserts, response_headers, response, status_code,
                                                cookies, retry, request_params, data_name, data_id)
                    session.add(result)
                    await session.flush()
        except Exception as e:
            ApiTestResultDao.log.error(f"新增测试结果失败, error: {e}")
            raise Exception("新增测试结果失败")

    @staticmethod
    async def list(report_id: int) -> List[ApiTestResultModel]:
        try:
            async with async_session() as session:
                sql = select(ApiTestResultModel, ApiTestCaseModel.directory_id).join(
                    ApiTestCaseModel,
                    ApiTestCaseModel.id == ApiTestResultModel.case_id). \
                    where(ApiTestResultModel.report_id == report_id,
                          ApiTestResultModel.delete_flag is False).order_by(
                    asc(ApiTestResultModel.case_id), asc(ApiTestResultModel.start_at))
                data = await session.execute(sql)
                ans = []
                for res, directory_id in data.all():
                    res.directory_id = directory_id
                    ans.append(res)
                return ans
        except Exception as e:
            ApiTestResultDao.log.error(f"获取测试用例执行记录失败, error: {e}")
            raise Exception("获取测试用例执行记录失败")
