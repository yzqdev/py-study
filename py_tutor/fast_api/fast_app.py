#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: main_app.py
@time: 2023/1/7 17:59
"""

import pytz
import uvicorn
from api.controller.fun_controller import fun_router
from api.controller.list_controller import list_router
from api.controller.user_controller import user_router
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from fast_api.api.controller.time_controller import time_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# 路由挂载
app.include_router(user_router, prefix='/user', tags=['检索词联想', ])
app.include_router(list_router, prefix='/list', tags=['列表', ])
app.include_router(fun_router, prefix='/fun', tags=['函数', ])
app.include_router(time_router, prefix='/time', tags=['日期', ])
port = 9600


@app.get("/")
async def root():
    return {"message": "Hello World", "code": 1}


@app.on_event('startup')
async def startup_event():
    scheduler = AsyncIOScheduler(timezone=pytz.utc)
    scheduler.start()
    scheduler.add_job(count_users_task, 'interval', seconds=30, id='job1')


def count_users_task():
    """Count the number of users in the database and save it into the user_counts table."""

    # we are outside of a request context, therefore we cannot rely on ``DBSessionMiddleware``
    # to create a database session for us. Instead, we can use the same ``db`` object and
    # use it as a context manager, like so:

    print(f"http://localhost:{port}/docs")


# 文档 https://www.cnblogs.com/liuweida/p/14324604.html
if __name__ == '__main__':
    # uvicorm.run(文件名:app),不然会出现 ERROR: Error loading ASGI app. Could not import module "main"
    # 启动服务，因为我们这个文件叫做 main.py
    # 所以需要启动 main.py 里面的 app
    # 第一个参数 "main:app" 就表示这个含义
    # 然后是 host 和 port 表示监听的 ip 和端口
    print(f"http://localhost:{port}/docs")
    uvicorn.run("fast_app:app", host="0.0.0.0", port=port )
