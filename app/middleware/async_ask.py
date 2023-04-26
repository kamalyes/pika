# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  async_ask.py
@Time    :  2022/6/17 12:55 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import json
from aiohttp.client_exceptions import ClientProxyConnectionError, InvalidURL
from urllib.parse import urlparse
import aiohttp
from aiohttp import FormData
from custard.time import Moment
from app.enums.RequestBodyEnum import ReqBodyTypeEnum
from app.middleware.oss import OssClient
from config import PikaAppConfig
from app.core.handler.exceres import SystemException

class AsyncRequest(object):
    def __init__(self, url: str, timeout=15, **kwargs):
        self.url = url
        self.kwargs = kwargs
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self.proxy = f"http://127.0.0.1:{PikaAppConfig.MITMPROXY_PROXY_PORT}" if PikaAppConfig.MITMPROXY_ENABLE_FLAG else None

    def get_cookie(self, session):
        cookies = session.cookie_jar.filter_cookies(self.url)
        return {k: v.value for k, v in cookies.items()}

    def get_data(self, kwargs):
        if kwargs.get("json") is not None:
            return kwargs.get("json")
        return kwargs.get("data")

    async def invoke(self, method: str):
        try:
            async with aiohttp.ClientSession(cookie_jar=aiohttp.CookieJar(unsafe=True)) as session:
                start_date = Moment.get_now_time("13timestamp")
                async with session.request(
                    method, self.url, timeout=self.timeout, proxy=self.proxy, ssl=False, **self.kwargs
                ) as resp:
                    # if resp.status != 200: # 当http状态码不为200的时候给出提示
                    #     return await self.collect(False, self.get_data(self.kwargs), resp.status, msg="http状态码不为200")
                    finished_date = Moment.get_now_time("13timestamp")
                    cost_ = int("%.0f" % (finished_date - start_date))
                    cost = "%.3fs"%(cost_ / 1000) if cost_ > 1000 else f'{cost_}ms'
                    # print("invoke请求耗时", start_date, finished_date)
                    response, json_format = await AsyncRequest.get_resp(resp)
                    cookie = self.get_cookie(session)
                    return await self.collect(
                        True,
                        self.get_data(self.kwargs),
                        resp.status,
                        response,
                        resp.headers,
                        resp.request_info.headers,
                        elapsed=cost,
                        cookies=cookie,
                        json_format=json_format,
                    )
        except ClientProxyConnectionError as err:
            raise SystemException(detail=f'invoke失败,{err}')

    async def download(self):
        async with aiohttp.ClientSession(cookie_jar=aiohttp.CookieJar(unsafe=True)) as session:
            async with session.request("GET", self.url, timeout=self.timeout, proxy=self.proxy, ssl=False, **self.kwargs) as resp:
                if resp.status != 200:
                    raise SystemException(detail="download file failed")
                return await resp.content.read()
    
    @classmethod
    async def probe(cls, url):
        if url.startswith("localhost"):
            url = f"http://{url}"
        try:
            urlparse(url)
        except InvalidURL as error:
             raise SystemException(detail=f"{error}")

    @classmethod
    async def client(cls, url: str, request_body_type: ReqBodyTypeEnum = ReqBodyTypeEnum.json, timeout=15, **kwargs):
        await cls.probe(url)
        headers = kwargs.get("headers", {})
        if request_body_type == ReqBodyTypeEnum.json:
            if "Content-Type" not in headers:
                headers["Content-Type"] = "application/json; charset=UTF-8"
            # 新增json校验,修复史诗级bug: json被额外序列化
            try:
                request_body = kwargs.get("request_body")
                if request_body:
                    request_body = json.loads(request_body)
            except Exception as e:
                raise SystemException(detail=f"json格式不正确: {e}")
            r = AsyncRequest(url, headers=headers, timeout=timeout, json=request_body)
        elif request_body_type == ReqBodyTypeEnum.form:
            try:
                request_body = kwargs.get("request_body")
                form_data = None
                if request_body:
                    form_data = FormData()
                    # 因为存储的是字符串,所以需要反序列化
                    items = json.loads(request_body)
                    for item in items:
                        # 如果是文本类型,直接添加key-value
                        if item.get("type") == "TEXT":
                            form_data.add_field(item.get("key"), item.get("value", ""))
                        else:
                            client = OssClient.get_oss_client()
                            file_object = await client.get_file_object(item.get("value"))
                            form_data.add_field(item.get("key"), file_object)
                r = AsyncRequest(url, headers=headers, data=form_data, timeout=timeout)
            except Exception as e:
                raise SystemException(detail=f"解析form-data失败: {str(e)}")
        elif request_body_type == ReqBodyTypeEnum.x_form:
            request_body = kwargs.get("request_body", "{}")
            request_body = json.loads(request_body)
            r = AsyncRequest(url, headers=headers, data=request_body, timeout=timeout)
        else:
            # 暂时未支持其他类型
            r = AsyncRequest(url, headers=headers, timeout=timeout, data=kwargs.get("request_body"))
        return r

    @staticmethod
    async def get_resp(resp):
        try:
            data = await resp.json(encoding="utf-8")
            # 说明是json格式
            return json.dumps(data, ensure_ascii=False, indent=4), True
        except:
            data = await resp.text()
            # 说明不是json格式,我们不做loads操作了
            return data, False

    @staticmethod
    def get_request_data(request_body):
        if isinstance(request_body, bytes):
            request_body = request_body.decode()
        if isinstance(request_body, FormData):
            request_body = str(request_body)
        if isinstance(request_body, str) or request_body is None:
            return request_body
        return json.dumps(request_body, ensure_ascii=False, indent=4)

    @staticmethod
    async def collect(
        status,
        request_data,
        status_code=200,
        response=None,
        response_headers=None,
        request_headers=None,
        cookies=None,
        elapsed=None,
        msg="success",
        **kwargs,
    ):
        """
        收集http返回数据
        Args:
            status: 请求状态
            request_data: 请求入参
            status_code: 状态码
            response: 相应
            response_headers: 返回header
            request_headers:  请求header
            cookies:  cookie
            elapsed: 耗时
            msg: 报错信息
            **kwargs:

        Returns:

        """
        request_headers = json.dumps(
            {k: v for k, v in request_headers.items()} if request_headers is not None else {}, ensure_ascii=False
        )
        response_headers = json.dumps(
            {k: v for k, v in response_headers.items()} if response_headers is not None else {}, ensure_ascii=False
        )
        cookies = {k: v for k, v in cookies.items()} if cookies is not None else {}
        cookies = json.dumps(cookies, ensure_ascii=False)
        return {
            "status": status,
            "response": response,
            "status_code": status_code,
            "request_data": AsyncRequest.get_request_data(request_data),
            "response_headers": response_headers,
            "request_headers": request_headers,
            "msg": msg,
            "cost": elapsed,
            "cookies": cookies,
            **kwargs,
        }
