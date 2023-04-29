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
from sqlalchemy import Column, ForeignKey, String, UniqueConstraint

from app.core.handler.sqlbin_uuid import BinaryUUID
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models.basic import NormBaseModel
from app.models.user import UserModel


class SecurityNominateIssueModel(NormBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_security_issue"
    __table_args__ = (UniqueConstraint("question"), {"comment": "密保问题推荐表"})
    question = Column(String(ByteSizeEnum.LENGTH_255), nullable=False, comment="密保问题")


class PikaSecurityRelIssues(NormBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_user_security"
    __table_args__ = {"comment": "用户密保问题表"}
    uid = Column(
        BinaryUUID,
        ForeignKey(UserModel.id, ondelete="cascade", onupdate="cascade"),
        nullable=False,
        comment="员工编号",
    )
    emp_no = Column(
        String(ByteSizeEnum.LENGTH_20),
        ForeignKey(UserModel.emp_no, ondelete="cascade", onupdate="cascade"),
        comment="员工编号",
        nullable=False,
    )
    question = Column(String(ByteSizeEnum.LENGTH_255), comment="密保问题")
    answers = Column(String(ByteSizeEnum.LENGTH_255), comment="密保答案")
