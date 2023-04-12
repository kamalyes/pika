# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  OperationEnum.py
@Time    :  2022/6/17 12:55 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from datetime import datetime

from sqlalchemy import func, select

from app.crud import PikaWrapper, PikaMdWrapper
from app.models import async_session
from app.models.system import OperationLogModel


@PikaMdWrapper(OperationLogModel)
class PikaOperationDao(PikaWrapper):

    @classmethod
    async def count_user_activities(cls, operator, start_date: datetime, finished_date: datetime):
        """
        根据开始/结束时间 获取用户的活动日历(操作记录的数量)
        Args:
            operator:
            start_date:
            finished_date:

        Returns:

        """
        async with async_session() as session:
            async with session.begin():
                sql = select(OperationLogModel.operator_date,
                             func.count(OperationLogModel.id)).where(
                    OperationLogModel.operator_date.between(start_date, finished_date),
                    OperationLogModel.operator == operator) \
                    .group_by(OperationLogModel.operator_date).order_by(
                    OperationLogModel.operator_date)
                data = await session.execute(sql)
                return data.all()
