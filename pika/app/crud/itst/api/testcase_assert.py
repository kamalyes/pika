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
from app.crud import PikaWrapper, PikaMdWrapper
from app.models import async_session
from app.models.api_testcase_asserts import ApiTestCaseAssertsModel
from app.schema.api_testcase import TestCaseAssertsSchema


@PikaMdWrapper(ApiTestCaseAssertsModel)
class ApiTestCaseAssertsDao(PikaWrapper):

    @classmethod
    async def list_test_case_asserts(cls, case_id: str) -> List[ApiTestCaseAssertsModel]:
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
            err_detail = f"获取用例断言失败, error: {str(e)}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def async_list_test_case_asserts(cls, case_id: str):
        try:
            async with async_session() as session:
                sql = select(ApiTestCaseAssertsModel).where(
                    ApiTestCaseAssertsModel.case_id == case_id,
                    ApiTestCaseAssertsModel.delete_flag == 0).order_by(
                    ApiTestCaseAssertsModel.name)
                case_list = await session.execute(sql)
                return case_list.scalars().all()
        except Exception as e:
            err_detail = f"获取用例断言失败, error: {str(e)}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def insert_test_case_asserts(cls, form: TestCaseAssertsSchema, operator: str):
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
                        raise Exception("断言信息已存在, 请检查")
                    new_assert = ApiTestCaseAssertsModel(
                        **form.dict(), operator=operator)
                    session.add(new_assert)
                    # TODO bug:Could not refresh instance '<ApiTestCaseAssertsModel at 0x155e8af9be0>
                    await session.flush()
                    await session.refresh(new_assert)
                    session.expunge(new_assert)
                    return new_assert
            return ans
        except Exception as e:
            err_detail = f"新增用例断言失败, error: {e}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def update_test_case_asserts(cls, form: TestCaseAssertsSchema,
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
                        raise Exception("断言信息不存在, 请检查")
                    cls.update_model(data, form, operator)
                    await session.flush()
                    session.expunge(data)
                    return data
        except Exception as e:
            err_detail = f"编辑用例断言失败, error: {e}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def delete_test_case_asserts(cls, id: str, operator: str) -> None:
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = select(ApiTestCaseAssertsModel).where(ApiTestCaseAssertsModel.id == id,
                                                                ApiTestCaseAssertsModel.delete_flag == 0)
                    result = await session.execute(sql)
                    data = result.scalars().first()
                    if data is None:
                        raise Exception("断言信息不存在, 请检查")
                    cls.delete_model(data, operator)
        except Exception as e:
            err_detail = f"删除用例断言失败, error: {e}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)
