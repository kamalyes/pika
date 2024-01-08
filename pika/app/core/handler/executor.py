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
import asyncio
import re
import time
from collections import defaultdict
from datetime import datetime
from typing import Any, List, Tuple, Union

from config import PikaAppConfig

from app.core.constructor.case_constructor import TestCaseConstructor
from app.core.constructor.http_constructor import HttpConstructor
from app.core.constructor.python_constructor import PythonConstructor
from app.core.constructor.redis_constructor import RedisConstructor
from app.core.constructor.sql_constructor import SqlConstructor
from app.core.handler.jsonres import PikaJsonEncoder
from app.core.handler.logger import PikaLogger
from app.core.notice.dingtalk import DingTalk
from app.core.notice.email import EmailManger
from app.core.paramters import parameters_parser
from app.crud.itst.api.testcase import ApiTestCaseDao
from app.crud.itst.api.testcase_assert import ApiTestCaseAssertsDao
from app.crud.itst.api.testcase_data import ApiTestCaseDataDao
from app.crud.itst.api.testcase_out_params import ApiTestCaseOutParametersDao
from app.crud.itst.api.testreport import ApiTestReportDao
from app.crud.itst.api.testresult import ApiTestResultDao
from app.crud.itstem.environment import EnvironmentDao
from app.crud.itstem.gateway import GatewayDao
from app.crud.itstem.gconfig import GConfigDao
from app.crud.pmp.project import ProjectDao
from app.crud.pmp.testplan import ApiTestPlanDao
from app.crud.rbac.user import UserDao
from app.enums.ConstructorEnum import ConstructorTypeEnum
from app.enums.GconfigEnum import GConfigParserEnum, GConfigTypeEnum
from app.enums.NoticeEnum import NoticeTypeEnum
from app.enums.RequestBodyEnum import ReqBodyTypeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.middleware.async_ask import AsyncRequest
from app.models.api_test_case import ApiTestCaseModel
from app.models.api_testcase_asserts import ApiTestCaseAssertsModel
from app.models.api_testcase_out_parameters import ApiTestCaseOutParametersModel
from app.models.api_testplan import ApiTestPlanModel
from app.models.constructor import ConstructorModel
from app.models.project import ProjectModel
from app.schema.api_testcase_result import ApiTestCaseResultSchema
from app.utils.case_logger import CaseLog
from app.utils.decorator import case_log, lock
from app.utils.gconfig_parser import JSONGConfigParser, StringGConfigParser, YamlGConfigParser
from app.utils.json_compare import JsonCompare
from app.utils.ws_manager import ws_manage


class Executor(object):
    log = PikaLogger("Executor")
    el_exp = r"\$\{(.+?)\}"
    pattern = re.compile(el_exp)
    # 需要替换全局变量的字段
    fields = ["request_body", "url", "request_headers"]

    def __init__(self, log: CaseLog = None):
        if log is None:
            self._logger = CaseLog()
            self._main = True
        else:
            self._logger = log
            self._main = False

    @property
    def logger(self):
        return self._logger

    @staticmethod
    def get_constructor_type(c: ConstructorModel):
        if c.type == ConstructorTypeEnum.testcase:
            return TestCaseConstructor
        if c.type == ConstructorTypeEnum.sql:
            return SqlConstructor
        if c.type == ConstructorTypeEnum.redis:
            return RedisConstructor
        if c.type == ConstructorTypeEnum.py_script:
            return PythonConstructor
        if c.type == ConstructorTypeEnum.http:
            return HttpConstructor
        return None

    def append(self, content, end=False):
        self.logger.append(content=content, end=end)

    @case_log
    async def parse_gconfig(self, data, type_, env, *fields):
        """
        解析全局变量
        Args:
            data:
            type_:
            env:
            *fields:

        Returns:

        """
        for f in fields:
            await self.parse_field(data, f, GConfigTypeEnum.text(type_), env)

    @case_log
    def get_parser(self, key_type):
        """
        获取变量解析器
        Args:
            key_type:

        Returns:

        """
        if key_type == GConfigParserEnum.string:
            return StringGConfigParser.parse
        if key_type == GConfigParserEnum.json:
            return JSONGConfigParser.parse
        if key_type == GConfigParserEnum.yaml:
            return YamlGConfigParser.parse
        raise Exception(f"全局变量类型: {key_type}不合法, 请检查!")

    # noinspection PyMethodMayBeStatic
    def get_el_expression(self, string: str):
        """
        获取字符串中的el表达式
        Args:
            string:

        Returns:

        """
        if string is None:
            return []
        return re.findall(Executor.pattern, string)

    async def parse_field(self, data, field, name, env):
        """
        解析字段
        Args:
            data:
            field:
            name:
            env:

        Returns:

        """
        try:
            self.append("获取{}: [{}]字段: [{}]中的el表达式".format(name, data, field))
            field_origin = getattr(data, field)
            variables = self.get_el_expression(field_origin)
            for v in variables:
                key = v.split(".")[0]
                cf = await GConfigDao.async_get_gconfig_by_key(key, env)
                if cf is not None:
                    # 解析变量
                    parse = self.get_parser(cf.key_type)
                    new_value = parse(cf.value, v)
                    new_field = field_origin.replace("${%s}" % v, new_value)
                    setattr(data, field, new_field)
                    self.append("替换全局变量成功, 字段: [{}]:\n\n[{}] -> [{}]\n".format(field, "${%s}" % v, new_value))
                    field_origin = new_field
            self.append("获取{}字段: [{}]中的el表达式".format(name, field), True)
        except Exception as e:
            Executor.log.error(f"查询全局变量失败, error: {str(e)}")
            raise Exception(f"查询全局变量失败, error: {str(e)}")

    def replace_params(self, field_name, field_origin, params: dict):
        """

        Args:
            field_name:
            field_origin:
            params:

        Returns:

        """
        new_data = {}
        if not isinstance(field_origin, str):
            return new_data
        variables = self.get_el_expression(field_origin)
        for v in variables:
            key = v.split(".")
            if not params.get(key[0]):
                continue
            result = params
            for branch in key:
                if isinstance(result, str):
                    # 说明需要反序列化
                    try:
                        result = PikaJsonEncoder.safe_json_loads(result)
                    except Exception as e:
                        self.append(f"反序列化失败, result: {result}\nERROR: {e}")
                        break
                if branch.isdigit():
                    # 说明路径里面的是数组
                    result = result[int(branch)]
                else:
                    result = result.get(branch)
                if result is None:
                    raise Exception(f"变量路径: {v}不存在, 请检查JSON或路径!")
            if field_name == "request_headers":
                new_value = PikaJsonEncoder.safe_json_loads(result)
            elif not isinstance(result, str):
                new_value = PikaJsonEncoder.safe_json_dumps(result, ensure_ascii=False)
            else:
                new_value = result
                if new_value is None:
                    self.append("替换变量失败, 找不到对应的数据")
                    continue
            new_data["${%s}" % v] = new_value
        return new_data

    async def parse_params(self, data: ApiTestCaseModel, params: dict):
        """

        Args:
            data:
            params:

        Returns:

        """
        self.append("正在替换变量")
        try:
            for c in data.__table__.columns:
                field_origin = getattr(data, c.name)
                replace_kv = self.replace_params(c.name, field_origin, params)
                for k, v in replace_kv.items():
                    new_field = field_origin.replace(k, v)
                    setattr(data, c.name, new_field)
                    self.append("替换流程变量成功,字段: [{}]: \n\n[{}] -> [{}]\n".format(c.name, k, v))
        except Exception as e:
            Executor.log.error(f"替换变量失败, error: {str(e)}")
            raise Exception(f"替换变量失败, error: {str(e)}")

    @case_log
    async def get_constructor(self, case_id):
        """
        获取构造数据
        Args:
            case_id:

        Returns:

        """
        return await ApiTestCaseDao.async_select_constructor(case_id)

    async def execute_constructors(
        self,
        env: str,
        path,
        case_info,
        params,
        req_params,
        constructors: List[ConstructorModel],
        asserts,
        suffix=False,
    ):
        """
        开始构造数据
        Args:
            env:
            path:
            case_info:
            params:
            req_params:
            constructors:
            asserts:
            suffix:

        Returns:

        """
        if len(constructors) == 0:
            self.append("前后置条件为空, 跳出该环节")
            return False
        current = 0
        for _i, c in enumerate(constructors):
            if c.suffix == suffix:
                await self.execute_constructor(env, current, path, params, req_params, c)
                self.replace_args(params, case_info, constructors, asserts)
                current += 1
        return True

    async def execute_constructor(self, env, index, path, params, req_params, constructor: ConstructorModel):
        """
        执行构造方法
        Args:
            env:
            index:
            path:
            params:
            req_params:
            constructor:

        Returns:

        """
        if not constructor.enabled_flag:
            self.append(f"当前路径: {path}, 构造方法: {constructor.name} 已关闭, 不继续执行")
            return False
        construct = Executor.get_constructor_type(constructor)
        if construct is None:
            self.append(f"构造方法类型: {constructor.type} 不合法, 请检查")
            return None
        await construct.run(
            self,
            env=env,
            index=index,
            path=path,
            params=params,
            req_params=req_params,
            constructor=constructor,
            executor_class=Executor,
        )
        return None

    def add_header(self, case_info, headers):
        """

        Args:
            case_info:
            headers:

        Returns:

        """
        if case_info.request_body_type == ReqBodyTypeEnum.none:
            return
        if case_info.request_body_type == ReqBodyTypeEnum.json and "Content-Type" not in headers:
            headers["Content-Type"] = "application/json; charset=UTF-8"

    @case_log
    def extract_out_parameters(self, response_info, data: List[ApiTestCaseOutParametersModel]):
        """
        提取出参数据
        Args:
            response_info:
            data:

        Returns:

        """
        result = {}
        for d in data:
            p = parameters_parser(d.source)
            result[d.name] = p(response_info, d.expression, idx=d.match_index)
        return result

    @case_log
    def my_assert(self, asserts: List, json_format: bool) -> Union[dict, bool, Tuple]:
        """
        断言验证
        Args:
            asserts:
            json_format:

        Returns:

        """
        result, status = {}, True
        if len(asserts) == 0:
            self.append("未设置断言, 用例结束")
            result = PikaJsonEncoder.safe_json_dumps(result, ensure_ascii=False)
            return result, status
        for item in asserts:
            try:
                # 解析预期/实际结果
                expected = self.translate(item.expected)
                # 判断请求返回是否是json格式,如果不是则不进行loads操作
                actually = self.translate(item.actually)
                status, err = self.ops(item.assert_type, expected, actually)
                result[item.id] = {"status": status, "msg": err}
            except Exception as e:
                status = False
                self.append(f"预期结果: {item.expected}\n实际结果: {item.actually}\n")
                result[item.id] = {"status": False, "msg": f"断言取值失败, 请检查断言语句: {e}"}
        return PikaJsonEncoder.safe_json_dumps(result, ensure_ascii=False), status

    async def run(
        self,
        env: str,
        case_id: str,
        params_pool: dict = None,
        request_param: dict = None,
        path: str = "主case",
    ):
        """
        开始执行测试用例
        Args:
            env:
            case_id:
            params_pool:
            request_param:
            path:

        Returns:

        """
        response_info = {}

        # 初始化case全局变量, 只存在于case生命周期 注意 它与全局变量不是一套逻辑
        case_params = params_pool
        if case_params is None:
            case_params = {}

        req_params = request_param
        if req_params is None:
            req_params = {}

        try:
            case_info, err = await ApiTestCaseDao.query_test_case(case_id)
            if err:
                return response_info, err
            response_info["case_id"] = case_info.id
            response_info["case_name"] = case_info.name
            request_method = case_info.request_method.upper()
            response_info["request_method"] = request_method

            # Step1: 替换全局变量
            await self.parse_gconfig(case_info, GConfigTypeEnum.case, env, *Executor.fields)
            self.append("解析全局变量", True)

            # Step2: 获取构造数据
            constructors = await self.get_constructor(case_id)

            #  Step3: 解析前后置条件的全局变量
            for c in constructors:
                await self.parse_gconfig(c, GConfigTypeEnum.constructor, env, "constructor_json")

            # Step4: 获取断言
            asserts = await ApiTestCaseAssertsDao.async_list_test_case_asserts(case_id)
            for ast in asserts:
                await self.parse_gconfig(ast, GConfigTypeEnum.asserts, env, "expected", "actually")

            # Step5: 获取出参信息
            out_parameters = await ApiTestCaseOutParametersDao.select_list(case_id=case_id)

            # Step6: 替换参数
            self.replace_args(req_params, case_info, constructors, asserts)

            # Step7: 执行前置条件
            await self.execute_constructors(env, path, case_info, case_params, req_params, constructors, asserts)

            # Step8: 批量改写主方法参数
            await self.parse_params(case_info, case_params)
            headers = PikaJsonEncoder.safe_json_loads(case_info.request_headers)
            # Step9: 替换请求参数
            request_body = await self.replace_body(request_param, case_info.request_body, case_info.request_body_type)

            # Step10: 替换base_gateway
            if case_info.base_gateway:
                base_gateway = await GatewayDao.query_gateway(env, id=case_info.base_gateway)
                case_info.url = f"{base_gateway if base_gateway else ''}{case_info.url}"
            response_info["url"] = case_info.url

            # Step10: 完成http请求
            request_obj = await AsyncRequest.client(
                url=case_info.url,
                request_body_type=case_info.request_body_type,
                headers=headers,
                request_body=request_body,
            )
            res = await request_obj.invoke(request_method)
            self.append(
                f"http请求过程\n\nRequest Method: {request_method}\n\n"
                f"Request Headers:\n{headers}\n\nUrl: {case_info.url}"
                f"\n\nRequest Body:\n{case_info.request_body}\n\nResponse:\n{res.get('response', '未获取到返回值')}",
            )
            response_info.update(res)

            # Step11: 提取出参
            if out_parameters:
                out_dict = self.extract_out_parameters(response_info, out_parameters)
                case_params.update(out_dict)

            # Step12: 替换变量
            self.replace_asserts(asserts, req_params, case_params)
            self.replace_constructors(constructors, req_params, case_params)

            # Step13: 执行后置条件
            await self.execute_constructors(env, path, case_info, case_params, req_params, constructors, asserts, True)

            # Step14: 执行断言
            json_format_ = response_info.get("json_format")
            asserts, status = await self.my_assert(asserts, json_format_)
            response_info["status"] = status
            response_info["asserts"] = asserts
            # 日志输出, 如果不是主用例则不记录
            if self._main:
                response_info["case_log"] = self.logger.join()
            return response_info, None
        except Exception as e:
            detail = f"执行用例失败, error: {str(e)}"
            Executor.log.exception(f"{detail} \n")
            self.append(detail)
            if self._main:
                response_info["case_log"] = self.logger.join()
            return response_info, f"执行用例失败, error: {str(e)}"

    @staticmethod
    def get_dict(json_data: str):
        return PikaJsonEncoder.safe_json_loads(json_data)

    def replace_cls(self, params: dict, cls, *fields: Any):
        for k, _v in params.items():
            for f in fields:
                fd = getattr(cls, f, "")
                if fd is None:
                    continue
                if k in fd:
                    data = self.replace_params(f, fd, params)
                    for a, b in data.items():
                        fd = fd.replace(a, b)
                        setattr(cls, f, fd)

    def replace_args(
        self,
        params,
        data: ApiTestCaseModel,
        constructors: List[ConstructorModel],
        asserts: List[ApiTestCaseAssertsModel],
    ):
        """
        替换参数
        Args:
            params:
            data:
            constructors:
            asserts:

        Returns:

        """
        self.replace_testcase(params, data)
        self.replace_constructors(constructors, params)
        self.replace_asserts(asserts, params)

    def replace_testcase(self, params: dict, data: ApiTestCaseModel):
        """
        替换测试用例中的参数
        Args:
            params:
            data:

        Returns:

        """
        self.replace_cls(params, data, "request_headers", "request_body", "url")

    def replace_constructors(self, constructors: List[ConstructorModel], *params: dict):
        """
        替换数据构造器中的参数
        Args:
            params:
            constructors:

        Returns:

        """
        for c in constructors:
            for par in params:
                self.replace_cls(par, c, "constructor_json")

    def replace_asserts(self, asserts: List[ApiTestCaseAssertsModel], *params):
        """
        替换断言中的参数
        Args:
            params:
            asserts:

        Returns:

        """
        for a in asserts:
            for p in params:
                self.replace_cls(p, a, "expected", "actually")

    @staticmethod
    async def run_with_test_data(
        env,
        result_data: dict = None,
        report_id: str = None,
        case_id: str = None,
        params_pool: dict = None,
        request_param: dict = None,
        path="主case",
        data_name: str = None,
        data_id: str = None,
        retry_minutes: int = 0,
        retry_id=None,
    ):
        """
        运行测试
        Args:
            env:
            report_id:
            case_id:
            params_pool:
            request_param:
            path:
            data_name:
            data_id:
            retry_minutes:
            retry_id:

        Returns:

        """
        retry_times = PikaAppConfig.PIKA_CASE_RETRY_TIMES if retry_minutes > 0 else 0
        for i in range(retry_times + 1):
            start_date = datetime.now()
            executor = Executor()
            if retry_id is not None:
                result, err = await executor.run(env=env, case_id=case_id, request_param=request_param)
            else:
                result, err = await executor.run(env, case_id, params_pool, request_param, path)
            finished_date = datetime.now()
            cost = f"{(finished_date - start_date).seconds}s"
            status = 2 if err is not None else 0 if result.get("status") else 1
            # 若status不为0,代表case执行失败,走重试逻辑
            if status != 0 and i < retry_times:
                await asyncio.sleep(60 * retry_minutes)
                continue
            asserts = result.get("asserts")
            path = result.get("path")
            case_log_ = result.get("case_log")
            request_body = result.get("request_data")
            status_code = result.get("status_code")
            request_method = result.get("request_method")
            request_headers = result.get("request_headers")
            response = result.get("response")
            case_name = result.get("case_name")
            response_headers = result.get("response_headers")
            cookies = result.get("cookies")
            request_params = PikaJsonEncoder.safe_json_dumps(request_param, ensure_ascii=False)
            api_testcase_result = ApiTestCaseResultSchema(
                case_id,
                report_id,
                case_name,
                status,
                case_log_,
                start_date,
                finished_date,
                path,
                request_body,
                request_method,
                request_headers,
                cost,
                asserts,
                response_headers,
                response,
                status_code,
                cookies,
                retry_times,
                request_params,
                data_name,
            )
            if retry_id is not None:
                return await ApiTestResultDao.edit_report(api_testcase_result, retry_id=retry_id, case_id=case_id)
            result_data[case_id].append(status)
            api_testcase_result.data_id = data_id
            return await ApiTestResultDao.edit_report(api_testcase_result)
        return None

    @staticmethod
    async def run_single(
        env: str,
        result_data,
        report_id,
        case_id,
        params_pool: dict = None,
        path="主case",
        retry_minutes=0,
    ):
        """

        Args:
            env:
            result_data:
            report_id:
            case_id:
            params_pool:
            path:
            retry_minutes:

        Returns:

        """
        test_data = await ApiTestCaseDataDao.list_testcase_data_by_env(env, case_id)
        if not test_data:
            await Executor.run_with_test_data(
                env,
                result_data,
                report_id,
                case_id,
                params_pool,
                {},
                path,
                "默认数据",
                retry_minutes=retry_minutes,
            )
        else:
            await asyncio.gather(
                *(
                    Executor.run_with_test_data(
                        env,
                        result_data,
                        report_id,
                        case_id,
                        params_pool,
                        Executor.get_dict(x.json_data),
                        path,
                        x.name,
                        x.id,
                        retry_minutes=retry_minutes,
                    )
                    for x in test_data
                ),
            )

    @case_log
    def replace_body(self, req_params, request_body, request_body_type=1):
        """
        根据传入的构造参数进行参数替换
        Args:
            req_params:
            request_body:
            request_body_type:

        Returns:

        """
        if request_body_type != ReqBodyTypeEnum.json:
            self.append("当前请求数据不为json, 跳过替换")
            return request_body
        try:
            if request_body:
                data = PikaJsonEncoder.safe_json_loads(request_body)
                if req_params:
                    for k, v in req_params.items():
                        if data.get(k) is not None:
                            data[k] = v
                return PikaJsonEncoder.safe_json_dumps(data, ensure_ascii=False)
            self.append("request_body为空, 不进行替换")
        except Exception as e:
            self.append(f"替换请求request_body失败, {e}")
        return request_body

    @case_log
    def tidy_ops_res(self, expected, actually, condition, flag):
        symbol = "【✅】" if flag else "【❌】"
        detail = f"预期结果: {expected} {condition} 实际结果: {actually}{symbol}"
        return flag, detail

    @case_log
    def ops(self, assert_type: str, expected, actually) -> Union[bool, str, tuple]:
        """
        通过断言类型进行校验
        Args:
            assert_type:
            expected:
            actually:

        Returns:

        """
        if assert_type == "equal":
            if expected == actually:
                return self.tidy_ops_res(expected, actually, "等于", True)
            return self.tidy_ops_res(expected, actually, "不等于", False)
        if assert_type == "not_equal":
            # ne: 表示不等于!=, 即not equals
            if expected != actually:
                return self.tidy_ops_res(expected, actually, "不等于", True)
            return self.tidy_ops_res(expected, actually, "等于", False)
        if assert_type == "in":
            if expected in actually:
                return self.tidy_ops_res(expected, actually, "包含于", True)
            return self.tidy_ops_res(expected, actually, "不包含于", False)
        if assert_type == "not_in":
            if expected not in actually:
                return self.tidy_ops_res(expected, actually, "不包含于", True)
            return self.tidy_ops_res(expected, actually, "包含于", False)
        if assert_type == "contain":
            if actually in expected:
                return self.tidy_ops_res(expected, actually, "包含", True)
            return self.tidy_ops_res(expected, actually, "不包含", False)
        if assert_type == "not_contain":
            if actually not in expected:
                return self.tidy_ops_res(expected, actually, "不包含", True)
            return self.tidy_ops_res(expected, actually, "包含", False)
        if assert_type == "length_eq":
            # eq: 表示等于,即equals
            if expected == len(actually):
                return self.tidy_ops_res(expected, actually, "等于", True)
            return self.tidy_ops_res(expected, actually, "不等于", False)
        if assert_type == "length_gt":
            # gt: 表示大于>,即greater than
            if expected > len(actually):
                return self.tidy_ops_res(expected, actually, "大于", True)
            return self.tidy_ops_res(expected, actually, "不大于", False)
        if assert_type == "length_ge":
            #  ge: 表示大于等于>=, 即greater than or equals to
            if expected >= len(actually):
                return self.tidy_ops_res(expected, actually, "大于等于", True)
            return self.tidy_ops_res(expected, actually, "小于", False)
        if assert_type == "length_le":
            # le: 表示小于等于<=, 即less than or equals to
            if expected <= len(actually):
                return self.tidy_ops_res(expected, actually, "小于等于", True)
            return self.tidy_ops_res(expected, actually, "大于", False)
        if assert_type == "length_lt":
            # lt: 表示小于<, 即less than
            if expected < len(actually):
                return self.tidy_ops_res(expected, actually, "小于", True)
            return self.tidy_ops_res(expected, actually, "不小于", False)
        if assert_type == "json_equal":
            data = JsonCompare().compare(expected, actually)
            if len(data) == 0:
                return self.tidy_ops_res(expected, actually, "等于", True)
            return False, data
        if assert_type == "text_in":
            if isinstance(actually, str):
                # 如果b是string,则不转换
                if expected in actually:
                    return self.tidy_ops_res(expected, actually, "文本包含于", True)
                return self.tidy_ops_res(expected, actually, "文本不包含于", False)
            temp = PikaJsonEncoder.safe_json_dumps(actually, ensure_ascii=False)
            if expected in temp:
                return self.tidy_ops_res(expected, actually, "文本包含于", True)
            return self.tidy_ops_res(expected, actually, "文本不包含于", False)
        if assert_type == "text_not_in":
            if isinstance(actually, str):
                if expected not in actually:
                    return self.tidy_ops_res(expected, actually, "文本不包含于", True)
                return self.tidy_ops_res(expected, actually, "文本包含于", False)
            temp = PikaJsonEncoder.safe_json_dumps(actually, ensure_ascii=False)
            if expected not in temp:
                return self.tidy_ops_res(expected, actually, "文本不包含于", True)
            return self.tidy_ops_res(expected, actually, "文本不包含于", False)
        return False, "不支持的断言方式💔"

    @case_log
    def translate(self, data):
        """
        反序列化为Python对象
        Args:
            data:

        Returns:

        """
        return PikaJsonEncoder.safe_json_loads(data)

    # noinspection PyMethodMayBeStatic
    def replace_branch(self, branch: str, params: dict):
        if not params:
            return branch
        if branch.startswith("#"):
            # 说明branch也是个子变量
            data = branch[1:]
            if len(data) == 0:
                return branch
            dist = params.get(data)
            if dist is None:
                return branch
            return params.get(data)
        return branch

    @case_log
    def parse_variable(self, response_info, string: str, params=None):
        """
        解析返回response中的变量
        Args:
            response_info:
            string:
            params:

        Returns:

        """
        expected = self.get_el_expression(string)
        if len(expected) == 0:
            return string
        data = expected[0]
        el_list = data.split(".")
        # ${response.data.id}
        result = response_info
        try:
            for branch in el_list:
                branch = self.replace_branch(branch, params)
                if isinstance(result, str):
                    # 说明需要反序列化
                    try:
                        result = PikaJsonEncoder.safe_json_loads(result)
                    except Exception as e:
                        self.append(f"反序列化失败, result: {result}\nERROR: {e}")
                        break
                # 2022-02-27 修复数组变量替换的bug
                if isinstance(branch, int) or branch.isdigit():
                    # 说明路径里面的是数组
                    result = result[int(branch)]
                else:
                    result = result.get(branch)
        except Exception as e:
            raise Exception(f"获取变量失败, error: {str(e)}")
        if string == "${response}":
            return result
        return PikaJsonEncoder.safe_json_dumps(result, ensure_ascii=False)

    @staticmethod
    async def notice(env: list, plan: ApiTestPlanModel, project: ProjectModel, report_dict: dict, users: list):
        """
        消息通知方法
        Args:
            env:
            plan:
            project:
            report_dict:
            users:

        Returns:

        """
        for e in env:
            msg_types = plan.msg_type.split(",")
            if msg_types and users:
                for m in msg_types:
                    if int(m) == NoticeTypeEnum.EMAIL:
                        content = EmailManger.test_report_template(plan_name=plan.name, **report_dict[e])
                        subject = (
                            f"【{report_dict[e].get('env')}】测试计划【{plan.name}】执行完毕({report_dict[e].get('plan_result')})"
                        )
                        return EmailManger.send_email(
                            content=content,
                            subject=subject,
                            addressee=[r.get("email") for r in users],
                        )
                    if int(m) == NoticeTypeEnum.DINGDING:
                        report_dict[e]["result_color"] = (
                            "#67C23A" if report_dict[e]["plan_result"] == "通过" else "#E6A23C"
                        )
                        # 批量获取用户手机号
                        ding_users = [r.get("mobile") for r in users]
                        report_dict[e]["notification_user"] = " ".join((f"@{x}" for x in ding_users))
                        render_markdown = DingTalk.render_markdown(**report_dict[e], plan_name=plan.name)
                        if not project.dingtalk_url:
                            Executor.log.debug("项目未配置钉钉通知机器人")
                            continue
                        ding = DingTalk(project.dingtalk_url)
                        await ding.send_msg(
                            f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}测试报告",
                            render_markdown,
                            None,
                            ding_users,
                        )
        return None

    @staticmethod
    @lock("test_plan")
    async def run_test_plan(plan_id: str, executor: str = None):
        """
        通过测试计划id执行测试计划
        Args:
            plan_id:
            executor:

        Returns:

        """
        plan = await ApiTestPlanDao.query_test_plan(plan_id)
        if plan is None:
            Executor.log.debug(f"测试计划: [{plan_id}]不存在")
            return
        try:
            # 设置为running
            await ApiTestPlanDao.update_test_plan_state(plan.id, 1)
            project, _ = await ProjectDao.query_project(plan.project_id)
            env = list(map(str, plan.env_list.split(",")))
            case_list = list(map(str, plan.case_list.split(",")))
            receiver = list(map(str, plan.receiver.split(",") if plan.receiver else []))
            # 聚合报告dict
            report_dict = {}
            await asyncio.gather(
                *(
                    Executor.run_multiple(
                        executor,
                        e,
                        case_list,
                        mode=1,
                        retry_minutes=plan.retry_minutes,
                        plan_id=plan.id,
                        ordered=plan.ordered,
                        report_dict=report_dict,
                    )
                    for e in env
                ),
            )
            await ApiTestPlanDao.update_test_plan_state(plan.id, 0)
            users = await UserDao.list_user_touch(*receiver)
            await Executor.notice(env, plan, project, report_dict, users)
            if executor is not None:
                await ws_manage.notify(executor, title="测试计划执行完毕", content="请前往测试报告页面查看细节")
        except Exception as e:
            Executor.log.exception(detail=f"执行测试计划: 【{plan.name}】失败, error: {str(e)}")

    @staticmethod
    async def run_multiple(
        executor: str,
        env: str,
        case_list: List[str],
        mode=0,
        plan_id: str = None,
        ordered=False,
        report_dict: dict = None,
        retry_minutes: int = 0,
    ):
        try:
            current_env = await EnvironmentDao.query_env(env)
            if executor is not None:
                # 说明不是系统执行
                user = await UserDao.query_user(executor)
                executor = user.username if user is not None else "未知"
            else:
                executor = "CPU"
            st = time.perf_counter()
            # step1: 新增测试报告数据
            report_id = await ApiTestReportDao.start(executor, env, mode, plan_id=plan_id)
            # step2: 开始执行用例
            result_data = defaultdict(list)
            # step3: 将报告改为 running状态
            await ApiTestReportDao.update(report_id, 1)
            # step4: 执行用例并搜集数据
            if not ordered:
                await asyncio.gather(
                    *(
                        Executor.run_single(env, result_data, report_id, c, retry_minutes=retry_minutes)
                        for c in case_list
                    ),
                )
            else:
                # 顺序执行
                for c in case_list:
                    await Executor.run_single(env, result_data, report_id, c, retry_minutes=retry_minutes)
            ok, fail, skip, error = 0, 0, 0, 0
            for _case_id, status in result_data.items():
                for s in status:
                    if s == 0:
                        ok += 1
                    elif s == 1:
                        fail += 1
                    elif s == 2:
                        error += 1
                    else:
                        skip += 1
            cost = time.perf_counter() - st
            cost = "%.2f" % cost
            # step5: 回写数据到报告
            report = await ApiTestReportDao.end(report_id, ok, fail, error, skip, 3, cost)
            if report_dict is not None:
                format_ytdhms = PikaGlobalVarEnum.TIME_FORMATTING_YTDHMS
                report_dict[env] = {
                    "report_url": f"{PikaAppConfig.PIKA_FRONTEND_URL}/#/record/report/{report_id}",
                    "start_date": report.start_date.strftime(format_ytdhms),
                    "finished_date": report.finished_date.strftime(format_ytdhms),
                    "success": ok,
                    "failed": fail,
                    "total": ok + fail + error + skip,
                    "error": error,
                    "skip": skip,
                    "executor": executor,
                    "cost": cost,
                    "plan_result": "通过" if ok + fail + error + skip > 0 and fail + error == 0 else "未通过",
                    "env": current_env.name,
                }
            return report_id
        except Exception as e:
            raise Exception(f"批量执行用例失败: {e}")
