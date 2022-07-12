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

from app.core.handler.logger import PikaLogger
from app.crud import PikaMapper
from app.models import async_session
from app.models.system import OperationLogModel
from app.utils.decorator import dao


@dao(OperationLogModel, PikaLogger("PikaOperationDao"))
class PikaOperationDao(PikaMapper):

    @classmethod
    async def count_user_activities(cls, operator_emp_no, start_time: datetime, end_time: datetime):
        """
        根据开始/结束时间 获取用户的活动日历（操作记录的数量）
        Args:
            operator_emp_no:
            start_time:
            end_time:

        Returns:

        """
        async with async_session() as session:
            async with session.begin():
                sql = select(OperationLogModel.operator_date,
                             func.count(OperationLogModel.id)).where(
                    OperationLogModel.operator_date.between(start_time, end_time),
                    OperationLogModel.operator == operator_emp_no) \
                    .group_by(OperationLogModel.operator_date).order_by(
                    OperationLogModel.operator_date)
                data = await session.execute(sql)
                return data.all()
