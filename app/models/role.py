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
from sqlalchemy import Column, Integer, String, BOOLEAN, UniqueConstraint
from sqlalchemy import ForeignKey

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysvarEnum import PikaGlobalVarEnum
from app.models.basic import NormBaseModel
from app.models.user import SysUserModel


class SysRoleModel(NormBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.APP_NAME_LOWER}_sys_role"
    __table_args__ = (UniqueConstraint("name"), {"comment": "角色配置表"})
    is_usable = Column(BOOLEAN, server_default="1", comment="是否可用 1：启用，0：禁用")
    name = Column(String(ByteSizeEnum.LENGTH_255), nullable=False, comment="角色名称")
    role_type = Column(Integer, nullable=False, comment='角色权限类型，10菜单权限，20用户组权限', index=True,
                       default=10)
    menus_id = Column(String(ByteSizeEnum.LENGTH_64), nullable=True, comment='菜单id', index=True)


class SysRoleRelModel(NormBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.APP_NAME_LOWER}_sys_role_relation"
    __table_args__ = {"comment": "角色应用表"}
    role_id = Column(
        Integer,
        ForeignKey(SysRoleModel.id, ondelete="cascade", onupdate="cascade"),
        nullable=False,
        comment="角色id",
    )
    emp_no = Column(
        String(ByteSizeEnum.LENGTH_20),
        ForeignKey(SysUserModel.emp_no, ondelete="cascade", onupdate="cascade"),
        comment="员工编号",
    )
    rel_type = Column(Integer, server_default="0", comment="应用类型 1：上级关联绑定，2：下级用户申请")
    is_verify = Column(Integer, server_default="0", comment="审核状态 0：未审核， 1：初审通过，3：终审通过，4：驳回审核(不通过)")
