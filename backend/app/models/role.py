# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  role.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  角色配置表
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey

from app.enums.bytesize import ByteSizeEnum
from app.enums.sysvar import GlobalVarEnum
from app.models.basic import PikaLargeBase, PikaNormBase
from app.models.user import User


class Role(PikaLargeBase):
    __tablename__ = f"{GlobalVarEnum.APP_NAME_LOWER}_user_role"
    __table_args__ = {"comment": "角色配置表"}
    name = Column(String(ByteSizeEnum.LENGTH_255), nullable=False, comment="角色名称")
    role_type = Column(Integer, nullable=False, comment='角色权限类型，10菜单权限，20用户组权限', index=True, default=10)
    menus_id = Column(String(64), nullable=True, comment='菜单id', index=True)


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
