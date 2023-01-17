#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: cat_api.py
@time: 2023/1/5 16:16
"""
from uuid import UUID

from sanic import text, json, Blueprint

bp = Blueprint("cat")


@bp.get("/cat/text")
async def get_cat_text(request):
    return json({"new": "cat"})


@bp.get("/foo/<foo_id:uuid>")
async def uuid_handler(request, foo_id: UUID):
    return text("UUID - {}".format(foo_id))


@bp.get("/tag/<tag>")
async def tag_handler(request, tag):
    return text("Tag - {}".format(tag))
