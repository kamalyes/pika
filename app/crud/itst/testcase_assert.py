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

from app.core.handler.logger import PikaLogger
from app.crud import PikaMapper
from app.models import async_session, DatabaseHelper
from app.models.testcase_asserts import PikaTestCaseAsserts
from app.schema.testcase_schema import TestCaseAssertsForm
from app.utils.decorator import dao


@dao(PikaTestCaseAsserts, PikaLogger("TestCaseAssertsDao"))
class TestCaseAssertsDao(PikaMapper):

    @classmethod
    async def list_test_case_asserts(cls, case_id: int) -> List[PikaTestCaseAsserts]:
        """
        通过用例id获取断言数据
        :param case_id:
        :return:
        """
        try:
            async with async_session() as session:
                query = await session.execute(select(PikaTestCaseAsserts)
                                              .where(PikaTestCaseAsserts.case_id == case_id,
                                                     PikaTestCaseAsserts.is_delete == 0)).order_by(
                    asc(PikaTestCaseAsserts.name))
                return query.scalars().all()
        except Exception as e:
            cls.log.error(f"获取用例断言失败: {str(e)}")
            raise Exception("获取用例断言失败")

    @classmethod
    async def async_list_test_case_asserts(cls, case_id: int):
        try:
            async with async_session() as session:
                sql = select(PikaTestCaseAsserts).where(PikaTestCaseAsserts.case_id == case_id,
                                                        PikaTestCaseAsserts.is_delete == 0).order_by(
                    PikaTestCaseAsserts.name)
                case_list = await session.execute(sql)
                return case_list.scalars().all()
        except Exception as e:
            cls.log.error(f"获取用例断言失败: {str(e)}")
            raise Exception(f"获取用例断言失败: {str(e)}")

    @staticmethod
    async def insert_test_case_asserts(form: TestCaseAssertsForm, operator: int):
        try:
            ans = None
            async with async_session() as session:
                async with session.begin():
                    sql = select(PikaTestCaseAsserts).where(PikaTestCaseAsserts.case_id == form.case_id,
                                                            PikaTestCaseAsserts.name == form.name,
                                                            PikaTestCaseAsserts.is_delete == 0)
                    result = await session.execute(sql)
                    data = result.scalars().first()
                    if data is not None:
                        raise Exception("断言信息已存在, 请检查")
                    new_assert = PikaTestCaseAsserts(**form.dict(), operator=operator)
                    session.add(new_assert)
                    await session.flush()
                    await session.refresh(new_assert)
                    session.expunge(new_assert)
                    return new_assert
            return ans
        except Exception as e:
            TestCaseAssertsDao.log.error(f"新增用例断言失败, error: {e}")
            raise Exception(f"新增用例断言失败, {e}")

    @classmethod
    async def update_test_case_asserts(cls, form: TestCaseAssertsForm, operator: int) -> PikaTestCaseAsserts:
        """
        更新用例断言
        :param form:
        :param operator:
        :return:
        """
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = select(PikaTestCaseAsserts).where(PikaTestCaseAsserts.id == form.id,
                                                            PikaTestCaseAsserts.is_delete == 0)
                    result = await session.execute(sql)
                    data = result.scalars().first()
                    if data is None:
                        raise Exception("断言信息不存在, 请检查")
                    DatabaseHelper.update_model(data, form, operator)
                    await session.flush()
                    session.expunge(data)
                    return data
        except Exception as e:
            cls.log.error(f"编辑用例断言失败, error: {e}")
            raise Exception(f"编辑用例断言失败, {e}")

    @classmethod
    async def delete_test_case_asserts(cls, id: int, operator: int) -> None:
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = select(PikaTestCaseAsserts).where(PikaTestCaseAsserts.id == id,
                                                            PikaTestCaseAsserts.is_delete == 0)
                    result = await session.execute(sql)
                    data = result.scalars().first()
                    if data is None:
                        raise Exception("断言信息不存在, 请检查")
                    DatabaseHelper.delete_model(data, operator)
        except Exception as e:
            cls.log.error(f"编辑用例断言失败, error: {e}")
            raise Exception(f"编辑用例断言失败, {e}")
