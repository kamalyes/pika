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
from app.core.handler.exceres import KeyExistException, KeyUndefinedException
from app.models import async_db_session_generator
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
    async def insert_menu(request: Any, operator: str, is_parent=False) -> MenuModel:
        menu_id = request.id
        menu_name = request.name
        menu_title = request.title
        menu_parent_id = request.parent_id
        try:
            delattr(request, "children")
        except AttributeError as e:
            pass
        if menu_parent_id == 0 and not is_parent:
            raise KeyUndefinedException(detail='父菜单id不存在！')
        async with async_db_session_generator() as session:
            async with session.begin():
                query_by_id_sql = select(MenuModel.id, MenuModel.title, MenuModel.name, MenuModel.parent_id).where(
                    or_(MenuModel.id == menu_id,
                        MenuModel.name == menu_name,
                        MenuModel.title == menu_title))
                query_id_execute = await session.execute(query_by_id_sql)
                ex_menu_info = query_id_execute.all()
                ex_parent_ids = []
                for ex_menu_index in ex_menu_info:
                    ex_parent_ids.append(ex_menu_index.id)
                    if menu_parent_id not in ex_parent_ids and not is_parent:
                        raise KeyExistException(detail='父菜单id不存在！')
                    if menu_id != ex_menu_index.id:
                        if ex_menu_index.name == menu_name:
                            raise KeyExistException(detail='菜单名已存在！')
                        elif ex_menu_index.title == menu_title:
                            raise KeyExistException(detail="title已存在！")
                        result = MenuModel(**request.dict(), operator=operator)
                        session.add(result)
                        await session.flush()
                    else:
                        delattr(request, "id")
                        update_sql = update(MenuModel).where(MenuModel.id == menu_id). \
                            values(**request.dict(),
                                   create_emp_no=str(operator))
                        await session.execute(update_sql)

    @staticmethod
    async def save_or_update_menus(request: Any, operator: str):
        menu_parent_id = request.id
        try:
            menu_children = request.children
        except AttributeError:
            menu_children = []
        if menu_parent_id in (0, None) and len(menu_children) > 0:
            raise ValueError(f"数据格式错误、有children、但父id=={menu_parent_id}")
        await MenuDao.insert_menu(request, operator, True)
        if len(menu_children) > 0:
            for index in menu_children:
                await MenuDao.insert_menu(index, operator)

    @staticmethod
    async def deleted(id: int):
        menu = MenuModel.get(id)
        menus = MenuModel.get_menu_by_parent(id)
        if menus:
            raise ValueError("当前菜单下管理的子菜单，不能删除！")
        menu.delete() if menu else ...
