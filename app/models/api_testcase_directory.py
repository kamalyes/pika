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

from sqlalchemy import Column, INT, String, UniqueConstraint

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysvarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel
from app.schema.api_testcase_directory import ApiTestCaseDirectorySchema


class ApiTestCaseDirectoryModel(LargeBaseModel):
    __tablename__ = f'{PikaGlobalVarEnum.APP_NAME_LOWER}_testcase_directory'
    __table_args__ = (UniqueConstraint('project_id', 'name', 'parent'), {"comment": "用例目录表"})
    name = Column(String(ByteSizeEnum.LENGTH_18), nullable=False, comment="目录名称")
    id = Column(INT, primary_key=True, comment="用例id")
    project_id = Column(INT, index=True, comment="项目id")
    parent = Column(INT, comment="目录上级目录，如果没有则为None")

    def __init__(self, form: ApiTestCaseDirectorySchema, operator):
        super().__init__(operator)
        self.project_id = form.project_id
        self.name = form.name
        self.parent = form.parent
        self.create_date = datetime.now()
        self.update_date = datetime.now()
        self.operator = operator
        self.update_user = operator
