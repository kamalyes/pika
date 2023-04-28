# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  role.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  角色配置表
"""
from uuid import uuid4
from sqlalchemy import Column, SMALLINT, String
from app.core.handler.sqlbin_uuid import BinaryUUID
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models.basic import NormBaseModel


class RoleModel(NormBaseModel):
    __tablename__ = f'{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_role'
    __table_args__ = {"comment": "角色表"}
    name = Column(String(ByteSizeEnum.LENGTH_64),
                  nullable=True, comment='菜单名称', index=True)
    role_type = Column(SMALLINT, server_default='10', nullable=False,
                       comment='权限类型,10菜单权限,20用户组权限', index=True)
    menus = Column(String(ByteSizeEnum.LENGTH_255),
                   nullable=True, comment='菜单列表', index=True)
    status = Column(SMALLINT, server_default='10',
                    nullable=True, comment='状态 10 启用 20 禁用')

    def __init__(self, id=None, name=None, role_type=None, menus=None, status=None, description=None, operator=None):
        super().__init__(operator=operator)
        self.id = id
        self.name = name
        self.role_type = role_type
        self.menus = menus
        self.status = status
        self.description = description
