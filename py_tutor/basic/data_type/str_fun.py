#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: str_fun.py
@time: 2023/1/8 15:24
"""
import copy


# 当你不确定你的函数里将要传递多少参数时你可以用*args.例如,它可以传递任意数量的参数:
def print_everything(*args):
    for count, thing in enumerate(args):
        print('{0},{1}'.format(count, thing))


# 相似的, ** kwargs允许你使用没有事先定义的参数名:
def print_every(**kwargs):
    for name, value in kwargs.items():
        print('{0}={1}'.format(name, value))


def main():
    print_everything("apple", 'banana', 'cabbage')
    print_every(apple="fruite", cabbage='vegetable')
    deepcopy()


def deepcopy():
    a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象

    b = a  # 赋值，传对象的引用
    c = copy.copy(a)  # 对象拷贝，浅拷贝
    d = copy.deepcopy(a)  # 对象拷贝，深拷贝

    a.append(5)  # 修改对象a
    a[4].append('c')  # 修改对象a中的['a', 'b']数组对象

    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)

def main():
    pass


if __name__ == "__main__":
    main()
