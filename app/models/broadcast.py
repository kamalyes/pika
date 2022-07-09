# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  broadcast.py
@Time    :  2022/6/17 12:58 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from datetime import datetime

from sqlalchemy import Column, INT, DATETIME, BIGINT

from app.enums.SysvarEnum import PikaGlobalVarEnum
from app.models import Base


class BroadcastReadUserModel(Base):
    __tablename__ = f'{PikaGlobalVarEnum.APP_NAME_LOWER}_broadcast_read_user'
    id = Column(BIGINT, primary_key=True)
    notification_id = Column(INT, comment="对应消息id", index=True)
    read_user = Column(INT, comment="已读用户id")
    read_time = Column(DATETIME, comment="已读时间")

    def __init__(self, notification_id: int, read_user: int):
        self.notification_id = notification_id
        self.read_user = read_user
        self.read_time = datetime.now()
        self.id = None
