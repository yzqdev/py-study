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
from click.core import Command

"""
见多命令
https://segmentfault.com/q/1010000043242688
"""


@click.group()
def db() -> Command:
    """
    初始化数据库

    """
    pass


@db.command('drop')
def dropdb():
    """
    删除数据库
    :return:
    """
    click.echo('Dropped the database')
