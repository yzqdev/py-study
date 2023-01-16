#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: closure.py
@time: 2023/1/8 0:15
"""

def sum_late(*args):
    def calc_sum():
        ax=0
        for n in args:
            ax=ax + n
        return ax
    return calc_sum
def logger(func):
    def wrapper(*args, **kw):
        print('主人，我准备开始执行：{} 函数了:'.format(func.__name__))

        # 真正执行的是这行。
        func(*args, **kw)

        print('主人，我执行完啦。')
    return wrapper
@logger
# 等价于show_data=logger(show_data)
def show_data():
    print("hello show data")
    pass
def main():
    # 用一个表达式完成4件事情
    #
    # 1. 遍历旧列表：for n in numbers
    # 2. 对成员进行条件过滤：if n % 2 == 0
    # 3. 修改成员： n * 100
    # 4. 组装新的结果列表
    #
    numbers=[1,2,43,4,5]
    results = [n * 100 for n in numbers if n % 2 == 0]
    print(f'调用sum_late的结果：{sum_late(1, 2, 3, 4)}')
    calc_sum = sum_late(1, 2, 3, 4)
    print(f'调用calc_sum的结果：{calc_sum()}')


if __name__ == "__main__":
    main()
    show_data()
