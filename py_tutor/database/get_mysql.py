#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: get_mysql.py
@time: 2022/12/31 12:33
"""
from typing import Any

from faker import Faker
# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from colorama import Fore, Back
from database import db, constants
from database.db import Base
from database.util import random_username

fake = Faker()


# 创建对象的基类:
# Base = declarative_base()


# 定义User对象:
class UserSql(db.UserBase):
    # 表的名字:
    __tablename__ = 'user_sql'
    deleted = Column(String(200))


# 初始化数据库连接:
engine = create_engine(f'mysql+pymysql://root:123456@localhost:3306/{constants.db_name}')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
Base.metadata.drop_all(engine)
# 创建表
Base.metadata.create_all(engine)


def main():
    # 创建session对象:
    session = DBSession()

    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    users = session.query(UserSql).filter(UserSql.sex == "man").all()

    print("获取所有user")
    print(users)
    if users:
        # 打印类型和对象的name属性:
        print(f'type:{type(users)}')
        print(f"name:{users[0].username}")
    else:
        # 创建新User对象:
        users2 = []
        for i in range(0, 10):
            users2.append(UserSql(username=fake.name(), nickname=fake.name(), sex="man", hobby=random_username(6, 10),
                                  deleted="false", email=fake.email()))
        # 添加到session:
        session.add_all(users2)
        # 提交即保存到数据库:
        session.commit()
        print("创建完成")

    # 关闭Session:
    session.close()


if __name__ == "__main__":
    main()
