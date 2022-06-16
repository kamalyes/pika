# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  action.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  访问权限配置表
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey

from app.enums.bytesize import ByteSizeEnum
from app.enums.sysvar import GlobalVarEnum
from app.models.basic import PikaNormBase
from app.models.menu import Menu
from app.models.user import User


class ActionControl(PikaNormBase):
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
