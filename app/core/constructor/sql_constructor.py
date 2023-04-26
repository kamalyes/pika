# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  sql_constructor.py
@Time    :  2022/6/10 6:53 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import json
from app.core.constructor.constructor import ConstructorAbstract
from app.core.handler.exceres import SystemException
from app.core.handler.jsonres import PikaJsonEncoder
from app.crud.itstem.database import DbConfigDao
from app.models.constructor import ConstructorModel


class SqlConstructor(ConstructorAbstract, PikaJsonEncoder):

    @classmethod
    async def run(cls, executor, env, index, path, params, constructor: ConstructorModel, **kwargs):
        try:
            constructor_type_ = cls.get_name(constructor)
            executor.append(f"当前路径: {path}, 第{index + 1}条{constructor_type_}")
            data = cls.safe_loads(constructor.constructor_json)
            database = data.get("database")
            sql = data.get("sql")
            executor.append(f"当前{constructor_type_}类型为sql, 数据库名: {database}\nsql: {sql}\n")
            sql_data = await DbConfigDao.execute_sql(env, database, sql)
            params[constructor.value] = sql_data
            executor.append(f"当前{constructor_type_}返回变量: {constructor.value}\n返回值:\n {sql_data}\n")
        except Exception as e:
            raise SystemException(detail=f"{path}->{constructor.name} 第{index + 1}个{constructor_type_}执行失败: {e}")
