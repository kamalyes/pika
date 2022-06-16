# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  kerberos.py
@Time    :  2022/5/2 10:27 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from sqlalchemy import Column, INT, String, UniqueConstraint
from sqlalchemy import ForeignKey

from app.enums.bytesize import ByteSizeEnum
from app.enums.sysvar import GlobalVarEnum
from app.models.basic import PikaNormBase
from app.models.user import User


class SecurityNominateIssue(PikaNormBase):
    __tablename__ = f"{GlobalVarEnum.APP_NAME_LOWER}_security_issue"
    __table_args__ = (UniqueConstraint("question"), {"comment": "密保问题推荐表"})
    question = Column(String(ByteSizeEnum.LENGTH_255), nullable=False, comment="密保问题")


class SecurityRelIssues(PikaNormBase):
    __tablename__ = f"{GlobalVarEnum.APP_NAME_LOWER}_user_security_relation"
    __table_args__ = {"comment": "用户密保问题表"}
    uid = Column(
        INT,
        ForeignKey(User.id, ondelete="cascade", onupdate="cascade"),
        nullable=False,
        comment="员工编号",
    )
    emp_no = Column(
        String(ByteSizeEnum.LENGTH_20),
        ForeignKey(User.emp_no, ondelete="cascade", onupdate="cascade"),
        comment="员工编号",
        nullable=False,
    )
    question = Column(String(ByteSizeEnum.LENGTH_255), comment="密保问题")
    answers = Column(String(ByteSizeEnum.LENGTH_255), comment="密保答案")
