# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  api_testcase_directory.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, INT, String, UniqueConstraint
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel
from app.schema.api_testcase_directory import ApiTestCaseDirectorySchema
from app.core.handler.sqlbin_uuid import BinaryUUID

class ApiTestCaseDirectoryModel(LargeBaseModel):
    __tablename__ = f'{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_testcase_directory'
    __table_args__ = (UniqueConstraint('project_id', 'name', 'parent_id'), {"comment": "用例目录表"})
    name = Column(String(ByteSizeEnum.LENGTH_50),
                  nullable=False, comment="目录名称")
    project_id = Column(BinaryUUID,
                        default=uuid4, index=True, comment="项目id")
    parent_id = Column(BinaryUUID, nullable=True, comment="目录上级目录,如果没有则为None")

    def __init__(self, form: ApiTestCaseDirectorySchema, operator):
        super().__init__(operator=operator)
        self.project_id = form.project_id
        self.name = form.name
        self.parent_id = form.parent_id
        self.create_date = datetime.now()
        self.update_date = datetime.now()
        self.operator = operator
        self.update_user = operator
