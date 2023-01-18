#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: FirstCraweller.py
@time: 2019/7/20 21:06
"""

import http.cookiejar
import urllib.request

import pymongo
import requests


class FirstCraweller:
    def __init__(self):
        print('program started')

    def __repr__(self):
        print("pppp")

    def main(self):
        response = urllib.request.urlopen('https://blog.csdn.net/weixin_43499626')
        print(response.read().decode('utf-8'))
        print(response.text)

    def saveasjson(self):
        import json

        dictobj = {
            '小明': {
                'age': 15,
                'city': 'beijing',
            },
            '汤姆': {
                'age': 16,
                'city': 'guangzhou',
            }
        }

        jsObj = json.dumps(dictobj, ensure_ascii=False)
        fileObject = open('jsonFile.json', 'w')
        fileObject.write(jsObj)
        fileObject.close()

    def requesttest1(self):
        # get请求
        response1 = requests.get(url='https://blog.csdn.net/weixin_43499626')
        print(response1.text)  # 打印解码后的返回数据
        # 带参数的requests get请求
        response2 = requests.get(url='https://blog.csdn.net/weixin_43499626',
                                 params={'key1': 'value1', 'key2': 'value2'})
        print(response2.text)

    def saveasscv(self):
        import csv
        with open('student.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['姓名', '年龄', '城市'])
            writer.writerows([['小明', 15, '北京'], ['汤姆', 16, '广州']])

    def savetomongo(self):
        # mongo服务
        client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
        # test数据库
        db = client.test
        # student表,没有自动创建
        student_db = db.student
        student_json = {
            'name': '小明',
            'age': 15,
            'city': '北京'
        }
        student_db.insert(student_json)

    # 表单提交登录 向服务器发送一个post请求并携带相关参数，将服务器返回的cookie保存在本地,cookie是服务器在客户端上的“监视器”，记录了登录信息等。客户端通过识别请求携带的cookie，确定是否登录
    def zhihu(self):
        params = {'username': '18856967709', 'passwd': ''}
        response = requests.post("http://zhihu.com/login", data=params)
        for key, value in response.cookies.items():
            print('key = ', key + ' ||| value :' + value)


if __name__ == "__main__":
    zhihu()
