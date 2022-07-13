# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  testcase_out_params.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import time
from datetime import datetime
from typing import List

from sqlalchemy import select, update

from app.core.handler.logger import PikaLogger
from app.crud import PikaMapper
from app.middleware.xredis import RedisHelper
from app.models import async_session
from app.models.api_testcase_out_parameters import ApiTestCaseOutParametersModel
from app.schema.api_testcase_out_parameters import ApiTestCaseOutParametersSchema
from app.utils.decorator import dao


@dao(ApiTestCaseOutParametersModel, PikaLogger("ApiTestCaseOutParametersDao"))
class ApiTestCaseOutParametersDao(PikaMapper):

    @classmethod
    async def should_remove(cls, before, after):
        """
        找出要删除的数据
        Args:
            before:
            after:

        Returns:

        """
        data = []
        for b in before:
            for a in after:
                if a.id == b.id:
                    break
            else:
                data.append(b.id)
        return data

    @classmethod
    @RedisHelper.up_cache("dao")
    async def update_many(cls, case_id: int, data: List[ApiTestCaseOutParametersSchema],
                          operator_emp_no: str):
        result = []
        try:
            async with async_session() as session:
                async with session.begin():
                    source = await session.execute(select(ApiTestCaseOutParametersModel).where(
                        ApiTestCaseOutParametersModel.case_id == case_id,
                        ApiTestCaseOutParametersModel.delete_flag == False,
                    ))
                    before = source.scalars().all()
                    should_remove = await cls.should_remove(before, data)
                    for item in data:
                        if item.id is None:
                            # add
                            temp = ApiTestCaseOutParametersModel(**item.dict(), case_id=case_id,
                                                                 operator=operator_emp_no)
                            session.add(temp)
                        else:
                            query = await session.execute(
                                select(ApiTestCaseOutParametersModel).where(
                                    ApiTestCaseOutParametersModel.id == item.id,
                                ))
                            temp = query.scalars().first()
                            if temp is None:
                                # 走新增逻辑
                                temp = ApiTestCaseOutParametersModel(**item.dict(), case_id=case_id,
                                                                     operator=operator_emp_no)
                                session.add(temp)
                            else:
                                temp.name = item.name
                                temp.case_id = case_id
                                temp.expression = item.expression
                                temp.source = item.source
                                temp.match_index = item.match_index
                                temp.update_user = operator_emp_no
                                temp.update_date = datetime.now()
                        await session.flush()
                        session.expunge(temp)
                        result.append(temp)
                    if should_remove:
                        await session.execute(
                            update(ApiTestCaseOutParametersModel).where(
                                ApiTestCaseOutParametersModel.id.in_(should_remove)).values(
                                delete_flag=int(time.time() * 1000)))
            return result
        except Exception as e:
            cls.log.error(f"批量更新出参数据失败: {e}")
            raise Exception(f"批量更新出参数据失败: {e}")
