# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  testcase_assert.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import List

from sqlalchemy import asc, select
from app.core.handler.execres import KeyExistException, KeyUndefinedException

from app.crud import PikaWrapper, PikaMdWrapper
from app.models import async_session
from app.models.api_testcase_asserts import ApiTestCaseAssertsModel
from app.schema.api_testcase import TestCaseAssertsForm


@PikaMdWrapper(ApiTestCaseAssertsModel)
class ApiTestCaseAssertsDao(PikaWrapper):

    @classmethod
    async def list_test_case_asserts(cls, case_id: int) -> List[ApiTestCaseAssertsModel]:
        """
        通过用例id获取断言数据
        Args:
            case_id:

        Returns:

        """
        try:
            async with async_session() as session:
                query = await session.execute(select(ApiTestCaseAssertsModel)
                                              .where(ApiTestCaseAssertsModel.case_id == case_id,
                                                     ApiTestCaseAssertsModel.delete_flag == 0)).order_by(
                    asc(ApiTestCaseAssertsModel.name))
                return query.scalars().all()
        except Exception as e:
            cls.__log__.error(f"获取用例断言失败: {str(e)}")
            raise Exception("获取用例断言失败")

    @classmethod
    async def async_list_test_case_asserts(cls, case_id: int):
        try:
            async with async_session() as session:
                sql = select(ApiTestCaseAssertsModel).where(
                    ApiTestCaseAssertsModel.case_id == case_id,
                    ApiTestCaseAssertsModel.delete_flag == 0).order_by(
                    ApiTestCaseAssertsModel.name)
                case_list = await session.execute(sql)
                return case_list.scalars().all()
        except Exception as e:
            cls.__log__.error(f"获取用例断言失败: {str(e)}")
            raise Exception(f"获取用例断言失败: {str(e)}")

    @staticmethod
    async def insert_test_case_asserts(form: TestCaseAssertsForm, operator: str):
        try:
            ans = None
            async with async_session() as session:
                async with session.begin():
                    sql = select(ApiTestCaseAssertsModel).where(
                        ApiTestCaseAssertsModel.case_id == form.case_id,
                        ApiTestCaseAssertsModel.name == form.name,
                        ApiTestCaseAssertsModel.delete_flag == 0)
                    result = await session.execute(sql)
                    data = result.scalars().first()
                    if data is not None:
                        raise KeyExistException("断言信息已存在, 请检查")
                    new_assert = ApiTestCaseAssertsModel(
                        **form.dict(), operator=operator)
                    session.add(new_assert)
                    # TODO bug：Could not refresh instance '<ApiTestCaseAssertsModel at 0x155e8af9be0>
                    await session.flush()
                    await session.refresh(new_assert)
                    session.expunge(new_assert)
                    return new_assert
            return ans
        except Exception as e:
            ApiTestCaseAssertsDao.__log__.error(f"新增用例断言失败, error: {e}")
            raise Exception(f"新增用例断言失败, {e}")

    @classmethod
    async def update_test_case_asserts(cls, form: TestCaseAssertsForm,
                                       operator: str) -> ApiTestCaseAssertsModel:
        """
        更新用例断言
        Args:
            form:
            operator:

        Returns:

        """
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = select(ApiTestCaseAssertsModel).where(
                        ApiTestCaseAssertsModel.id == form.id,
                        ApiTestCaseAssertsModel.delete_flag == 0)
                    result = await session.execute(sql)
                    data = result.scalars().first()
                    if data is None:
                        raise KeyUndefinedException("断言信息不存在, 请检查")
                    cls.update_model(data, form, operator)
                    await session.flush()
                    session.expunge(data)
                    return data
        except Exception as e:
            cls.__log__.error(f"编辑用例断言失败, error: {e}")
            raise Exception(f"编辑用例断言失败, {e}")

    @classmethod
    async def delete_test_case_asserts(cls, id: int, operator: str) -> None:
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = select(ApiTestCaseAssertsModel).where(ApiTestCaseAssertsModel.id == id,
                                                                ApiTestCaseAssertsModel.delete_flag == 0)
                    result = await session.execute(sql)
                    data = result.scalars().first()
                    if data is None:
                        raise KeyUndefinedException("断言信息不存在, 请检查")
                    cls.delete_model(data, operator)
        except Exception as e:
            cls.__log__.error(f"删除用例断言失败, error: {e}")
            raise Exception(f"删除用例断言失败, {e}")
