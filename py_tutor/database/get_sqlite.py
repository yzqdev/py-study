#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: get_sqlite.py
@time: 2022/12/31 15:11
"""
import random

from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database.util import random_username

# 定义数据库路径（不存在会自动创建）
SQLiteURL = 'sqlite:///py_db.db'

# 创建engine，即数据库驱动信息
engine = create_engine(
    url=SQLiteURL,
    echo=True,    # 打开sqlalchemy ORM过程中的详细信息
    connect_args={
        'check_same_thread':False   # 是否多线程
    }
)

# 数据表的基类（定义表结构用）
Base = declarative_base()

# 定义User表结构

class User(Base):
    # User类对象对应表users
    __tablename__='users'
    my_id = Column(Integer,primary_key=True,index=True)
    name = Column(String(32),unique=True,index=True)
    passwd = Column(String(32),index=True)
    is_active = Column(Boolean,default=True)

# 创建表
# checkfirst=True 默认也是 True，即如果数据库存在则不再创建
Base.metadata.create_all(engine, checkfirst=True)
def main():
    # 创建session类对象（建立和数据库的链接）
    session_local = sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False
    )

    # 创建session实例（实例化）
    db = session_local()

    # 创建新的User类实例

    phyger = User(
        # my_id=1,
        name= random_username(6,10),
        passwd='pwd@123'
    )

    # 将phyger实例插入users表中

    db.add(phyger)


    # 提交后才算正式插入数据
    db.commit()

    # 关闭数据库连接
    db.close()

    # 查询数据

    res = db.query(User).all()
    print(res)

    # 条件查询
    user1 = db.query(User).filter_by(my_id=1).first()
    print(user1.name)

    # 关闭数据库连接
    db.close()



if __name__ == "__main__":
    main()

