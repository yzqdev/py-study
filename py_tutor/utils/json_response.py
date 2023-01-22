#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: json_response.py
@time: 2023/1/22 16:01
"""


def json_res(code: int, msg: str, data):
    return {
        "code": code, "msg": msg, "data": data
    }
