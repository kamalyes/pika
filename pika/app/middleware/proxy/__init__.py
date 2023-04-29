# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  __init__.py
@Time    :  2022/6/17 12:55 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from config import PikaAppConfig

from app.middleware.proxy.record import PikaRecorder
from app.models.mock import MockModel


async def start_proxy(log):
    """
    start mitmproxy server
    :return:
    """
    try:
        from mitmproxy import options
        from mitmproxy.tools.dump import DumpMaster
    except ImportError:
        log.bind(name=None).warning(
            "mitmproxy not installed, Please see: https://docs.mitmproxy.org/stable/overview-installation/",
        )
        return

    addons = [PikaRecorder()]
    try:
        if PikaAppConfig.MITMPROXY_ENABLE_FLAG:
            addons.append(MockModel())
        opts = options.Options(listen_host="0.0.0.0", listen_port=PikaAppConfig.MITMPROXY_PROXY_PORT)
        m = DumpMaster(opts, False, False)
        # remove global block
        block_addon = m.addons.get("block")
        m.addons.remove(block_addon)
        m.addons.add(*addons)
        log.bind(name=None).debug(f"mock server is running at http://0.0.0.0:{PikaAppConfig.MITMPROXY_PROXY_PORT}")
        await m.run()
    except Exception as e:
        log.bind(name=None).debug(f"mock server running failed, if all nodes run failed, please check: {e}")
