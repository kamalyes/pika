# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  access.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from typing import Optional

from fastapi import Body, Form, Query
from hutools.time import Moment

from app.enums.bytesize import ByteSizeEnum


class EditMenuModel:
    def __init__(
            self,
            son_id: int = Body(None, title="子菜单id"),
            title: str = Body(..., title="菜单名称", max_length=ByteSizeEnum.LENGTH_70),
            icon: str = Body(..., title="菜单图标", max_length=ByteSizeEnum.LENGTH_70),
            path: str = Body(..., title="路由地址", max_length=ByteSizeEnum.LENGTH_255),
            type: str = Body(..., title="菜单类型：用于区分模块、目录、菜单、按钮", max_length=ByteSizeEnum.LENGTH_20),
            component: str = Body(..., title="菜单对应的组件路径", max_length=ByteSizeEnum.LENGTH_255),
            hidden: int = Body(..., title="是否隐藏此菜单"),
            parent_id: int = Body(None, title="父菜单id"),
            description: str = Body(None, title="备注信息", max_length=ByteSizeEnum.LENGTH_255),
            is_enabled: int = Body(1, title="禁用/启用 1：启用、0：禁用"),
    ):
        self.son_id = son_id
        self.title = title
        self.icon = icon
        self.path = path
        self.type = type
        self.component = component
        self.hidden = hidden
        self.parent_id = parent_id
        self.description = description
        self.is_enabled = is_enabled


class DelMenuModel:
    def __init__(self, menu_ids: Optional[list] = Form(None, title="菜单id")):
        self.menu_ids = menu_ids


class QueryMenuModel:
    def __init__(
            self,
            query_type: Optional[str] = Query(None, title="类型"),
            menu_title: Optional[int] = Query(None, title="菜单名称"),
            create_emp_no: Optional[str] = Query(None, title="创建者员工编号", max_length=ByteSizeEnum.LENGTH_20),
            update_emp_no: Optional[str] = Query(None, title="修改者员工编号", max_length=ByteSizeEnum.LENGTH_20),
            create_time: Optional[str] = Query(Moment.skew_date(days=-1), title="创建时间"),
            update_time: Optional[str] = Query(Moment.skew_date(hours=1), title="更新时间"),
            page_index: Optional[int] = Query(1, title="分页起始值"),
            page_size: Optional[int] = Query(10, title="分页量"),
    ):
        self.query_type = query_type
        self.menu_title = menu_title
        self.update_emp_no = update_emp_no
        self.create_emp_no = create_emp_no
        self.create_time = create_time
        self.update_time = update_time
        self.page_index = page_index
        self.page_size = page_size


class EditRoleModel:
    def __init__(
            self,
            role_id: Optional[int] = Body(0, title="角色id"),
            role_name: str = Body(..., title="角色名称", min_length=2, max_length=ByteSizeEnum.LENGTH_255),
            description: str = Body(None, title="备注信息", max_length=ByteSizeEnum.LENGTH_255),
            is_enabled: int = Body(1, title="禁用/启用 1：启用、0：禁用"),
            create_emp_no: Optional[str] = Query(None, title="创建者员工编号", max_length=ByteSizeEnum.LENGTH_20),
            update_emp_no: Optional[str] = Query(
                None, title="修改者员工编号", max_length=ByteSizeEnum.LENGTH_20
            ),
    ):
        self.role_id = role_id
        self.role_name = role_name
        self.description = description
        self.is_enabled = is_enabled
        self.create_emp_no = create_emp_no
        self.update_emp_no = update_emp_no


class DelRoleModel:
    def __init__(self, role_ids: Optional[list] = Form(None, title="菜单id")):
        self.role_ids = role_ids


class EditRoleRelModel:
    def __init__(
            self,
            role_rel_id: Optional[int] = Body(0, title="角色应用id"),
            role_id: Optional[int] = Body(0, title="角色id"),
            emp_no: str = Body(..., title="员工编号", max_length=ByteSizeEnum.LENGTH_20),
            description: str = Body(None, title="备注信息", max_length=ByteSizeEnum.LENGTH_255),
            create_emp_no: Optional[str] = Query(None, title="创建者员工编号", max_length=ByteSizeEnum.LENGTH_20),
            update_emp_no: Optional[str] = Query(None, title="修改者员工编号", max_length=ByteSizeEnum.LENGTH_20),
    ):
        self.role_rel_id = role_rel_id
        self.role_id = role_id
        self.emp_no = emp_no
        self.description = description
        self.create_emp_no = create_emp_no
        self.update_emp_no = update_emp_no


class DelRoleRelModel:
    def __init__(self, role_rel_ids: Optional[list] = Form(None, title="角色应用id")):
        self.role_rel_ids = role_rel_ids


class EditRoleActionModel:
    def __init__(
            self,
            role_action_id: Optional[int] = Body(0, title="id"),
            menu_id: Optional[int] = Body(0, title="菜单id"),
            emp_no: str = Body(..., title="员工编号", max_length=ByteSizeEnum.LENGTH_20),
            auth_control_id: str = Body(..., title="权限控制id", max_length=ByteSizeEnum.LENGTH_255),
            auth_control_desc: str = Body(..., title="权限控制说明", max_length=ByteSizeEnum.LENGTH_255),
            create_emp_no: Optional[str] = Query(None, title="创建者员工编号", max_length=ByteSizeEnum.LENGTH_20),
            update_emp_no: Optional[str] = Query(None, title="修改者员工编号", max_length=ByteSizeEnum.LENGTH_20),
    ):
        self.role_action_id = role_action_id
        self.menu_id = menu_id
        self.emp_no = emp_no
        self.auth_control_id = auth_control_id
        self.auth_control_desc = auth_control_desc
        self.create_emp_no = create_emp_no
        self.update_emp_no = update_emp_no


class DelRoleActionModel:
    def __init__(self, role_action_ids: Optional[list] = Form(None, title="活动id")):
        self.role_action_ids = role_action_ids
