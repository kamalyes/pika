# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  async_http_client.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

import asyncio
import time

import aiohttp
import requests

url = "https://www.baidu.com"


async def fetchBaidu():
    async with aiohttp.ClientSession() as session:
        resp = await session.get(url)
        text = await resp.text(encoding="utf-8")
        print(text.split("\n")[0])
        await asyncio.sleep(1)


async def main():
    start = time.time()
    await asyncio.gather(*(fetchBaidu() for _ in range(500)))
    print("花费时间:", time.time() - start)


def main2():
    start = time.time()
    session = requests.Session()
    for i in range(200):
        r = session.get(url)
        time.sleep(1)
        print(r.text.split("\n")[0])
    print("花费时间:", time.time() - start)


if __name__ == "__main__":
    asyncio.run(main())
    # main2()
