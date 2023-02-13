#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: db_cli.py
@time: 2023/2/12 23:59
"""
import click
import colorama
from click.core import Command

from pytool.util.file_util import get_md5

"""
见多命令
https://segmentfault.com/q/1010000043242688
"""


@click.group("file")
def file_cli() -> Command:
    """
    初始化数据库

    """

    pass


@file_cli.command('md5')
@click.option('--file', help='文件名.')
def md5(file):
    """
    删除数据库
    :return:
    """
    get_md5(file)
