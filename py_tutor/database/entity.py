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

from db import Base
from sqlalchemy import Column, Date, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
# 方法一， 利用sqlalchemy_utils库的create_databse模块
from sqlalchemy_utils import UUIDType, create_database, database_exists
