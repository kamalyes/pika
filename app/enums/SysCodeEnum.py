# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  ExcCodeEnum.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""


class ExcCodeEnum:
    # Index_Code 1000~2000
    IS_EXISTS_ERROR = 1001  # 存在
    IS_NOT_EXISTS_ERROR = 1002  # 不存在

    # Var_Code 2001~3000
    DYNAMIC_ERROR = 2001  # 获取动态验证码失败
    VAR_ERROR = 2002  # 入参数错误
    FIELD_TYPE_ERROR = 2003  # 入参数据类型错误
    QUERY_RESTRICT_ERROR = 2004  # 频率限制
    WRITE_ERROR = 2008  # 写入错误
    WRITE_NORMAL = 2006  # 写入成功
    READ_NORMAL = 2007  # 读取错误
    DELETE_NORMAL = 2008  # 删除错误
    SQL_OPERATION_ERROR = 2009  # 数据库操作失败
    REDIS_OPERATION_ERROR = 2010  # redis错误

    # Status_Code 3000~5000
    LOGIN_STATUS_NORMAL = 3000  # 登录态正常
    LOGIN_STATUS_HAVE_EXPIRED = 3001  # 登录态失效
    LOGIN_STATUS_AUTH_ERROR = 3002  # 登录态鉴权失败
    ACCOUNT_HAS_NOT_ACTIVATE = 3003  # 账号未激活
    ACCOUNT_HAS_DIS_ENABLED = 3004  # 账号已被禁用
    ACCOUNT_HAS_DELETE = 3005  # 账号已被删除
    PASSWORD_ERROR_COUNT_OUT = 3006  # 密码错误次数过大
    PASSWORD_HAS_EXPIRED = 3007  # 密码已过期
    LOGIN_ERROR = 3008  # 登录失败
    LOGOUT_ERROR = 3009  # 注销失败
    ROSOURCE_USED = 3010  # 资源已被使用
    MALFEASONCE_ERROR = 3011  # 越权操作错误
    ACCOUNT_NOT_EXISTS = 3012
    USER_HAS_USED = 3013  # 用户名已被使用
    EMAIL_NOT_REGISTER = 3015  # email暂未注册使用
    PASSWORD_ERROR = 3016  # 密码错误
    RAND_ALGORITHM_ERROR = 3017  # 随机USER_NO错误
    ENCRYPTED_ERROR = 3018  # 密保错误
    ENCRYPTED_INDEX_ERROR = 3019  # 密保问题下标错误

    # Other_Code 5001~6000
    SEND_EMAIL_ERROR = 5001  # 发送邮件失败
    EMAIL_HAS_USED = 5002  # 邮箱地址已被使用
    EMAIL_CURSOR_ERROR = 5003  # 关闭邮件游标失败
    UNICODE_DECODE_ERROR = 5004  # 密码解密错误

    # 系统相关
    INIT_STATUS_NORMAL = 10000  # 已初始化
    UNKNOWN_ERROR = 10001  # 未知错误
    JWT_ENCODE_ERROR = 10002  # jwt加密失败
