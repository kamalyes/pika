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

from uuid import uuid4
from sqlalchemy import Column, Integer, String, UniqueConstraint
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models.basic import NormBaseModel
from app.core.handler.sqlbin_uuid import BinaryUUID


class OrganizationModel(NormBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_organization"
    __table_args__ = (UniqueConstraint('name', 'parent_id'), {"comment": "组织机构表"})
    name = Column(String(ByteSizeEnum.LENGTH_255), nullable=False, comment="用户组名称")
    parent_id = Column(BinaryUUID, default=uuid4, comment="父序号")
    sort_id = Column(Integer, server_default="0", comment="排序id")

    def __init__(self, name, parent_id, sort_id, operator, id=None, description=None):
        super().__init__(id=id, operator=operator,  description=description)
        self.name = name
        self.parent_id = parent_id
        self.sort_id = sort_id
