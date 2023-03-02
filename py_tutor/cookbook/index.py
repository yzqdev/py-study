#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: index.py
@time: 2019/7/20 19:00
"""

import heapq
from collections import deque
from re import search


class Index:
    # 保留最后 N 个元素
    def __init__(self):
        print('program started')

    def search(self, lines, pattern, history=5):
        previous_lines = deque(maxlen=history)
        for line in lines:
            if pattern in line:
                yield line, previous_lines
            previous_lines.append(line)

    def print_largest(self):

        nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
        print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
        print(heapq.nsmallest(3, nums))  #
        portfolio = [
            {'name': 'IBM', 'shares': 100, 'price': 91.1},
            {'name': 'AAPL', 'shares': 50, 'price': 543.22},
            {'name': 'FB', 'shares': 200, 'price': 21.09},
            {'name': 'HPQ', 'shares': 35, 'price': 31.75},
            {'name': 'YHOO', 'shares': 45, 'price': 16.35},
            {'name': 'ACME', 'shares': 75, 'price': 115.65}
        ]
        cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
        expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])


# Example use on a file
if __name__ == '__main__':
    with open(r'somefile.txt') as f:
        for line, prevlines in search(f, 'old', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
