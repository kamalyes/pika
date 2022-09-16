# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  dept.py
@Time    :  2022/9/15 11:01
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from sqlalchemy import Column, Integer, String, UniqueConstraint

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysvarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel, NormBaseModel


class DepartmentModel(LargeBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_department"
    __table_args__ = (UniqueConstraint('name', 'organization_id'), {"comment": "部门表"})
    name = Column(String(ByteSizeEnum.LENGTH_255), nullable=False, comment="部门名称")
    organization_id = Column(Integer, nullable=False, comment="组织id")
    sort_id = Column(Integer, server_default="0", comment="排序id")

    def __init__(self, name, organization_id, sort_id, operator, id=None):
        super().__init__(id=id, operator=operator)
        self.name = name
        self.organization_id = organization_id
        self.sort_id = sort_id


class DepartmentRelModel(NormBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_department_relation"
    __table_args__ = {"comment": "部门应用表"}
    department_id = Column(Integer, nullable=False, comment="部门id")
    emp_no = Column(String(ByteSizeEnum.LENGTH_20), comment="员工编号", nullable=False)

    def __init__(self, name, department_id, operator, emp_no, id=None):
        super().__init__(id=id, operator=operator)
        self.name = name
        self.department_id = department_id
        self.emp_no = emp_no
