#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: mock_app.py
@time: 2023/1/5 13:25
"""
import os
from sanic import Sanic
from sanic.response import text, json
from colorama import Fore, Back

from sanic_api.cat_api import bp

app = Sanic("MyHelloWorldApp")
app.blueprint(bp)

@app.get("/")
async def hello_world(request):
    return text("Hello, world.")


@app.get("/json")
async def get_json(request):
    return json({"code": 200, "message": "清清楚楚", "data": request.args})

async def handler(request):
    return text("OK")


app.add_route(handler, "/test")

if __name__ == '__main__':
    port = 8900
    print(f"{Fore.RED}http://localhost:{port}")
    app.run(host="0.0.0.0", port=port)
