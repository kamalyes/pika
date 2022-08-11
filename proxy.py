import asyncio

import uvicorn
from fastapi import FastAPI
from loguru import logger

from app.middleware.proxy import start_proxy
from config import PikaAppConfig

mock = FastAPI()
if PikaAppConfig.MOCK_OPEN:
    asyncio.run(start_proxy(logger))

if __name__ == "__main__":
    uvicorn.run("proxy:mock", host=PikaAppConfig.SERVER_HOST, port=PikaAppConfig.PROXY_PORT,
                reload=False, forwarded_allow_ips="*", workers=1)
