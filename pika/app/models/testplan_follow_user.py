# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  testplan_follow_user.py
@Time    :  2021/10/18 2:28 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String, UniqueConstraint

from app.core.handler.sqlbin_uuid import BinaryUUID
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel
from app.models.user import UserModel
from app.models.api_testplan import ApiTestPlanModel


class ApiTestPlanFollowUserRelModel(LargeBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_testplan_follow_user_rel"
    __table_args__ = (UniqueConstraint("emp_no", "plan_id"), {"comment": "测试计划关注用户表"})
    emp_no = Column(
        String(ByteSizeEnum.LENGTH_20),
        ForeignKey(UserModel.emp_no, ondelete="cascade", onupdate="cascade"),
        comment="员工编号",
        nullable=False,
    )
    plan_id = Column(
        String(ByteSizeEnum.LENGTH_20),
        ForeignKey(ApiTestPlanModel.id, ondelete="cascade", onupdate="cascade"),
        comment="计划id",
        nullable=False,
    )

    def __init__(self, plan_id, emp_no):
        super().__init__(operator=emp_no)
        self.emp_no = emp_no
        self.plan_id = plan_id
