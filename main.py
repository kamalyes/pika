# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
"""
# FileName： main.py
# Author : YuYanQing
# Desc: PyCharm
# Date： 2021/9/21 0:11
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/hello", name="HelloWord Name",description="HelloWord Description")
async def index():
    return {"key":"HelloWord"}