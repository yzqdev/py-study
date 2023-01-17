#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: constants.py
@time: 2023/1/17 12:34
"""
from flask import Flask
from flask_siwadoc import SiwaDoc

app = Flask(__name__)
siwa = SiwaDoc(app)
