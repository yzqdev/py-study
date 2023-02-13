#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: file_util.py
@time: 2023/2/13 14:41
"""
import hashlib
import time


def get_md5(file_name):
    start = time.time()
    with open(file_name, 'rb') as f:
        data = f.read()
    file_md5 = hashlib.md5(data).hexdigest()
    print("md5=>" + file_md5)
    end = time.time()
    print('用时:' + str(end - start) + "s")


