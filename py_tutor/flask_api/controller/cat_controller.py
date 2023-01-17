#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: cat_controller.py
@time: 2023/1/8 12:55
"""
from flask import Blueprint



cat = Blueprint('cat', __name__)


@cat.route('/name')
def index():
    return 'Hello, cat!'
