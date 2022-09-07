# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  basic.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  公共基础字段
"""

from sqlalchemy import INT, DATETIME, Column, String, BOOLEAN, text

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.models import Base


class LargeBaseModel(Base):
    id = Column(INT, primary_key=True, autoincrement=True, comment="id")
    enabled_flag = Column(BOOLEAN, server_default="1", comment="启用标识 1：启用，0：禁用")
    delete_flag = Column(BOOLEAN, server_default="0", comment="删除标识 1：已删除，0：未删除")
    create_emp_no = Column(String(ByteSizeEnum.LENGTH_16), comment="创建者emp_no")
    update_emp_no = Column(String(ByteSizeEnum.LENGTH_16), comment="修改者emp_no")
    create_date = Column(
        DATETIME,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="创建日期",
    )
    update_date = Column(
        DATETIME,
        nullable=True,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        comment="修改时间",
    )
    delete_date = Column(DATETIME, nullable=True, comment="删除时间")
    description = Column(String(ByteSizeEnum.LENGTH_600), default=None, comment="备注信息")
    __abstract__ = True

    def __init__(self, id=None, operator=None, description=None, delete_date=None, enabled_flag=True,
                 delete_flag=False):
        self.id = id
        self.create_emp_no = operator
        self.update_emp_no = operator
        self.enabled_flag = enabled_flag
        self.delete_flag = delete_flag
        if isinstance(delete_date, DATETIME):
            self.delete_date = delete_date
        self.description = description


class NormBaseModel(Base):
    id = Column(INT, primary_key=True, autoincrement=True, comment="id")
    description = Column(String(ByteSizeEnum.LENGTH_600), default=None, comment="备注信息")
    create_emp_no = Column(String(ByteSizeEnum.LENGTH_16), comment="创建者emp_no")
    update_emp_no = Column(String(ByteSizeEnum.LENGTH_16), comment="修改者emp_no")
    create_date = Column(
        DATETIME,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="创建日期",
    )
    update_date = Column(
        DATETIME,
        nullable=True,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        comment="修改时间",
    )
    __abstract__ = True

    def __init__(self, id=None, description=None, operator=None):
        self.id = id
        self.create_emp_no = operator
        self.update_emp_no = operator
        self.description = description


class TimestampBaseModel(Base):
    create_emp_no = Column(String(ByteSizeEnum.LENGTH_16), comment="创建者emp_no")
    update_emp_no = Column(String(ByteSizeEnum.LENGTH_16), comment="修改者emp_no")
    create_date = Column(
        DATETIME,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="创建日期",
    )
    update_date = Column(
        DATETIME,
        nullable=True,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        comment="修改时间",
    )
    __abstract__ = True

    def __init__(self, id=None, description=None, operator=None):
        self.id = id
        self.create_emp_no = operator
        self.update_emp_no = operator
        self.description = description


class MinBaseModel(Base):
    id = Column(INT, primary_key=True, autoincrement=True, comment="id")
    description = Column(String(ByteSizeEnum.LENGTH_600), default=None, comment="备注信息")
    operator = Column(String(ByteSizeEnum.LENGTH_16), comment="操作者emp_no")
    operator_date = Column(
        DATETIME,
        nullable=True,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="创建日期",
    )
    __abstract__ = True

    def __init__(self, id=0, operator=None, description=None):
        self.id = id
        self.operator = operator
        self.description = description
