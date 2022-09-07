# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  system.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  系统
"""
from typing import Optional

from fastapi import Body
from pydantic import BaseModel

from app.enums.ByteSizeEnum import ByteSizeEnum


class DataBaseSchema(BaseModel):
    host: Optional[str] = Body(..., title="主机地址", max_length=ByteSizeEnum.LENGTH_70)
    port: Optional[str] = Body(..., title="端口", max_length=ByteSizeEnum.LENGTH_56)
    user: Optional[str] = Body(..., title="用户名", max_length=ByteSizeEnum.LENGTH_56)
    password: Optional[str] = Body(..., title="密码", max_length=ByteSizeEnum.LENGTH_128)
    name: Optional[str] = Body(..., title="链接的数据库名称", max_length=ByteSizeEnum.LENGTH_56)
    charset: Optional[str] = Body("utf8mb4", title="编码", max_length=ByteSizeEnum.LENGTH_36)
    time_zone: Optional[str] = Body("Asia/Shanghai", title="时区", max_length=ByteSizeEnum.LENGTH_36)


class RedisSchema(BaseModel):
    host: Optional[str] = Body(..., title="主机地址", max_length=ByteSizeEnum.LENGTH_70)
    port: Optional[str] = Body(..., title="端口", max_length=ByteSizeEnum.LENGTH_56)
    auth: Optional[str] = Body(None, title="密码", max_length=ByteSizeEnum.LENGTH_56)
    encoding: Optional[str] = Body("utf-8", title="链接的数据库名称", max_length=ByteSizeEnum.LENGTH_56)
    enable_flag: Optional[bool] = Body(True, title="编码")
    index: Optional[str] = Body(0, title="时区", max_length=ByteSizeEnum.LENGTH_36)
    decode_responses: Optional[bool] = Body(True, title="时区")
    target_max_memory: Optional[str] = Body("572978192", title="时区", max_length=ByteSizeEnum.LENGTH_36)
    max_connections: Optional[str] = Body(100, title="时区", max_length=ByteSizeEnum.LENGTH_36)


class EmailSchema(BaseModel):
    host: Optional[str] = Body(..., title="主机地址", max_length=ByteSizeEnum.LENGTH_70)
    port: Optional[str] = Body(..., title="端口", max_length=ByteSizeEnum.LENGTH_56)
    sender: Optional[str] = Body(..., title="发件人邮箱", max_length=ByteSizeEnum.LENGTH_70)
    password: Optional[str] = Body(..., title="发件人邮箱授权码", max_length=ByteSizeEnum.LENGTH_128)


class JwtSchema(BaseModel):
    secret_key: Optional[str] = Body(..., title="秘钥", max_length=ByteSizeEnum.LENGTH_128)
    md5_salt: Optional[str] = Body(..., title="密盐", max_length=ByteSizeEnum.LENGTH_56)
    mpop: Optional[bool] = Body(True, title="是否启用多点登录")


class MitmproxySchema(BaseModel):
    port: Optional[str] = Body(..., title="端口", max_length=ByteSizeEnum.LENGTH_56)
    enable_flag: Optional[bool] = Body(True, title="启用状态")


class OssSchema(BaseModel):
    type: Optional[str] = Body("aliyun", title="类型", max_length=ByteSizeEnum.LENGTH_56)
    access_key_id: Optional[str] = Body(..., title="访问密钥id", max_length=ByteSizeEnum.LENGTH_128)
    access_key_secret: Optional[str] = Body(..., title="访问密钥的秘钥", max_length=ByteSizeEnum.LENGTH_128)
    bucket_name: Optional[str] = Body(..., title="桶名称", max_length=ByteSizeEnum.LENGTH_128)
    endpoint: Optional[str] = Body(None, title="端点", max_length=ByteSizeEnum.LENGTH_128)


class YapiSchema(BaseModel):
    token: Optional[str] = Body(None, title="token", max_length=ByteSizeEnum.LENGTH_200)


class OtherSchema(BaseModel):
    log_switch: Optional[bool] = Body(True, title="日志开关")


class MsConfigSchema(BaseModel):
    """系统配置"""
    database: DataBaseSchema = Body(None, title="数据库配置")
    redis: RedisSchema = Body(None, title="Redis配置")
    jwt: JwtSchema = Body(None, title="JWT配置")
    email: EmailSchema = Body(None, title="Email配置")
    mitmproxy: MitmproxySchema = Body(None, title="Mitmproxy配置")
    oss: OssSchema = Body(None, title="Oss配置")
    yapi: YapiSchema = Body(None, title="Yapi配置")
    other: OtherSchema = Body(None, title="其它配置")
