#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: deal_csv.py
@time: 2019/7/3 13:36
"""
import csv


def write_csv(path, data):
    with open(path, "w") as f:
        writer = csv.writer(f)
        for rowData in data:
            print("rowData=", rowData)
            writer.writerow(rowData)


def read_csv(path):
    infolist = []
    with open(path, "r") as f:
        allFile = csv.reader(f)
        for row in allFile:
            infolist.append(row)
    return infolist


if __name__ == "__main__":
    path = r"../resources/1.csv"
    write_csv(path, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(read_csv(path))
