#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: siwa_py.py
@time: 2023/1/17 12:24
"""

from flask import Blueprint, Flask
from flask_siwadoc import SiwaDoc

from py_swagger.controller.cat_controller import cats
from py_swagger.siwa_constants import app, siwa

port = 7800



def get_siwa():
    return SiwaDoc(app)


# or
# siwa = SiwaDoc()
# siwa.init_app(app)

@app.route("/hello", methods=["GET"])
@siwa.doc()
def hello():
    return "hello siwadoc"


app.register_blueprint(cats)

if __name__ == '__main__':
    print(f"http://localhost:{port}/docs")
    app.run(port=port, debug=True)
