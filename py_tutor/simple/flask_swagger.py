#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: flask_swagger.py
@time: 2023/1/17 1:56
"""


from flask import Flask
from flask_siwadoc import SiwaDoc

app = Flask(__name__)

siwa = SiwaDoc(app)



@app.route("/hello", methods=["GET"])
@siwa.doc()
def hello():
    return "hello siwadoc"


if __name__ == '__main__':
    app.run()