#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: db_api.py
@time: 2023/2/9 19:55
"""
from sanic import Blueprint

from database.get_mongo import create_pydb
from database.get_mysql import mysql_db

db_api = Blueprint("db")


@db_api.get("/createMongoDb")
def create_db(request):
    create_pydb()
    pass


@db_api.get("/mysql")
def create_mysql(request):
    mysql_db()
