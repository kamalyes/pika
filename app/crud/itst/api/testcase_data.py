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
from app.core.handler.execres import KeyExistException, KeyUndefinedException

from app.crud import PikaWrapper, PikaMdWrapper
from app.models import async_session
from app.models.api_testcase_data import ApiTestCaseDataModel
from app.schema.api_testcase_data import ApiTestCaseDataSchema


@PikaMdWrapper(ApiTestCaseDataModel)
class ApiTestCaseDataDao(PikaWrapper):

    @classmethod
    async def insert_testcase_data(cls, form: ApiTestCaseDataSchema, operator: str):
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = select(ApiTestCaseDataModel).where(
                        ApiTestCaseDataModel.case_id == form.case_id,
                        ApiTestCaseDataModel.env == form.env,
                        ApiTestCaseDataModel.name == form.name,
                        ApiTestCaseDataModel.delete_flag == 0)
                    result = await session.execute(sql)
                    query = result.scalars().first()
                    if query is not None:
                        raise KeyExistException("该数据已存在, 请重新编辑")
                    data = ApiTestCaseDataModel(
                        **form.dict(), operator=operator)
                    session.add(data)
                    await session.flush()
                    await session.refresh(data)
                    session.expunge(data)
                    return data
        except Exception as e:
            cls.__log__.error(f"新增测试数据失败, error: {str(e)}")
            raise Exception(f"新增测试数据失败, {str(e)}")

    @classmethod
    async def update_testcase_data(cls, form: ApiTestCaseDataSchema, operator: str):
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = select(ApiTestCaseDataModel).where(ApiTestCaseDataModel.id == form.id,
                                                             ApiTestCaseDataModel.delete_flag == 0)
                    result = await session.execute(sql)
                    query = result.scalars().first()
                    if query is None:
                        raise KeyUndefinedException("测试数据不存在")
                    cls.update_model(query, form, operator)
                    await session.flush()
                    session.expunge(query)
                    return query
        except Exception as e:
            cls.__log__.error(f"编辑测试数据失败, error: {str(e)}")
            raise Exception(f"编辑测试数据失败, {str(e)}")

    @classmethod
    async def delete_testcase_data(cls, id: int, operator: str):
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = select(ApiTestCaseDataModel).where(ApiTestCaseDataModel.id == id,
                                                             ApiTestCaseDataModel.delete_flag == 0)
                    result = await session.execute(sql)
                    query = result.scalars().first()
                    if query is None:
                        raise KeyUndefinedException("测试数据不存在")
                    cls.delete_model(query, operator)
        except Exception as e:
            cls.__log__.error(f"删除测试数据失败, error: {str(e)}")
            raise Exception(f"删除测试数据失败, {str(e)}")

    @classmethod
    async def list_testcase_data(cls, case_id: int):
        ans = defaultdict(list)
        try:
            async with async_session() as session:
                sql = select(ApiTestCaseDataModel).where(ApiTestCaseDataModel.case_id == case_id,
                                                         ApiTestCaseDataModel.delete_flag == 0)
                result = await session.execute(sql)
                query = result.scalars().all()
                for q in query:
                    ans[q.env].append(q)
                return ans
        except Exception as e:
            cls.__log__.error(f"查询测试数据失败, error: {str(e)}")
            raise Exception(f"查询测试数据失败, {str(e)}")

    @classmethod
    async def list_testcase_data_by_env(cls, env: int, case_id: int) -> List[ApiTestCaseDataModel]:
        try:
            async with async_session() as session:
                sql = select(ApiTestCaseDataModel).where(ApiTestCaseDataModel.case_id == case_id,
                                                         ApiTestCaseDataModel.env == env,
                                                         ApiTestCaseDataModel.delete_flag == 0)
                result = await session.execute(sql)
                return result.scalars().all()
        except Exception as e:
            cls.__log__.error(f"查询测试数据失败, error: {str(e)}")
            raise Exception(f"查询测试数据失败, {str(e)}")
