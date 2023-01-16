
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: download_video.py
@time: 2021/10/19 23:44
"""
import json
import re


def main():
    f = "lucky.txt"

    a = 8
    with open(f, "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
        for i in range(a):
            file.write(str(i) + "d" + " " + "\n")
        a += 1


if __name__ == "__main__":
    title = '<zheshini>:jjjj*hhh?ss.txt "",kldff / \ \n'
    real_title = re.sub(r'[\\/:*?\"<>|!\n]', "_", title)
    main()
