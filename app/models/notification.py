# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  notification.py
@Time    :  2021/10/18 2:28 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  消息通知表
"""
from sqlalchemy import SMALLINT, Column, VARCHAR, INT

from app.enums.SysvarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel


class NotificationModel(LargeBaseModel):
    __tablename__ = f'{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_notification'
    __table_args__ = {"comment": "消息通知表"}
    msg_type = Column(SMALLINT, comment="消息类型 1: 系统消息 2: 其他消息")
    msg_title = Column(VARCHAR(32), comment="消息标题", nullable=False)
    msg_content = Column(VARCHAR(200), comment="消息内容", nullable=True)
    msg_link = Column(VARCHAR(128), comment="消息链接")
    msg_status = Column(SMALLINT, comment="消息状态 1: 未读 2: 已读")
    sender = Column(INT, comment="消息发送人, 0则是CPU 非0则是其他用户")
    receiver = Column(INT, comment="消息接收人, 系统消息则该字段为空")

    def __init__(self, msg_type, msg_title, msg_content, sender, receiver, update_emp_no,
                 msg_link=None, msg_status=0):
        super().__init__(update_emp_no)
        self.msg_type = msg_type
        self.msg_title = msg_title
        self.receiver = receiver
        self.msg_content = msg_content
        self.sender = sender
        self.msg_link = msg_link
        self.msg_status = msg_status
