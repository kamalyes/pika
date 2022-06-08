# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  basic.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  公共基础字段
"""

from datetime import datetime

from sqlalchemy import INT, DATETIME, Column, String, BOOLEAN, text

from app.enums.bytesize import ByteSizeEnum
from app.models import Base


class PikaLargeBase(Base):
    id = Column(INT, primary_key=True, autoincrement=True, comment="id")
    is_usable = Column(BOOLEAN, server_default="1", comment="是否可用 1：启用，0：禁用")
    is_delete = Column(BOOLEAN, server_default="0", comment="是否被删除 1：已删除，0：未删除")
    create_emp_no = Column(INT, comment="创建者用户id")
    update_emp_no = Column(INT, comment="修改者用户id")
    create_time = Column(
        DATETIME,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="创建时间",
    )
    update_time = Column(
        DATETIME,
        nullable=True,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        comment="修改时间",
    )
    delete_time = Column(DATETIME, nullable=True, comment="删除时间")
    description = Column(String(ByteSizeEnum.LENGTH_600), default=None, comment="备注信息")
    __abstract__ = True
    __table_args__ = {}
    __alias__ = dict(name="名称")
    __show__ = 1

    def __init__(self, user, description=None, is_usable=1, is_delete=0, id=0):
        self.id = id
        self.is_usable = is_usable
        self.is_delete = is_delete
        self.create_user = user
        self.update_user = user
        self.delete_time = datetime.now()
        self.description = description


class PikaNormBase(Base):
    id = Column(INT, primary_key=True, autoincrement=True, comment="id")
    create_time = Column(
        DATETIME,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="创建时间",
    )
    update_time = Column(
        DATETIME,
        nullable=True,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        comment="修改时间",
    )
    __abstract__ = True
    __table_args__ = {}
    __alias__ = dict(name="名称")
    __show__ = 1

    def __init__(self, id=0):
        self.id = id
