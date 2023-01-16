
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: utils.py
@time: 2022/1/27 13:04
"""
import os
import re


def main():
    title="我去尼玛 大幅度康师傅"
    if re.search("\s", title):
        print(title)
        title.replace(" ","")
        print(title.replace(" ",""))
    print("--user-data-dir="+os.environ["USERPROFILE"]+"/AppData/Local/Google/Chrome/User Data/Default")


if __name__ == "__main__":
    main()
