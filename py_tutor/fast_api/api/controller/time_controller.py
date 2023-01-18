#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: time_controller.py
@time: 2023/1/18 12:30
"""
import fastapi

time_router = fastapi.APIRouter()


@time_router.get("/strFormat")
def str_format():
    import time

    t = (2019, 9, 15, 19, 50, 38, 6, 48, 0)
    t = time.mktime(t)
    print(time.strftime('%b %d %Y %H:%M:%S', time.gmtime(t)))
    return {"data": t}
