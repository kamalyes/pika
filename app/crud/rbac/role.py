# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  role.py
@Time    :  2022/5/3 3:52 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import Dict, Any, Text

from sqlalchemy import select, delete, update, and_, or_

from app.core.handler.asyncsql import AsyncDbSession
from app.core.handler.exceres import KeyExistException, SystemException
from app.crud import PikaMdWrapper
from app.models import async_db_session_generator
from app.models.role import RoleModel
from app.models.user import UserModel


@PikaMdWrapper(RoleModel)
class RoleDao:

    @staticmethod
    async def list(db, request: Any) -> Dict[Text, Any]:
        all_do_sql = select(RoleModel)
        dim_do_sql = select(RoleModel).where(
            or_(RoleModel.id == request.id,
                RoleModel.name == request.name,
                RoleModel.status == request.status,
                RoleModel.role_type == request.role_type,
                RoleModel.create_emp_no.like(f"%{request.create_emp_no}%"),
                RoleModel.update_emp_no.like(f"%{request.update_emp_no}%"),
                and_(RoleModel.create_date >= request.create_date,
                     RoleModel.update_date <= request.update_date)
                ))
        do_sql = all_do_sql if request.query_type == 0 else dim_do_sql
        return await AsyncDbSession.query(db, do_sql)

    @classmethod
    async def save_or_update(cls, request: Any, operator) -> RoleModel:
        try:
            id = request.id
            name = request.name
            menus = request.menus
            async with async_db_session_generator() as session:
                async with session.begin():
                    query_ex_sql = select(RoleModel).where(
                        RoleModel.name == f'{name}')
                    query_ex_role_result = await session.execute(query_ex_sql)
                    ex_role_info = query_ex_role_result.scalars().first()
                    if ex_role_info:
                        raise KeyExistException(detail='角色名已存在!')
                    if menus:
                        request.menus = ','.join(list(map(str, menus)))
                    update_role_info_sql = update(RoleModel) \
                        .where(RoleModel.id == id).values(**request.__dict__, operator=operator)
                    await session.execute(update_role_info_sql)
        except ValueError as err:
            err_msg = f"更新/写入失败，错误原因：{err}"
            cls.__log__.error(err_msg)
            raise SystemException(detail=err_msg)

    @classmethod
    async def delete(cls, id: int):
        try:
            async with async_db_session_generator() as session:
                async with session.begin():
                    query_us_role_sql = select(UserModel) \
                        .where(UserModel.roles == id)
                    query_result_ = await session.execute(query_us_role_sql)
                    users = query_result_.scalars().first()
                    if users:
                        raise ValueError('有用户关联了当前角色，不允许删除!')
                    del_role_sql = delete(RoleModel).where(RoleModel.id == id)
                    await session.execute(del_role_sql)
        except Exception as e:
            cls.__log__.error(f"获取数据库配置失败, error: {e}")
            raise SystemException(detail="获取数据库配置失败")
