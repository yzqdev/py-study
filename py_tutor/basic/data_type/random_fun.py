#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: random_fun.py
@time: 2023/1/2 18:58
"""
import random


def main():
    default_companys = ["Microsoft", "Google", "张三粮配", "李四粮食", "王五小麦", "赵六麦子专营", "小米", "微信读书"]
    print(random.choice(default_companys))
    print(random.sample(default_companys,2))
    random.shuffle(default_companys)
    print(default_companys)
    pass


if __name__ == "__main__":
    main()
