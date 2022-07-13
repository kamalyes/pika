# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  action.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  访问权限配置表
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysvarEnum import PikaGlobalVarEnum
from app.models.basic import NormBaseModel
from app.models.menu import MenuModel
from app.models.user import UserModel


class ActionControlModel(NormBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.APP_NAME_LOWER}_sys_action"
    __table_args__ = {"comment": "权限控制配置表"}
    action_name = Column(String(ByteSizeEnum.LENGTH_128), nullable=False, comment="权限名称")


class RoleAction(NormBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.APP_NAME_LOWER}_user_action_relation"
    __table_args__ = {"comment": "角色活动表"}
    emp_no = Column(
        String(ByteSizeEnum.LENGTH_20),
        ForeignKey(UserModel.emp_no, ondelete="cascade", onupdate="cascade"),
        comment="员工编号",
        nullable=False,
    )
    menu_id = Column(
        Integer,
        ForeignKey(MenuModel.id, ondelete="cascade", onupdate="cascade"),
        comment="对应menu_config表中的id",
    )
    control_id = Column(
        Integer,
        ForeignKey(ActionControlModel.id, ondelete="cascade", onupdate="cascade"),
        nullable=False,
        comment="权限控制id",
    )
