# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  notification.py
@Time    :  2022/6/17 12:58 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from datetime import timedelta, datetime
from typing import List

from sqlalchemy import select, and_, or_, update

from app.core.handler.logger import PikaLogger
from app.crud import PikaMapper
from app.enums.MessageEnum import MessageTypeEnum, MessageStateEnum
from app.models import async_session
from app.models.broadcast import PikaBroadcastReadUser
from app.models.notification import PikaNotification
from app.utils.decorator import dao


@dao(PikaNotification, PikaLogger("PikaNotificationDao"))
class PikaNotificationDao(PikaMapper):

    @classmethod
    async def list_messages(cls, msg_type: int, msg_status: int, receiver: int):
        """
        根据消息id和消息类型以及接收人获取消息数据
        :param msg_type:
        :param msg_status:
        :param receiver:
        :return:
        """
        ninety_days = datetime.now() - timedelta(days=90)
        # 1. 当消息类型不为广播类型时，正常查询
        if msg_type == MessageTypeEnum.others:
            ans = await cls.list_record(msg_status=msg_status, receiver=receiver, msg_type=msg_type,
                                        condition=[PikaNotification.create_date > ninety_days])
        else:
            # 否则需要根据是否已读进行查询 只支持90天内数据
            async with async_session() as session:
                # 找到3个月内的消息
                default_condition = [PikaNotification.is_delete == 0, PikaNotification.create_date >= ninety_days]
                if msg_type == MessageTypeEnum.broadcast:
                    conditions = [*default_condition, PikaNotification.msg_type == msg_type]
                else:
                    # 说明是全部消息
                    conditions = [*default_condition,
                                  or_(PikaNotification.msg_type == MessageTypeEnum.broadcast.value,
                                      and_(PikaNotification.msg_type == MessageTypeEnum.others.value,
                                           PikaNotification.receiver == receiver))]
                sql = select(PikaNotification, PikaBroadcastReadUser) \
                    .outerjoin(PikaBroadcastReadUser,
                               and_(PikaNotification.id == PikaBroadcastReadUser.notification_id,
                                    PikaBroadcastReadUser.read_user == receiver)).where(*conditions).order_by(
                    PikaNotification.create_date.desc())
                query = await session.execute(sql)
                result = query.all()
                ans = []
                last_month = datetime.now() - timedelta(days=30)
                for notify, read in result:
                    # 如果非广播类型，直接
                    if notify.msg_type == MessageTypeEnum.others:
                        if notify.msg_status == msg_status:
                            ans.append(notify)
                            continue
                    else:
                        if msg_status == MessageStateEnum.read:
                            if read is not None or notify.updated_date < last_month:
                                ans.append(notify)
                        else:
                            if not read:
                                ans.append(notify)
        return ans

    @classmethod
    async def delete_message(cls, session, msg_id: List[int], receiver: int):
        async with session.begin():
            await session.execute(
                update(PikaNotification).where(
                    PikaNotification.id.in_(msg_id),
                    PikaNotification.receiver == receiver,
                    PikaNotification.deleted_date == 0)) \
                .values(
                delete_date=0,
                update_date=datetime.now(),
                update_emp_no=receiver)
