# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  gunicorn.py
@Time    :  2022/5/2 3:49 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

import multiprocessing

# debug = True
loglevel = "debug"
bind = "0.0.0.0:7777"
daemon = True
timeout = 60

# 启动的进程数
workers = multiprocessing.cpu_count()
worker_class = "uvicorn.workers.UvicornWorker"
x_forwarded_for_header = "X-FORWARDED-FOR"
