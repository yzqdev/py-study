#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: main.py
@time: 2021/10/22 17:05
"""
import os
import sys
import os


def main():
    filename = '../../dist/cat_200_300.jpg'
    print(os.path.getsize(filename))
    print(os.stat(filename))
    print(sys.version)
    pass


cmd = 'ping baidu.com'


def ping():
    r = os.popen(cmd)
    for line in r.readlines():
        print(line)


if __name__ == "__main__":
    ping()
    main()
