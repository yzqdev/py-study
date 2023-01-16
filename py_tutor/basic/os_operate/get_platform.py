#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: get_platform.py
@time: 2023/1/2 19:09
"""
import os
import platform


def main():
    print(platform.machine())
    print(platform.version())
    print(platform.processor())
    print(platform.node(),platform.architecture())
    print(os.getcwd())
    print(os.listdir("."))
    pass


if __name__ == "__main__":
    main()
