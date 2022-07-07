# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  iteration.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  迭代
"""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.enums.bytesize import ByteSizeEnum
from app.enums.sysvar import PikaGlobalVarEnum
from app.models.basic import PikaLargeBase, PikaNormBase


class PikaIterate(PikaLargeBase):
    __tablename__ = f"{PikaGlobalVarEnum.APP_NAME_LOWER}_iterate"
    __table_args__ = {"comment": "迭代表"}
    project_id = Column(Integer, nullable=False, comment="被关联的项目id")
    project_name = Column(String(ByteSizeEnum.LENGTH_30), comment="迭代名称", nullable=False)
    is_private = Column(Integer, server_default="0", comment="是否私有 1：私有 0：公开", nullable=False)


class PikaIterateRel(PikaNormBase):
    __tablename__ = f"{PikaGlobalVarEnum.APP_NAME_LOWER}_iterate_relation"
    __table_args__ = {"comment": "用户迭代关联表"}
    iterate_id = Column(Integer, comment="迭代id")
    emp_no = Column(String(ByteSizeEnum.LENGTH_30), comment="员工编号", nullable=False)
    description = Column(String(ByteSizeEnum.LENGTH_255), comment="描述", nullable=False)
