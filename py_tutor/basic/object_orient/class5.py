#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: class5.py
@time: 2019/7/6 13:54
"""

import getpass


class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)


def get1pass():
    user = input("getusername")
    password = getpass.getpass('pasword')
    print(user, password)


def main():
    d = Bag()
    d.add("5")
    print(d.data)
    for key in {'one': 1, 'two': 2}:
        print(key)
    get1pass()


def nmethod():
    m = Reverse('lik')
    print(m.data)


if __name__ == "__main__":
    main()
