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


app = Flask(__name__)
port = 4500
# siwa = SiwaDoc(app, title="siwadocapi", description="一个自动生成openapi文档的库")
swagger = Swagger(app)
# Create an APISpec


@app.route('/colors/<palette>/')
def colors(palette):
    """示例端点按调色板返回颜色列表
    这是使用文档字符串作为spec。
    ---
    parameters:
      - name: palette
        in: path
        type: string
        enum: ['all', 'rgb', 'cmyk']
        required: true
        default: all
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: 颜色列表（可被调色板过滤）
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """
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
def hello_world():
    """
    hello
    ---
    Returns:

    """
    return 'Hello, World!'


@app.route("/hello", methods=["GET"])
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
    print(f"文档地址=>http://localhost:{port}/doc")  # 注意不要多待杠 /doc/
    app.run(port=port, debug=True)
