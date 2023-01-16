#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: jiujiu.py
@time: 2019/1/9 16:14
"""

# -*- coding: UTF-8 -*-

# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        # 打印语句中，大括号及其里面的字符 (称作格式化字段) 将会被 .format() 中的参数替换,注意有个点的
        print('{}x{}={}\t'.format(i, j, i * j), end='')
    print()
