#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: jsontutor.py
@time: 2019/7/6 11:48
"""
import json


def main():
    import json
    # json.dumps的功能是将字典类型转换为json格式的字符串类型
    data = {'token': 'e5dads5 3455s2', 'verify': True, 'content': '中文'}
    data_json = json.dumps(data)
    print(data_json)
    # 输出：{"token": "e5dads5 3455s2", "verify": true, "content": "\u4e2d\u6587"}
def show_chinese():
    data = {'token': 'e5dads5 3455s2', 'verify': True, 'content': '中文'}
    data_json = json.dumps(data, ensure_ascii=False)
    print(data_json)


if __name__ == "__main__":
    main()
