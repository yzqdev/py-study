#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: flasgger_py.py
@time: 2023/1/17 12:19
"""


from flasgger import Swagger
from flasgger.utils import swag_from
from flask import Blueprint, Flask, jsonify

port=7900
app = Flask(__name__)

example_blueprint = Blueprint("example_blueprint", __name__)


@example_blueprint.route('/usernames/<username>', methods=['GET', 'POST'])

def usernames(username):
    return jsonify({'username': username})


@example_blueprint.route('/usernames2/<username>', methods=['GET', 'POST'])
def usernames2(username):
    """
    This is the summary defined in yaml file
    First line is the summary
    All following lines until the hyphens is added to description
    the format of the first lines until 3 hyphens will be not yaml compliant
    but everything below the 3 hyphens should be.
    ---
    tags:
      - users
    parameters:
      - in: path
        name: username
        type: string
        required: true
    responses:
      200:
        description: A single user item
        schema:
          id: rec_username
          properties:
            username:
              type: string
              description: The name of the user
              default: 'steve-harris'
    """
    return jsonify({'username': username})


@example_blueprint.route('/users', endpoint='user-without-id', methods=['GET'])
@example_blueprint.route('/users/<user_id>', endpoint='user-with-id', methods=['GET'])

def usernames(user_id=None):
    if user_id:
        return jsonify({'user_id': user_id})
    else:
        return jsonify([])


app.register_blueprint(example_blueprint)

swag = Swagger(app)

if __name__ == "__main__":
    print(f"文档地址=>http://localhost:{port}/apidocs/index.html ")
    app.run(port=port,debug=True)
