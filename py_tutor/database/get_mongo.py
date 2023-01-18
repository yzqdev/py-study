#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: get_mongo.py
@time: 2022/12/31 12:15
"""
import collections
import datetime
import pprint
import uuid

import bson
import pymongo
import util
from colorama import Back, Fore, Style
from faker import Faker
from random_word import RandomWords

from database import constants

fake = Faker(locale='zh_CN')
r = RandomWords()
# 文档在这里
# https://pymongo.readthedocs.io/en/stable/tutorial.html

connect_str = "mongodb+srv://<username>:<password>@<cluster-address>/test?retryWrites=true&w=majority"
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient[constants.db_name]
dblist = myclient.list_database_names()

post_collection: pymongo.collection.Collection = db.post


def create_user():
    users = []
    for i in range(0, 5):
        user = {
            "nickname": fake.name(),
            "sex": "man",
            "username": fake.email(),
            "uid": util.random_username(6, 10),
            "hobby": fake.sentence()
        }
        users.append(user)
    user_db: pymongo.collection.Collection = db.users
    user_db.insert_many(users)
    pass


def remove_duplicate_cos():
    """
    删除重复记录
    """
    name = post_collection.distinct('name')
    age = post_collection.distinct('age')
    name_age = zip(name, age)

    for name, age in name_age:
        data = post_collection.find_one({'name': name, 'age': age})  # 根据字段查询记录
        post_collection.delete_many({'name': name, 'age': age})  # 删除所有记录
        post_collection.insert_one(data)  # 重新插入记录


def create_post():
    print(f"{Fore.MAGENTA}所有的数据库=>")
    print(dblist)

    if "py_db" in dblist:
        print("数据库已存在！")
    post = {"author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}
    post4 = []
    for item in range(1, 4):
        post4.append({"author": fake.name(),
                      "text": fake.sentence(),
                      "tags": ["mongodb", "python", "pymongo"],
                      "date": datetime.datetime.now()})
    posts: pymongo.collection.Collection = db.posts
    print(f"{Fore.LIGHTYELLOW_EX}删除所有")
    posts.delete_many({})
    default_post = posts.find_one({"author": "Mike"})
    if default_post:
        print(Fore.RED + "post已存在")
    else:

        # 插入一条数据
        post_id = posts.insert_one(post).inserted_id
        print(post_id)
    print(Fore.CYAN + "打印一个")
    # 打印一个
    pprint.pprint(posts.find_one())
    # 插入多个
    posts.insert_many(post4)
    # 打印所有的
    print(Fore.BLUE + '打印所有')
    for post in posts.find():
        pprint.pprint(post)
    print(Fore.YELLOW + str(posts.count_documents({})))


if __name__ == "__main__":
    create_post()
    create_user()
