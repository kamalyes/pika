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
from typing import List

from sqlalchemy import and_, asc, update
from sqlalchemy.future import select

from app.crud import PikaMdWrapper, PikaWrapper
from app.models import async_session
from app.models.api_test_case import ApiTestCaseModel
from app.models.api_test_result import ApiTestResultModel
from app.schema.api_testcase_result import ApiTestCaseResultSchema


@PikaMdWrapper(ApiTestResultModel)
class ApiTestResultDao(PikaWrapper):
    @classmethod
    async def edit_report(cls, request: ApiTestCaseResultSchema, retry_id: str = None, case_id: str = None) -> None:
        try:
            async with async_session() as session:
                async with session.begin():
                    if retry_id is not None:
                        sql = (
                            update(cls.__model__)
                            .where(and_(ApiTestResultModel.id == retry_id, ApiTestResultModel.case_id == case_id))
                            .values(**request.__dict__)
                        )
                        await session.execute(sql)
                    else:
                        result = ApiTestResultModel(**request.__dict__)
                        session.add(result)
                    await session.flush()
                    return request
        except Exception as e:
            err_detail = f"新增测试结果失败, error: {str(e)}"
            await cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def list(cls, report_id: str) -> List[ApiTestResultModel]:
        try:
            async with async_session() as session:
                sql = (
                    select(ApiTestResultModel, ApiTestCaseModel.directory_id)
                    .join(ApiTestCaseModel, ApiTestCaseModel.id == ApiTestResultModel.case_id)
                    .where(ApiTestResultModel.report_id == report_id, ApiTestResultModel.delete_flag == 0)
                    .order_by(asc(ApiTestResultModel.case_id), asc(ApiTestResultModel.start_date))
                )
                data = await session.execute(sql)
                ans = []
                for res, directory_id in data.all():
                    res.directory_id = directory_id
                    ans.append(res)
                return ans
        except Exception as e:
            err_detail = f"获取测试用例执行记录失败, error: {str(e)}"
            await cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)
