#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: flask_main.py
@time: 2023/1/8 12:48
"""

from flask import Flask

from flask_api.controller.cat_controller import cat

app = Flask(__name__)
port=4500
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/hello')
def hello():
    return 'Hello, World!'
app.register_blueprint(cat, url_prefix='/cat')


if __name__ == '__main__':
    app.run(port=port,debug=True)
