# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  organization.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  组织
"""

from sqlalchemy import Column, Integer, String

from app.enums.bytesize import ByteSizeEnum
from app.enums.sysvar import PikaGlobalVarEnum
from app.models.basic import PikaLargeBase, PikaNormBase


class PikaUserGroup(PikaLargeBase):
    __tablename__ = f"{PikaGlobalVarEnum.APP_NAME_LOWER}_user_group"
    __table_args__ = {"comment": "用户组表"}
    name = Column(String(ByteSizeEnum.LENGTH_255), nullable=False, comment="用户组名称")
    parent_id = Column(Integer, server_default="0", comment="父序号")


class PikaDept(PikaLargeBase):
    __tablename__ = f"{PikaGlobalVarEnum.APP_NAME_LOWER}_department"
    __table_args__ = {"comment": "部门表"}
    name = Column(String(ByteSizeEnum.LENGTH_255), nullable=False, comment="部门名称")
    group_id = Column(Integer, nullable=False, comment="用户组id")


class PikaDeptRel(PikaNormBase):
    __tablename__ = f"{PikaGlobalVarEnum.APP_NAME_LOWER}_department_relation"
    __table_args__ = {"comment": "部门应用表"}
    dept_id = Column(Integer, nullable=False, comment="部门id")
    emp_no = Column(String(ByteSizeEnum.LENGTH_20), comment="员工编号", nullable=False)
