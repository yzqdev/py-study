#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: get_mysql.py
@time: 2022/12/31 12:33
"""

# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database import constants

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据库连接:
engine = create_engine(f'postgresql+psycopg2://postgres:123456@localhost:5432/{constants.db_name}')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建表
Base.metadata.create_all(engine)


def get_pg():
    # 创建session对象:
    session = DBSession()

    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    users = session.query(User).filter(User.id == '5').all()

    if users:
        # 打印类型和对象的name属性:
        print('type:', type(users))
        print('name:', users[0].name)
    else:
        # 创建新User对象:
        new_user = User(id='5', name='Bob')
        # 添加到session:
        session.add(new_user)
        # 提交即保存到数据库:
        session.commit()
        print("创建完成")

    # 关闭Session:
    session.close()
