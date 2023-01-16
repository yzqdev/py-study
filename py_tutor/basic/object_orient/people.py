#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: people.py
@time: 2023/1/2 19:03
"""


class People:
    def __init__(self, age):
        self.age = age

    def eat(self):
        print(f"i eat something")


class Teacher(People):
    sex = 'man'


def main():
    yzq = People(age=22)
    print(yzq.age)
    yang = Teacher(age=30)
    yang.sex="woman"
    print(yang.sex)
    print(Teacher.sex)


if __name__ == "__main__":
    main()
