#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: sarsa.py
@time: 2019/4/18 10:35
"""
states = [1, 2, 3, 4, 5, 6, 7, 8]
actions = ['n', 'e', 'w', 's']
alpha = 0.1
Q = dict()
gamma = 0.5
epsilon = 0.1
for s in states:
    for a in actions:
        key = "%d_%s" % (s, a)
        Q[key]=0
