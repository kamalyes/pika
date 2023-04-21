# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  api_definition.py
@Time    :  2023/4/20 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from sqlalchemy import Column, INT,  UniqueConstraint, ForeignKey, BOOLEAN, DATETIME
from app.core.handler.sqlbin_uuid import BinaryUUID
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models.api_testcase_directory import ApiTestCaseDirectoryModel
from app.models.basic import ApiGBaseModel
from app.models.environment import EnvironmentModel
from app.models.project import ProjectIterModel


class ApiDefinitionModel(ApiGBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_api_definition"
    # 调整联合唯一索引
    __table_args__ = (UniqueConstraint(
        'directory_id', 'name'), {"comment": "接口定义表"})
    directory_id = Column(BinaryUUID, 
                       ForeignKey(ApiTestCaseDirectoryModel.id, ondelete="cascade", onupdate="cascade"),
                       nullable=False, comment='接口定义目录id', )
    environment_id = Column(BinaryUUID, 
                       ForeignKey(EnvironmentModel.id, ondelete="cascade", onupdate="cascade"),
                       comment='环境表id', nullable=False)
    case_total = Column(INT, nullable=False, comment='用例总数')
    version_id = Column(BinaryUUID, 
                       ForeignKey(ProjectIterModel.id, ondelete="cascade", onupdate="cascade"),
                       server_default='master', comment='版本id')
    version_name = Column(BinaryUUID, 
                       ForeignKey(ProjectIterModel.name, ondelete="cascade", onupdate="cascade"),
                       server_default='master', comment='版本名称')
    sync_updated_flag = Column(BOOLEAN, server_default="0", comment="自动同步标识 1:自动同步,0:不同步")
    last_sync_update_date = Column(DATETIME, nullable=False, default=None, comment="最后自动更新时间")

    def __init__(self, directory_id, environment_id, case_total, 
                 version_id, version_name=1, sync_updated_flag=0, last_sync_update_date=None):
        self.directory_id = directory_id
        self.environment_id = environment_id
        self.case_total = case_total
        self.version_id = version_id
        self.version_name = version_name
        self.sync_updated_flag = sync_updated_flag
        self.last_sync_update_date = last_sync_update_date

