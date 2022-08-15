# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  project.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  项目
"""

from sqlalchemy import INT, Column, String, BOOLEAN, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, backref

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysvarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel
from app.models.user import UserModel


class ProjectModel(LargeBaseModel):
    __tablename__ = f'{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_project'
    __table_args__ = (UniqueConstraint('name', 'delete_date'), {"comment": "项目管理表"})
    name = Column(String(ByteSizeEnum.LENGTH_16), unique=True, index=True, comment="项目名称")
    owner = Column(
        String(ByteSizeEnum.LENGTH_16),
        ForeignKey(UserModel.emp_no, ondelete="cascade", onupdate="cascade"),
        comment="项目所有者",
        nullable=False,
    )
    app = Column(String(ByteSizeEnum.LENGTH_32), index=True, comment="项目所属应用")
    private = Column(BOOLEAN, default=False, comment="是否私有")
    description = Column(String(ByteSizeEnum.LENGTH_200), comment="项目描述")
    avatar = Column(String(ByteSizeEnum.LENGTH_128), nullable=True, comment="项目头像")
    dingtalk_url = Column(String(ByteSizeEnum.LENGTH_128), nullable=True, comment="钉钉通知url")
    qy_wx_url = Column(String(ByteSizeEnum.LENGTH_128), nullable=True, comment="企微通知url")
    relationship(UserModel, backref=backref("children", cascade="all, delete"))

    def __init__(self, name, app, owner, operator, description="",
                 private=False, avatar=None, dingtalk_url='', qy_wx_url=''):
        super().__init__(operator)
        self.name = name
        self.app = app
        self.owner = owner
        self.private = private
        self.description = description
        self.avatar = avatar
        self.dingtalk_url = dingtalk_url
        self.qy_wx_url = qy_wx_url


class ProjectRoleModel(LargeBaseModel):
    __tablename__ = f'{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_project_role'
    __table_args__ = {"comment": "项目人员关联表"}
    emp_no = Column(
        String(ByteSizeEnum.LENGTH_16),
        ForeignKey(UserModel.emp_no, ondelete="cascade", onupdate="cascade"),
        nullable=False,
        comment="项目成员编号（用户编号）")
    project_id = Column(INT, index=True, comment="项目id")
    project_role = Column(INT, index=True, comment="角色")
    relationship(UserModel, backref=backref("children", cascade="all, delete"))

    def __init__(self, emp_no, project_id, project_role, operator):
        super().__init__(operator)
        self.emp_no = emp_no
        self.project_id = project_id
        self.project_role = project_role
