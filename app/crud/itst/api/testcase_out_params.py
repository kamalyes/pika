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
from custard.time import Moment
from datetime import datetime
from typing import List

from sqlalchemy import select, update
from app.core.handler.exceres import SystemException

from app.crud import PikaWrapper, PikaMdWrapper
from app.middleware.xredis import RedisHelper
from app.models import async_session
from app.models.api_testcase_out_parameters import ApiTestCaseOutParametersModel
from app.schema.api_testcase_out_parameters import ApiTestCaseOutParametersSchema


@PikaMdWrapper(ApiTestCaseOutParametersModel)
class ApiTestCaseOutParametersDao(PikaWrapper):
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
            if b.id not in after:
                data.append(b.id)
        return data

    @classmethod
    @RedisHelper.up_cache("dao")
    async def update_many(cls, case_id: str, data: List[ApiTestCaseOutParametersSchema], operator: str):
        result = []
        try:
            async with async_session() as session:
                async with session.begin():
                    source = await session.execute(
                        select(ApiTestCaseOutParametersModel).where(
                            ApiTestCaseOutParametersModel.case_id == case_id,
                            ApiTestCaseOutParametersModel.delete_flag == 0,
                        )
                    )
                    before = source.scalars().all()
                    for item in data:
                        query = await session.execute(
                            select(ApiTestCaseOutParametersModel).where(
                                ApiTestCaseOutParametersModel.id == item.id,
                            )
                        )
                        temp = query.scalars().first()
                        if temp is None:
                            # 走新增逻辑
                            temp = ApiTestCaseOutParametersModel(**item.dict(), case_id=case_id, operator=operator)
                            session.add(temp)
                        else:
                            temp.name = item.name
                            temp.expression = item.expression
                            temp.source = item.source
                            temp.match_index = item.match_index
                            temp.update_user = operator
                            temp.update_date = datetime.now()
                        await session.flush()
                        session.expunge(temp)
                        result.append(temp)
                    should_remove = await cls.should_remove(before, [x.id for x in result])
                    if should_remove:
                        await session.execute(
                            update(ApiTestCaseOutParametersModel)
                            .where(ApiTestCaseOutParametersModel.id.in_(should_remove))
                            .values(delete_flag=1, delete_date=Moment.get_now_time())
                        )
            return result
        except Exception as e:
            cls.__log__.error(f"批量更新出参数据失败: {e}")
            raise SystemException(detail=f"批量更新出参数据失败: {e}")
