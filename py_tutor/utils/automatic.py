#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: automatic.py
@time: 2019/7/3 22:50
"""
import random
import string


class Automatic:
    def __init__(self):
        print("program started!")

    # 生成一个随机数数组
    def gen_random_num(self):
        start = int(input('请输入起始数字'))
        end = int(input('请输入结束数字')) - 1
        num = int(input('请输入数字个数'))
        resultList = random.sample(range(start, int(end) - 1), num)
        print(resultList)

    # 计算文章中单词数目
    def count_numbers(self):
        inpath = '../infile/' + input("文件名:")
        outpath = '../outfile/' + input("文件名:")
        ar = []
        ao = {}
        with open(inpath, 'r') as intext:
            with open(outpath, 'w', encoding='utf-8') as fw:
                words = [raw_word.strip(string.punctuation).lower() for raw_word in intext.read().split()]
                words_index = set(words)
                counts_dict = {index: words.count(index) for index in words_index}

                for word in sorted(counts_dict, key=lambda x: counts_dict[x], reverse=True):
                    ar.append("'{} ': '{} times'".format(word, counts_dict[word]))

                    ao.pop(word, counts_dict[word])
                fw.write(repr(ar))

    # 去除文件中的多余空行
    def clear_blank_line(self):
        inpath = '../infile/' + input('输入文件名:')
        outpath = '../outfile/' + input('输出文件名:')
        with open(inpath, 'r', encoding='utf-8') as fo:
            with open(outpath, 'w') as fw:
                for line in fo:
                    for line in fo.readlines():
                        if line == '\n':
                            line = line.strip("\n")
                        fw.write(line)
        print("已完成")

    """
    @Author: yanni
    @Description: //TODO 
    生成梳子序列
    @Date: 14:11 2019/7/7
    @Modified By:
    @Param: 
    @return: list
    """

    def gen_custom(self):
        global alist
        alist = []
        arrayname = input("请输入名字:")
        try:
            num = int(input("请输入要生成的序号数:")) - 1
            frontsig = input("输入前缀:")
            endsig = input("输入后缀:")
            for n in range(1, num):
                front = frontsig + arrayname + repr(n) + endsig + ","
                alist.append(front)
                print(front, end='')
        except ValueError as e:
            print("亲输入数字!")
        return alist

