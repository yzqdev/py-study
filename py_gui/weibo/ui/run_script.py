
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: run_script.py
@time: 2022/1/28 16:49
"""
import sys
import os
def main():
    os.system("pyside6-uic weibo_ui.ui -o weibo_ui.py")
if __name__ == "__main__":
    main()
