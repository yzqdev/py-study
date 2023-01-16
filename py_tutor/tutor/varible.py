#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: varible.py
@time: 2023/1/8 0:09
"""
x=50
def func_outer(x):
    print(f'x等于:{x}')
    x=2
    print(f'局部变量x变为:{x}')
func_outer(x)
print(f'x一直是:{x}')

def main():
    magicians = ['alice', 'david', 'carolina']
    for magician in magicians:
        print(magician.title() + ", that was a great trick!")
    pass


if __name__ == "__main__":
    main()
