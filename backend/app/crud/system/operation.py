# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  operation.py
@Time    :  2022/6/17 12:55 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from datetime import datetime

from sqlalchemy import func, select

from app.core.handler.logger import PikaLogger
from app.crud import PikaMapper
from app.models import async_session
from app.models.system import PikaOperationLog
from app.utils.decorator import dao


@dao(PikaOperationLog, PikaLogger("PikaOperationDao"))
class PikaOperationDao(PikaMapper):

    @classmethod
    async def count_user_activities(cls, operator, start_time: datetime, end_time: datetime):
        """
        根据开始/结束时间 获取用户的活动日历（操作记录的数量）
        Args:
            operator:
            start_time:
            end_time:

        Returns:

        """
        async with async_session() as session:
            async with session.begin():
                sql = select(PikaOperationLog.operator_date, func.count(PikaOperationLog.id)).where(
                    PikaOperationLog.operator_date.between(start_time, end_time),
                    PikaOperationLog.operator == operator) \
                    .group_by(PikaOperationLog.operator_date).order_by(PikaOperationLog.operator_date)
                data = await session.execute(sql)
                return data.all()
