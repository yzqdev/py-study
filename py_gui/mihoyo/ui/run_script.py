
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: run_script.py
@time: 2022/1/28 16:49
"""
import os
import sys


def main():
    os.system("pyside6-uic mihoyo_ui.ui -o mihoyo_ui.py")
    os.system("pyside6-uic single_cos.ui -o single_cos.py")
if __name__ == "__main__":
    main()
