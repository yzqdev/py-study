
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: read_txt.py
@time: 2021/10/22 21:31
"""
class ReadText:
    def __init__(self):
        self.name = "bb"

    def main(self):
        with open("1.txt", "r+", encoding="gbk") as f:
            content = f.readlines()
            arr = []

            for item in content:
                arr.append(item)
            self.name="aaaa"
            print(arr)




