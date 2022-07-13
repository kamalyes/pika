# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  menu.py
@Time    :  2022/5/3 3:52 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import Any, List

from sqlalchemy import select, or_, and_, update

from app.core.handler.asyncsql import AsyncDbSession
from app.models import async_db_session
from app.models.menu import MenuModel


class MenuDao:
    """菜单类"""

    @staticmethod
    async def list_menu(db, request) -> List[Any]:
        """平铺菜单"""
        all_do_sql = select(MenuModel)
        dim_do_sql = select(MenuModel).where(
            or_(MenuModel.id == request.id,
                MenuModel.parent_id == request.parent_id,
                MenuModel.name == request.name,
                MenuModel.title == request.title,
                MenuModel.isHide == request.isHide,
                MenuModel.create_emp_no.like(f"%{request.create_emp_no}%"),
                MenuModel.update_emp_no.like(f"%{request.update_emp_no}%"),
                and_(MenuModel.create_date >= request.create_date,
                     MenuModel.update_date <= request.update_date)
                ))
        do_sql = all_do_sql if request.query_type == 0 else dim_do_sql
        return await AsyncDbSession.query(db, do_sql)

    @staticmethod
    async def save_or_update_menus(request: Any, operator_emp_no, parent_id=0) -> "MenuModel":
        menu_id = request.id
        menu_children = request.children
        menu_name = request.name
        menu_title = request.title
        if len(menu_children) > 0:
            for index in menu_children:
                await MenuDao.save_or_update_menus(request=index, operator_emp_no=operator_emp_no,
                                                   parent_id=index.parent_id)
        async with async_db_session() as session:
            async with session.begin():
                query_by_id_menu = select(MenuModel).where(MenuModel.name == menu_name)
                query_execute = await session.execute(query_by_id_menu)
                ex_menu_info = query_execute.scalars().all()
                if ex_menu_info:
                    if ex_menu_info.title != menu_title:
                        if MenuModel.get_menu_by_name(menu_title):
                            raise ValueError('菜单名已存在！')
                parent_id = parent_id if parent_id != 0 else request.parent_id
                del request.children
                update_role_info_sql = update(MenuModel) \
                    .where(MenuModel.id == menu_id).values(**request.dict(),
                                                           operator=operator_emp_no, parent_id=parent_id)
                await session.execute(update_role_info_sql)
        return ex_menu_info

    @staticmethod
    async def deleted(id: int):
        menu = MenuModel.get(id)
        menus = MenuModel.get_menu_by_parent(id)
        if menus:
            raise ValueError("当前菜单下管理的子菜单，不能删除！")
        menu.delete() if menu else ...
