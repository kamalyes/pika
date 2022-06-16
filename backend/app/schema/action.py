# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  action.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from typing import Optional

from fastapi import Body, Form, Query

from app.enums.bytesize import ByteSizeEnum


class EditRoleActionModel:
    def __init__(
            self,
            role_action_id: Optional[int] = Body(0, title="id"),
            menu_id: Optional[int] = Body(0, title="菜单id"),
            emp_no: Optional[str] = Body(..., title="员工编号", max_length=ByteSizeEnum.LENGTH_20),
            auth_control_id: Optional[str] = Body(..., title="权限控制id", max_length=ByteSizeEnum.LENGTH_255),
            auth_control_desc: Optional[str] = Body(..., title="权限控制说明", max_length=ByteSizeEnum.LENGTH_255),
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
