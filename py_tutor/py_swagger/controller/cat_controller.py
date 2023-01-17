#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: cats.py
@time: 2023/1/17 12:32
"""
from flask import Blueprint

from py_swagger.siwa_constants import siwa

cats = Blueprint("cats", __name__)


@cats.route("/cats", methods=["GET"])
@siwa.doc(tags=["cat"], group="cat")
def get_cats():
    return "cats"
