#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: class2.py
@time: 2019/7/4 14:15
"""
import string


def main():
    path = '../../resources/1.txt'
    with open(path, 'r') as text:
        words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
        words_index = set(words)
        counts_dict = {index: words.count(index) for index in words_index}
    print(words)
    for word in sorted(counts_dict, key=lambda x: counts_dict[x], reverse=True):
        print('{} -- {} times'.format(word, counts_dict[word]))


if __name__ == "__main__":
    main()
