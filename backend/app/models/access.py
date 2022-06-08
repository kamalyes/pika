# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  access.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  角色/菜单配置表
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey

from app.enums.bytesize import ByteSizeEnum
from app.enums.sysvar import GlobalVarEnum
from app.models.basic import PikaLargeBase, PikaNormBase
from app.models.user import User


class Menu(PikaLargeBase):
    __tablename__ = f"{GlobalVarEnum.APP_NAME_LOWER}_user_menu"
    __table_args__ = {"comment": "菜单配置表"}
    title = Column(String(ByteSizeEnum.LENGTH_70), nullable=False, comment="菜单名称")
    icon = Column(String(ByteSizeEnum.LENGTH_70), nullable=False, comment="菜单图标")
    path = Column(String(ByteSizeEnum.LENGTH_255), nullable=False, comment="路由地址")
    type = Column(Integer, server_default="1", nullable=False, comment="菜单类型：用于区分模块、1：菜单、2：按钮")
    parent_id = Column(Integer, server_default="0", comment="父序号")
    component_path = Column(String(ByteSizeEnum.LENGTH_255), nullable=False, comment="菜单对应的组件路径")
    is_hidden = Column(Integer, server_default="0", nullable=False, comment="是否隐藏此菜单")


class Role(PikaLargeBase):
    __tablename__ = f"{GlobalVarEnum.APP_NAME_LOWER}_user_role"
    __table_args__ = {"comment": "角色配置表"}
    role_name = Column(String(ByteSizeEnum.LENGTH_255), nullable=False, comment="角色名称")


class RoleRel(PikaNormBase):
    __tablename__ = f"{GlobalVarEnum.APP_NAME_LOWER}_user_role_relation"
    __table_args__ = {"comment": "角色应用表"}
    role_id = Column(
        Integer,
        ForeignKey(Role.id, ondelete="cascade", onupdate="cascade"),
        nullable=False,
        comment="角色id",
    )
    emp_no = Column(
        String(ByteSizeEnum.LENGTH_20),
        ForeignKey(User.emp_no, ondelete="cascade", onupdate="cascade"),
        comment="员工编号",
    )


class ActionControl(PikaLargeBase):
    __tablename__ = f"{GlobalVarEnum.APP_NAME_LOWER}_user_action"
    __table_args__ = {"comment": "权限控制配置表"}
    action_name = Column(String(ByteSizeEnum.LENGTH_128), nullable=False, comment="权限名称")


class RoleAction(PikaNormBase):
    __tablename__ = f"{GlobalVarEnum.APP_NAME_LOWER}_user_action_relation"
    __table_args__ = {"comment": "角色活动表"}
    emp_no = Column(
        String(ByteSizeEnum.LENGTH_20),
        ForeignKey(User.emp_no, ondelete="cascade", onupdate="cascade"),
        comment="员工编号",
        nullable=False,
    )
    menu_id = Column(
        Integer,
        ForeignKey(Menu.id, ondelete="cascade", onupdate="cascade"),
        comment="对应menu_config表中的id",
    )
    control_id = Column(
        Integer,
        ForeignKey(ActionControl.id, ondelete="cascade", onupdate="cascade"),
        nullable=False,
        comment="权限控制id",
    )
