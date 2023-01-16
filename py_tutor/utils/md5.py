#!/usr/bin/python
# -*-coding:utf-8-*-

import hashlib
import sys
import time


def gen_md5(file_name):
    start = time.time()
    with open(file_name, 'rb') as f:
        data = f.read()
    file_md5 = hashlib.md5(data).hexdigest()
    print("md5=>" + file_md5)
    end = time.time()
    print('用时:' + str(end - start) + "s")


def strip_control_characters(self, s):
    word = ''
    for i in s:
        if ord(i) > 31 or ord(i) == 10 or ord(i) == 13:
            word += i
    return word


if __name__ == "__main__":
    file_name = sys.argv[1]
    gen_md5(file_name)
