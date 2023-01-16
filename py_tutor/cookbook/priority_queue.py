#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: priorityqueue.py
@time: 2019/7/20 19:27
"""
import heapq


class PriorityQueue:
    def __init__(self, name):
        self.name = name
        self._queue = []
        self._index = 0

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


def exec_pop():
    p=PriorityQueue('life')
    p.push(PriorityQueue('p1'),1)
    p.push(PriorityQueue('p2'),5)
    print(p)


if __name__ == '__main__':
    exec_pop()