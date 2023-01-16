#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: deal_xls.py
@time: 2023/1/2 12:26
"""
from colorama import Fore, Back


def main():
    name = input("请输入名字")
    print(f"您的名字是:{name}")
    pass


def list_operate():
    names = ['foo', 'bar']
    for index, s in enumerate(names):
        print(index, s)


def define_tuple():
    print(f"{Fore.MAGENTA} tuple function")
    tup = ("first", "second", "third", 'forth', "fifth")
    print(tup)
    print(type(tup))
    print(f"等于左边,不等于右边")
    print(f"{tup[2:]}")
    print(f"{tup[2:4]}")
    print(f"{tup[:2]}")


def define_dict():
    dic = {
        "username": "yzq",
        "nickname": "yzqdev"
    }
    print(type(dic))
    print(dic)
    print(dic["username"])
    print(dic.get("user", "nouser"))


def define_set():
    set1 = {}


def range_fun():
    for i in range(10):
        print(i)
    for i in range(1, 11):
        print(f"{Fore.CYAN}{i}")
    for i in range(0, 10, 2):
        print(f"{Fore.RED}{i}")


def str_func():
    print(f"{Fore.CYAN} str function")
    default_str = "a big fan of minecraft"

    print(default_str.title())
    print(default_str.center(50, "*"))


if __name__ == "__main__":
    # define_tuple()
    # define_dict()
    range_fun()
    str_func()
