# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  api_testcase_data.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from collections import defaultdict
from typing import List

from sqlalchemy import select

from app.core.handler.logger import PikaLogger
from app.crud import PikaMapper
from app.models import async_session, DatabaseHelper
from app.models.api_testcase_data import ApiTestCaseDataModel
from app.schema.api_testcase_data import ApiTestCaseDataSchema
from app.utils.decorator import dao


@dao(ApiTestCaseDataModel, PikaLogger("ApiTestCaseDataDao"))
class ApiTestCaseDataDao(PikaMapper):

    @classmethod
    async def insert_testcase_data(cls, form: ApiTestCaseDataSchema, operator_emp_no: str):
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = select(ApiTestCaseDataModel).where(
                        ApiTestCaseDataModel.case_id == form.case_id,
                        ApiTestCaseDataModel.env == form.env,
                        ApiTestCaseDataModel.name == form.name,
                        ApiTestCaseDataModel.delete_flag == False)
                    result = await session.execute(sql)
                    query = result.scalars().first()
                    if query is not None:
                        raise Exception("该数据已存在, 请重新编辑")
                    data = ApiTestCaseDataModel(**form.dict(), operator=operator_emp_no)
                    session.add(data)
                    await session.flush()
                    await session.refresh(data)
                    session.expunge(data)
                    return data
        except Exception as e:
            cls.log.error(f"新增测试数据失败, error: {str(e)}")
            raise Exception(f"新增测试数据失败, {str(e)}")

    @classmethod
    async def update_testcase_data(cls, form: ApiTestCaseDataSchema, operator_emp_no: int):
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = select(ApiTestCaseDataModel).where(ApiTestCaseDataModel.id == form.id,
                                                             ApiTestCaseDataModel.delete_flag == False)
                    result = await session.execute(sql)
                    query = result.scalars().first()
                    if query is None:
                        raise Exception("测试数据不存在")
                    DatabaseHelper.update_model(query, form, operator_emp_no)
                    await session.flush()
                    session.expunge(query)
                    return query
        except Exception as e:
            cls.log.error(f"编辑测试数据失败, error: {str(e)}")
            raise Exception(f"编辑测试数据失败, {str(e)}")

    @classmethod
    async def delete_testcase_data(cls, id: int, operator_emp_no: int):
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = select(ApiTestCaseDataModel).where(ApiTestCaseDataModel.id == id,
                                                             ApiTestCaseDataModel.delete_flag == False)
                    result = await session.execute(sql)
                    query = result.scalars().first()
                    if query is None:
                        raise Exception("测试数据不存在")
                    DatabaseHelper.delete_model(query, operator_emp_no)
        except Exception as e:
            cls.log.error(f"删除测试数据失败, error: {str(e)}")
            raise Exception(f"删除测试数据失败, {str(e)}")

    @classmethod
    async def list_testcase_data(cls, case_id: int):
        ans = defaultdict(list)
        try:
            async with async_session() as session:
                sql = select(ApiTestCaseDataModel).where(ApiTestCaseDataModel.case_id == case_id,
                                                         ApiTestCaseDataModel.delete_flag == False)
                result = await session.execute(sql)
                query = result.scalars().all()
                for q in query:
                    ans[q.env].append(q)
                return ans
        except Exception as e:
            cls.log.error(f"查询测试数据失败, error: {str(e)}")
            raise Exception(f"查询测试数据失败, {str(e)}")

    @classmethod
    async def list_testcase_data_by_env(cls, env: int, case_id: int) -> List[ApiTestCaseDataModel]:
        try:
            async with async_session() as session:
                sql = select(ApiTestCaseDataModel).where(ApiTestCaseDataModel.case_id == case_id,
                                                         ApiTestCaseDataModel.env == env,
                                                         ApiTestCaseDataModel.delete_flag == False)
                result = await session.execute(sql)
                return result.scalars().all()
        except Exception as e:
            cls.log.error(f"查询测试数据失败, error: {str(e)}")
            raise Exception(f"查询测试数据失败, {str(e)}")
