# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  python_constructor.py
@Time    :  2022/6/10 6:53 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from app.core.constructor.constructor import ConstructorAbstract
from app.core.handler.jsonres import PikaJsonEncoder
from app.models.constructor import ConstructorModel
from awaits.awaitable import awaitable


class PythonConstructor(ConstructorAbstract, PikaJsonEncoder):
    @classmethod
    @awaitable
    def run(cls, executor, index, path, params, constructor: ConstructorModel, **kwargs):
        try:
            constructor_type_ = cls.get_name(constructor)
            executor.append(f"当前路径: {path}, 第{index + 1}条{constructor_type_}")
            script = cls.safe_json_loads(constructor.constructor_json)
            command = script["command"]
            executor.append(f"当前{constructor_type_}类型为python脚本\n{command}")
            loc = {}
            exec(command, loc)
            py_data = loc.get(constructor.value)
            if py_data is None:
                executor.append(f"当前{constructor_type_}未返回任何值")
                return
            params[constructor.value] = py_data
            executor.append(f"当前{constructor_type_}返回变量: {constructor.value}\n返回值:\n {py_data}\n")
            return py_data
        except Exception as e:
            raise Exception(f"{path}->{constructor.name} 第{index + 1}个{constructor_type_}执行失败: {e}")
