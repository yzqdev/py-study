#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: user_controller.py
@time: 2023/1/7 18:12
"""
from typing import Optional

# 创建路由对象
from fastapi import APIRouter

user_router = APIRouter()


# 定义接口方法
@user_router.post("/all")
async def root(data):
    return {"data": data, "code": 1, "msg": "请求成功"}

@user_router.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@user_router.get("/all")
async def get_all(data):
    return {"data": data, "code": 1, "msg": "请求成功"}
@user_router.delete("/{uid}")
async def del_uid(data):
    return {"data": data, "code": 1, "msg": "请求成功"}