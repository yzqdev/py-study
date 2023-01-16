#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: entity.py
@time: 2022/12/31 18:00
"""
import uuid

from sqlalchemy import create_engine, Column, String,Date
from sqlalchemy.orm import declarative_base, sessionmaker

# 方法一， 利用sqlalchemy_utils库的create_databse模块
from sqlalchemy_utils import database_exists, create_database, UUIDType

from db import Base

