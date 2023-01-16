#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: util.py
@time: 2022/12/31 15:18
"""
import math
import random
import string


def random_username(user_min, user_max):
    letters1 = string.ascii_letters
    random_len = random.randint(user_min, user_max)
    # 2、获取指定长度的字符串sample(a,b)
    # b的长度需小于等于a
    name_str = ""
    for i in range(1, 3):
        name_str = name_str + letters1
    # 通过join()方法连接字符
    gen_str = ''.join(random.sample(name_str, random_len))
    print(gen_str)
    return gen_str


def rand_int(a, b):
    return random.randint(a, b)


def rand_length():
    return round(10 * random.random(), 2)


def main():
    random_username(6, 10)


if __name__ == "__main__":
    main()
