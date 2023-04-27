# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  http_constructor.py
@Time    :  2022/6/10 6:53 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from urllib.parse import urlencode, urljoin
from app.core.constructor.constructor import ConstructorAbstract
from app.core.handler.jsonres import PikaJsonEncoder
from app.crud.itstem.gateway import GatewayDao
from app.middleware.async_ask import AsyncRequest
from app.models.constructor import ConstructorModel


class HttpConstructor(ConstructorAbstract, PikaJsonEncoder):

    @classmethod
    async def run(cls, executor, env, index, path, params, constructor: ConstructorModel, **kwargs):
        try:
            constructor_type_ = cls.get_name(constructor)
            executor.append(f"当前路径: {path}, 第{index + 1}条{constructor_type_}")
            data = cls.safe_loads(constructor.constructor_json)
            base_gateway_, url_, headers = data.get("base_gateway"), data.get("url"), data.get("headers")
            base_gateway = await GatewayDao.query_gateway(env, id=base_gateway_)
            url = f"{base_gateway if base_gateway else ''}{url_}"
            if isinstance(headers, str):
                headers = cls.safe_loads(headers)
            client = await AsyncRequest.client(url=url, content_type=data.get("content_type"),
                                               headers=headers,
                                               request_body=data.get("request_body"))
            resp = await client.invoke(data.get("request_method"))
            executor.append(f"当前{constructor_type_}类型为http, url: {url}")
            if constructor.value:
                params[constructor.value] = resp
            executor.append(f"当前{constructor_type_}返回变量: {constructor.value}\n返回值:\n {resp}\n")
        except Exception as e:
            raise Exception(f"{path}->{constructor.name} 第{index + 1}个{constructor_type_}执行失败: {e}")
