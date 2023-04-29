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
import aiohttp
from aiohttp import FormData
from config import PikaAppConfig
from custard.time import Moment

from app.core.handler.jsonres import PikaJsonEncoder
from app.enums.RequestBodyEnum import ReqBodyTypeEnum
from app.middleware.oss import OssClient


class AsyncRequest(PikaJsonEncoder):
    def __init__(self, url: str, timeout=15, **kwargs):
        self.url = url
        self.kwargs = kwargs
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self.proxy = (
            f"http://127.0.0.1:{PikaAppConfig.MITMPROXY_PROXY_PORT}" if PikaAppConfig.MITMPROXY_ENABLE_FLAG else None
        )

    def get_cookie(self, session):
        cookies = session.cookie_jar.filter_cookies(self.url)
        return {k: v.value for k, v in cookies.items()}

    def get_data(self, kwargs):
        if kwargs.get("json") is not None:
            return kwargs.get("json")
        return kwargs.get("data")

    async def invoke(self, method: str):
        async with aiohttp.ClientSession(cookie_jar=aiohttp.CookieJar(unsafe=True)) as session:
            start_date = Moment.get_now_time("13timestamp")
            async with session.request(
                method,
                self.url,
                timeout=self.timeout,
                proxy=self.proxy,
                ssl=False,
                **self.kwargs,
            ) as resp:
                finished_date = Moment.get_now_time("13timestamp")
                cost = "%.3f" % (int("%.0f" % (finished_date - start_date)) / 1000)
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

    async def download(self):
        async with aiohttp.ClientSession(cookie_jar=aiohttp.CookieJar(unsafe=True)) as session:
            async with session.request(
                "GET",
                self.url,
                timeout=self.timeout,
                proxy=self.proxy,
                ssl=False,
                **self.kwargs,
            ) as resp:
                if resp.status != 200:
                    raise Exception("download file failed")
                return await resp.content.read()

    @classmethod
    async def probe(cls, url):
        if url.startswith("localhost"):
            url = f"http://{url}"
        if not url.startswith(("http://", "https://")):
            raise Exception("请输入正确的url, 记得带上http哦")

    @classmethod
    async def client(cls, url: str, request_body_type: ReqBodyTypeEnum = ReqBodyTypeEnum.json, timeout=15, **kwargs):
        request_body = kwargs.get("request_body")
        headers = kwargs.get("headers", None)
        content_type_array = [key.lower() == "content-type" for key, value in headers.items()]
        if content_type_array.count(True) > 1:
            raise Exception(f"Content-Type出现{len(content_type_array)}次,请修改后重试,{headers}")
        await cls.probe(url)
        if request_body_type == ReqBodyTypeEnum.json:
            if content_type_array.count(True) == 1 and not content_type_array:
                headers["Content-Type"] = "application/json; charset=UTF-8"
            request_body = cls.safe_json_loads(request_body)
            r = AsyncRequest(url, headers=headers, timeout=timeout, json=request_body)
        elif request_body_type == ReqBodyTypeEnum.form:
            try:
                form_data = None
                if request_body:
                    form_data = FormData()
                    items = cls.safe_json_loads(request_body)
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
                raise Exception(f"解析form-data失败, error: {str(e)}")
        elif request_body_type == ReqBodyTypeEnum.x_form:
            request_body = cls.safe_json_loads(request_body)
            r = AsyncRequest(url, headers=headers, data=request_body, timeout=timeout)
        else:
            # 暂时未支持其他类型
            r = AsyncRequest(url, headers=headers, timeout=timeout)
        return r

    @classmethod
    async def get_resp(cls, resp):
        try:
            data = await resp.json(encoding="utf-8")
            # 说明是json格式
            return cls.safe_json_dumps(data, ensure_ascii=False, indent=4), True
        except:
            data = await resp.text()
            # 说明不是json格式,我们不做loads操作了
            return data, False

    @classmethod
    def get_request_data(cls, request_body):
        if isinstance(request_body, bytes):
            request_body = request_body.decode()
        if isinstance(request_body, FormData):
            request_body = str(request_body)
        if isinstance(request_body, str) or request_body is None:
            return request_body
        return cls.safe_json_dumps(request_body, ensure_ascii=False, indent=4)

    @classmethod
    async def collect(
        cls,
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
        request_headers = cls.safe_json_dumps(
            dict(request_headers.items()) if request_headers is not None else {},
            ensure_ascii=False,
        )
        response_headers = cls.safe_json_dumps(
            dict(response_headers.items()) if response_headers is not None else {},
            ensure_ascii=False,
        )
        cookies = dict(cookies.items()) if cookies is not None else {}
        cookies = cls.safe_json_dumps(cookies, ensure_ascii=False)
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
