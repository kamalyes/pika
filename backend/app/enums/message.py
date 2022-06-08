# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  notice.py
@Time    :  2022/5/1 8:21 PM
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


class MessageStateEnum(IntEnum):
    """
    消息状态枚举类
    """

    UNREAD = 1  # 未读
    READ = 2  # 已读


class MessageTypeEnum(IntEnum):
    """
    消息类型枚举类
    """

    ALL = 0  # 全部消息
    BROADCAST = 1  # 广播消息
    OTHERS = 2  # 其他消息
