#!/usr/bin/python3
# -*- conding:utf-8 -*-

import csv

FILE = 'test_1.csv'


def tupleread():
    # 读
    with open(FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = [row for row in reader]

    print(rows)
    pass


def dicread():
    with open(FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        column = [row for row in reader]

    print(column)


def dicwrite():
    # 写：追加
    row = ['5', 'hanmeimei', '23', '81']
    out = open("test.csv", "a", newline="")
    csv_writer = csv.writer(out, dialect="excel")
    csv_writer.writerow(row)
    pass


if __name__ == '__main__':
    dicread()
    dicwrite()
    tupleread()
