# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  generator.py
@Time    :  2022/6/18 2:19 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  case生成器,根据RequestInfoSchema数组生成
"""

import json
from collections import defaultdict
from json import JSONDecodeError
from typing import List
from loguru import logger
from app.enums.CaseStatusEnum import CaseStatus
from app.enums.ConstructorEnum import ConstructorTypeEnum
from app.enums.RequestBodyEnum import ReqBodyTypeEnum
from app.enums.ProtocolEnum import ProtocolTypeEnum
from app.exceptions.convert.GenerateException import GenerateException
from app.schema.api_testcase import TestCaseSchema
from app.schema.constructor import IndexConstructorSchema
from app.schema.request import RequestInfoSchema


class CaseGenerator(object):
    # 忽略的字段
    ignored = (
        "Content-Type",
        "Connection",
        "Date",
        "Content-Length",
        "Host",
        "access-control-allow-credentials",
        "access-control-allow-origin",
        "User-Agent",
        "Server",
    )

    @staticmethod
    def ignore(key: str):
        """
        忽略值
        Args:
            key:

        Returns:

        """
        for ig in CaseGenerator.ignored:
            if key.lower().endswith(ig.lower()):
                return True
        return False

    @staticmethod
    def get_content_type(headers):
        """
        获取body类型
        Args:
            headers:

        Returns:

        """
        content_type = headers.get("Content-Type", "").lower()
        if "json" in content_type:
            return ReqBodyTypeEnum.json
        if "x-www-form" in content_type:
            return ReqBodyTypeEnum.x_form
        if "form" in content_type:
            return ReqBodyTypeEnum.form
        return ReqBodyTypeEnum.none

    @staticmethod
    def generate_constructors(requests: List[RequestInfoSchema]) -> List[IndexConstructorSchema]:
        """
        生成构建器
        Args:
            requests:

        Returns:

        """
        constructors = []
        for r in range(len(requests) - 1):
            name = f"http请求_{r + 1}"
            constructor_json = json.dumps(
                dict(
                    request_body=requests[r].request_body,
                    headers=requests[r].request_headers,
                    base_path=None,
                    url=requests[r].url,
                    request_method=requests[r].request_method,
                    content_type=CaseGenerator.get_content_type(
                        requests[r].request_headers),
                ),
                ensure_ascii=False,
            )
            c = IndexConstructorSchema(
                name=name,
                value=f"http_res_{r + 1}",
                constructor_json=constructor_json,
                enable=True,
                public=True,
                suffix=False,
                index=r + 1,
                type=ConstructorTypeEnum.http.value,
            )
            constructors.append(c)
        return constructors

    @staticmethod
    def generate_case(directory_id: str, name: str, last: RequestInfoSchema) -> TestCaseSchema:
        """
        生成用例
        Args:
            directory_id:
            name:
            last:

        Returns:

        """
        return TestCaseSchema(
            directory_id=directory_id,
            name=name,
            url=last.url,
            protocolType=ProtocolTypeEnum.http.value,
            request_body=last.request_body,
            request_method=last.request_method,
            content_type=CaseGenerator.get_content_type(last.request_headers).value,
            request_headers=json.dumps(
                last.request_headers, ensure_ascii=False),
            case_type=0,
            status=CaseStatus.debugging.value,
            priority="P3",
        )

    @staticmethod
    def extract_field(requests: List[RequestInfoSchema]) -> List[str]:
        """
        遍历接口,并提取其中的变量
        Args:
            requests:

        Returns:

        """
        var_pool = defaultdict(list)
        replaced = []
        for i in range(len(requests)):
            # 删除headers里面的Content-Length字段
            if "Content-Length" in requests[i].request_headers:
                requests[i].request_headers.pop("Content-Length")
            if "Content-Length" in requests[i].response_headers:
                requests[i].response_headers.pop("Content-Length")
            # 记录变量
            CaseGenerator.record_vars(
                requests[i], var_pool, f"http_res_{i + 1}")
            if i > 0:
                CaseGenerator.replace_vars(requests[i], var_pool, replaced)
        return replaced

    @staticmethod
    def replace_vars(request: RequestInfoSchema, ans: dict, replaced: list):
        """
        替换变量
        Args:
            request:
            ans:
            replaced:

        Returns:

        """
        CaseGenerator.replace_url(request, ans, replaced)
        CaseGenerator.replace_headers(request, ans, replaced)
        CaseGenerator.replace_body(request, ans, replaced)

    @staticmethod
    def record_vars(request: RequestInfoSchema, ans: dict, var_name: str):
        """
        记录变量
        Args:
            request:
            ans:
            var_name:

        Returns:

        """
        CaseGenerator.analysis_headers(
            request, ans, f"{var_name}.response_headers")
        CaseGenerator.analysis_body(request, ans, f"{var_name}.response")

    @staticmethod
    def dfs(request_body, path: str, ans: dict, headers: bool = False):
        """
        Args:
            request_body:
            path:
            ans:
            headers:

        Returns:

        """
        if isinstance(request_body, list):
            for i in range(len(request_body)):
                c_path = f"{path}.{i}"
                CaseGenerator.dfs(request_body[i], c_path, ans, headers)
        elif isinstance(request_body, dict):
            for k, v in request_body.items():
                c_path = f"{path}.{k}"
                CaseGenerator.dfs(v, c_path, ans, headers)
        else:
            if not headers or not CaseGenerator.ignore(path):
                # 如果是bool值,需要特殊处理一下,因为Python get False/True会变成get 0 1
                if request_body is not None:
                    if isinstance(request_body, bool):
                        ans[str(request_body)].append(path)
                    else:
                        ans[request_body].append(path)

    @staticmethod
    def analysis_body(request: RequestInfoSchema, ans: dict, var_name: str = None):
        """
        解析request_body
        Args:
            request:
            ans:
            var_name:

        Returns:

        """
        if request.request_body:
            try:
                request_body = json.loads(request.response_content)
                CaseGenerator.dfs(request_body, var_name, ans)
            except JSONDecodeError:
                # 可能request_body不是JSON,跳过
                pass
            except Exception as e:
                raise GenerateException(detail=f"解析接口request_body变量出错: {e}")

    @staticmethod
    def analysis_headers(request: RequestInfoSchema, ans: dict, var_name: str = None):
        """
        解析headers
        Args:
            request:
            ans:
            var_name:

        Returns:

        """
        try:
            CaseGenerator.dfs(request.response_headers, var_name, ans, True)
        except Exception as e:
            raise GenerateException(detail=f"解析接口headers变量出错: {e}")

    @staticmethod
    def replace_headers(request: RequestInfoSchema, ans: dict, replaced: list):
        """
        替换headers
        Args:
            request:
            ans:
            replaced:

        Returns:

        """
        for k, v in request.request_headers.items():
            if ans.get(v):
                request.request_headers[k] = "${%s}" % ans.get(v)[0]
                replaced.append("%s => ${%s}" % (k, ans.get(v)[0]))

    @staticmethod
    def replace_body(request: RequestInfoSchema, ans: dict, replaced: list):
        """
        替换request_body
        Args:
            request:
            ans:
            replaced:

        Returns:

        """
        if request.request_body:
            try:
                data = json.loads(request.request_body)
                var_type = list()
                CaseGenerator.dfs_replace(data, ans, var_type, replaced)
                result = json.dumps(data, ensure_ascii=False)
                for v in var_type:
                    result = result.replace(f'"{v}"', f"{v}")
                request.request_body = result
            except JSONDecodeError:
                pass
            except Exception as e:
                logger.error(f"转换body变量失败: {e}")

    @staticmethod
    def dfs_replace(request_body, ans: dict, var_type: list, replaced: list):
        """

        Args:
            request_body:
            ans:
            var_type:
            replaced:

        Returns:

        """
        if isinstance(request_body, dict):
            for k, v in request_body.items():
                string, value = CaseGenerator.dfs_replace(
                    v, ans, var_type, replaced)
                if value is not None:
                    request_body[k] = "${%s}" % value
                    if not string:
                        var_type.append("${%s}" % value)
        elif isinstance(request_body, list):
            for i in range(len(request_body)):
                string, value = CaseGenerator.dfs_replace(
                    request_body[i], ans, var_type, replaced)
                if value is not None:
                    request_body[i] = "${%s}" % value
                    if not string:
                        var_type.append("${%s}" % value)
        else:
            body_str = request_body
            if isinstance(request_body, bool):
                body_str = str(request_body)
            if ans.get(body_str):
                replaced.append("%s => ${%s}" %
                                (body_str, ans.get(body_str)[0]))
                if not isinstance(body_str, str):
                    return False, ans.get(body_str)[0]
                return True, ans.get(body_str)[0]
            return None, None

    @staticmethod
    def replace_url(request: RequestInfoSchema, ans: dict, replaced: list):
        """
        拆解url,将url里面的路由path和query参数
        Args:
            request:
            ans:
            replaced:

        Returns:

        """
        # 获取前缀和后缀
        url_query = request.url.split("?")
        if len(url_query) == 1:
            query_list = list()
            prefix = url_query[0]
        else:
            prefix, suffix = url_query
            query_list = suffix.split("&")
        http, prefix = prefix.split("//")
        url_list = prefix.split("/")
        new_url = []
        new_query = []
        for u in url_list:
            if ans.get(u):
                new_url.append(ans.get(u)[0])
                replaced.append("%s => ${%s}" % (u, ans.get(u)[0]))
            else:
                new_url.append(u)
        for q in query_list:
            k, v = q.split("=")
            if ans.get(v):
                new_query.append("%s=${%s}" % (k, ans.get(v)[0]))
                replaced.append("%s => ${%s}" % (k, ans.get(v)[0]))
            else:
                new_query.append(q)
        if len(query_list) == 0:
            request.url = f"{http}//{'/'.join(new_url)}"
            return
        request.url = f"{http}//{'/'.join(new_url)}?{'&'.join(new_query)}"
