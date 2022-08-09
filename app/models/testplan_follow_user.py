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
from sqlalchemy import INT, Column, UniqueConstraint

from app.enums.SysvarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel


class ApiTestPlanFollowUserRelModel(LargeBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.APP_NAME_LOWER}_testplan_follow_user_rel"
    __table_args__ = (UniqueConstraint('emp_no', 'plan_id'), {"comment": "测试计划关注用户表"})

    emp_no = Column(INT, nullable=False, comment="员工编号")
    plan_id = Column(INT, nullable=False, comment="计划id")

    def __init__(self, plan_id, emp_no):
        super().__init__(operator=emp_no)
        self.emp_no = emp_no
        self.plan_id = plan_id
