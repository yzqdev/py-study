#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: db.py
@time: 2022/12/31 18:03
"""
import datetime
import uuid
from typing import Any

from sqlalchemy import (DECIMAL, Boolean, Column, Date, DateTime, Enum, Float,
                        ForeignKey, Integer, String, Text, Time, create_engine)
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import declarative_base, sessionmaker
# 方法一， 利用sqlalchemy_utils库的create_databse模块
from sqlalchemy_utils import UUIDType, create_database, database_exists

# 创建对象的基类:


engine = create_engine('mysql+pymysql://root:123456@localhost:3306/py_db')
if not database_exists(engine.url):
    create_database(engine.url)
print(database_exists(engine.url))
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class UserBase(Base):
    # 表的名字:
    __tablename__ = 'user'
    __abstract__ = True
    # 表的结构:
    id = Column(Integer,
                primary_key=True, autoincrement=True)
    nickname = Column(String(200))
    uid = Column(UUIDType(binary=False), default=uuid.uuid4)
    sex = Column(String(8))
    hobby = Column(String(200))
    username = Column(String(200))
    email = Column(String(200))


class GrainData(Base):
    __tablename__ = "grain_data"
    id = Column(UUIDType(binary=False),
                primary_key=True,
                default=uuid.uuid4)
    weight = Column(String(200))
    price = Column(String(200))
    company = Column(String(255))
    company_id = Column(Integer, ForeignKey("company.id"))


class User(UserBase):
    # 表的名字:
    __tablename__ = 'user'


class Artile(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float)
    is_delete = Column(Boolean)
    money = Column(DECIMAL(10, 4))
    language = Column(Enum('python', 'flask'))
    create_date = Column(Date)
    create_datetime = Column(DateTime)
    content = Column(String(100))
    create_time = Column(Time)
    content_text = Column(Text)
    long_text = Column(LONGTEXT)


class Employees(Base):
    __tablename__ = "employees"
    id = Column(UUIDType(binary=False),
                primary_key=True,
                default=uuid.uuid4)
    first_name = Column(String(200))
    last_name = Column(String(200))
    hire_date = Column(DateTime)
    gender = Column(String(8))
    birth_date = Column(DateTime)
    company_id = Column(Integer, ForeignKey("company.id"))


class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200))
    location = Column(String(200))
    create_time = Column(DateTime)
    leader = Column(String(200))

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
