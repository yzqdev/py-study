#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: flask_main.py
@time: 2023/1/8 12:48
"""
from flasgger import APISpec, Swagger
from flask import Flask, jsonify
from flask_restx import Api

# from flask_siwadoc import SiwaDoc


# from flask_swagger_ui import get_swaggerui_blueprint

from flask_api.controller.cat_controller import cat
from flask_api.flask_app import app, siwa

port = 4500




@app.route('/colors/<palette>/')
@siwa.doc()
def colors(palette):

    all_colors = {
        'cmyk': ['cyan', 'magenta', 'yellow', 'black'],
        'rgb': ['red', 'green', 'blue']
    }
    if palette == 'all':
        result = all_colors
    else:
        result = {palette: all_colors.get(palette)}

    return jsonify(result)


@app.route('/', methods=["GET"])
@siwa.doc()
def hello_world():
    """
    hello
    ---
    Returns:

    """
    return 'Hello, World!'


@app.route("/hello", methods=["GET"])
@siwa.doc()
def hello():
    """
    hello get
    ---



    responses:
      200:
        description: 返回用户信息
        examples:
            {
                code: 0,
                msg: "ok",
                data:
                    {
                        name: "Tom",
                        uid: 1
                    },
            }

    """
    return "hello siwadoc"


app.register_blueprint(cat, url_prefix='/cat')

if __name__ == '__main__':
    print(f"文档地址=>http://localhost:{port}/docs ")  # 注意不要多待杠 /doc/
    app.run(port=port, debug=True)
