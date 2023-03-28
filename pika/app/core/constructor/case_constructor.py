# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  case_constructor.py
@Time    :  2022/6/10 6:53 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from app.core.constructor.constructor import ConstructorAbstract
from app.core.handler.jsonres import PikaJsonEncoder
from app.crud.itst.api.testcase import ApiTestCaseDao
from app.models.constructor import ConstructorModel


class TestCaseConstructor(ConstructorAbstract, PikaJsonEncoder):
    @classmethod
    async def run(cls, executor, env, index, path, params, req_params, constructor: ConstructorModel, **kwargs):
        try:
            constructor_name = cls.get_name(constructor)

            data = cls.safe_json_loads(constructor.constructor_json)
            case_id = data.get("constructor_case_id")
            if not case_id:
                raise Exception("未获取到前/后置条件的用例id, 请检查前置条件")
            testcase, err = await ApiTestCaseDao.query_test_case(case_id)
            if err:
                raise Exception(f"用例: [{case_id}]不存在:")
            executor.append(content=f"当前路径: {path}, 第{index + 1}条{constructor_name}")
            # 说明是case
            executor_class = kwargs.get("executor_class")(executor.logger)
            new_param = data.get("params")
            if new_param:
                temp = cls.safe_json_loads(new_param)
                req_params.update(temp)
            result, err = await executor_class.run(env, case_id, params, req_params, f"{path}->{testcase.name}")
            if err:
                raise Exception(err)
            if not result["status"]:
                raise Exception(f"断言失败, 断言数据: {result.get('asserts', 'unknown')}")
            params[constructor.value] = result
        except Exception as e:
            raise Exception(f"{path}->{constructor.name} 第{index + 1}个{constructor_name}执行失败: {e}")
