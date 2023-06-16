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

from sqlalchemy import Column, ForeignKey, String
from app.models import sync_session
from app.core.handler.sqlbin_uuid import BinaryUUID
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models.basic import NormBaseModel
from app.models.menu import MenuModel
from app.models.user import UserModel


class ActionControlModel(NormBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_sys_action"
    __table_args__ = {"comment": "权限控制配置表"}
    name = Column(String(ByteSizeEnum.LENGTH_128), nullable=False, comment="权限名称")


class RoleAction(NormBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_role_action"
    __table_args__ = {"comment": "角色活动权限表"}
    emp_no = Column(
        String(ByteSizeEnum.LENGTH_20),
        ForeignKey(UserModel.emp_no, ondelete="cascade", onupdate="cascade"),
        comment="员工编号",
        nullable=False,
    )
    menu_id = Column(
        BinaryUUID,
        ForeignKey(MenuModel.id, ondelete="cascade", onupdate="cascade"),
        comment="对应menu_config表中的id",
        nullable=False,
    )
    control_id = Column(
        BinaryUUID,
        ForeignKey(ActionControlModel.id, ondelete="cascade", onupdate="cascade"),
        nullable=False,
        comment="权限控制id",
    )


def create_initial_actions():
    actions = [
        {"name": "admin"},
        {"name": "user"},
        # 可根据需要添加更多的权限记录
    ]

    db = sync_session()
    try:
        for action_data in actions:
            action_data = ActionControlModel(**action_data)
            db.add(action_data)
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()
