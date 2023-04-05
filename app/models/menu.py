# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  menu.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from uuid import uuid4
from sqlalchemy import Column, Integer, String
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.core.handler.sqlbin_uuid import BinaryUUID
from app.models.basic import LargeBaseModel


class MenuModel(LargeBaseModel):
    __tablename__ = f'{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_menu'
    __table_args__ = {"comment": "菜单表"}
    path = Column(String(ByteSizeEnum.LENGTH_255),
                  nullable=True, comment='菜单路径')
    name = Column(String(ByteSizeEnum.LENGTH_255),
                  nullable=True, comment='菜单名称', index=True)
    component = Column(String(ByteSizeEnum.LENGTH_255),
                       nullable=True, comment='组件路径')
    title = Column(String(ByteSizeEnum.LENGTH_255),
                   nullable=True, comment='title', index=True)
    is_link = Column(Integer, nullable=True,
                     comment='开启外链条件,`1、is_link: true 2、链接地址不为空（meta.is_link） 3、is_iframe: false`')
    is_hide = Column(Integer, nullable=True, default=False,
                     comment='菜单是否隐藏（菜单不显示在界面,但可以进行跳转）')
    is_keepalive = Column(Integer, nullable=True,
                          default=True, comment='菜单是否缓存')
    is_affix = Column(Integer, nullable=True, default=False, comment='固定标签')
    is_iframe = Column(Integer, nullable=True, default=False, comment='是否内嵌')
    roles = Column(String(ByteSizeEnum.LENGTH_64),
                   nullable=True, default=False, comment='权限')
    icon = Column(String(ByteSizeEnum.LENGTH_64),
                  nullable=True, comment='icon', index=True)
    parent_id = Column(BinaryUUID,
                       default=uuid4, nullable=True, comment='父级菜单id')
    redirect = Column(String(ByteSizeEnum.LENGTH_255),
                      nullable=True, comment='重定向路由')
    sort = Column(Integer, nullable=True, comment='排序')
    menu_type = Column(Integer, nullable=True, comment='菜单类型')
    active_menu = Column(String(ByteSizeEnum.LENGTH_255),
                         nullable=True, comment='显示页签')

    def __init__(self, id, path, name, component, title, is_link, is_hide, is_keepalive, is_affix, is_iframe,
                 roles, icon, parent_id, redirect, sort, menu_type, active_menu, enabled_flag, operator):
        super().__init__(id=id, operator=operator, enabled_flag=enabled_flag)
        self.path = path
        self.name = name
        self.component = component
        self.title = title
        self.is_link = is_link
        self.is_hide = is_hide
        self.is_keepalive = is_keepalive
        self.is_affix = is_affix
        self.is_iframe = is_iframe
        self.roles = roles
        self.icon = icon
        self.parent_id = parent_id
        self.redirect = redirect
        self.sort = sort
        self.menu_type = menu_type
        self.active_menu = active_menu
