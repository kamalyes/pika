# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  mock.py
@Time    :  2022/6/18 2:19 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from uuid import uuid4
from sqlalchemy import Column, String, INT, Text, SMALLINT
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.core.handler.sqlbin_uuid import BinaryUUID
from app.models.basic import LargeBaseModel


class MockModel(LargeBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_mock_config"
    __table_args__ = {"comment": "mock配置表"}
    project_id = Column(BinaryUUID,
                        default=uuid4, nullable=False, comment='项目id')
    url = Column(String(ByteSizeEnum.LENGTH_600),
                 index=True, nullable=False, comment='url地址')
    method = Column(String(ByteSizeEnum.LENGTH_16), nullable=False, server_default='GET',
                    comment='请求方式')
    headers = Column(Text, comment='headers')
    match_type = Column(SMALLINT, server_default='0',
                        comment='类型:0:default,1:mockjs,2:faker')
    content_type = Column(String(ByteSizeEnum.LENGTH_30),
                          server_default='application/json')
    response_templates = Column(
        String(ByteSizeEnum.LENGTH_600), default=None, comment="响应模版")
    status_code = Column(INT, server_default='200',
                         comment='http 响应状态码:200（默认）')
