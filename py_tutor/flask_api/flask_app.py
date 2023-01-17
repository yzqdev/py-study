#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: flask_app.py
@time: 2023/1/17 20:02
"""
from flask import Flask
from flask_siwadoc import SiwaDoc

app = Flask(__name__)

siwa = SiwaDoc(app, title="siwadocapi", description="一个自动生成openapi文档的库")