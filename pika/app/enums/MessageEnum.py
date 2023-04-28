# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  MessageEnum.py
@Time    :  2022/7/6 16:39
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from enum import IntEnum


class WebSocketMessageEnum(IntEnum):
    # 消息数量
    COUNT = 0
    # 桌面通知
    DESKTOP = 1
    # 录制数据
    RECORD = 2


class MessageStateEnum(IntEnum):
    """
    消息状态枚举类
    """
    unread = 1  # 未读
    read = 2  # 已读


class MessageTypeEnum(IntEnum):
    """
    消息类型枚举类
    """
    all = 0  # 全部消息
    broadcast = 1  # 广播消息
    others = 2  # 其他消息
