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
from uuid import uuid4
from sqlalchemy import Column, DATETIME, String
from app.core.handler.sqlbin_uuid import BinaryUUID
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models import Base


class BroadcastReadUserModel(Base):
    __tablename__ = f'{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_broadcast_read_user'
    __table_args__ = {"comment": "消息已读表"}
    id = Column(BinaryUUID,
                default=uuid4, primary_key=True)
    notification_id = Column(BinaryUUID,
                             default=uuid4, comment="对应消息id", index=True)
    read_user = Column(String(ByteSizeEnum.LENGTH_20),
                       default=uuid4, comment="已读用户")
    read_time = Column(DATETIME, comment="已读时间")

    def __init__(self, notification_id: str, read_user: int):
        self.notification_id = notification_id
        self.read_user = read_user
        self.read_time = datetime.now()
        self.id = None
