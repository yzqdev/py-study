#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: create_db_ui.py
@time: 2022/12/31 17:32
"""
import datetime
import pprint
import random
import uuid

from sqlalchemy import create_engine, Column, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker

# 方法一， 利用sqlalchemy_utils库的create_databse模块
from sqlalchemy_utils import database_exists, create_database, UUIDType
from colorama import Fore
from database.db import Base, engine, session_local, User, Employees, Artile, GrainData, Company
from database.util import random_username, rand_int, rand_length
from faker import Faker

# Base.metadata.drop_all(engine)
fake = Faker()


def create_tables():
    "INSERT INTO employees (first_name, last_name, hire_date, gender, birth_date) VALUES (%s, %s, %s, %s, %s)"
    pass


# 创建数据库

def create_db():
    Base.metadata.create_all(engine)
    session = session_local()

    employees = []
    articles = []
    grains = []
    default_companys = ["Microsoft", "Google", "张三粮配", "李四粮食", "王五小麦", "赵六麦子专营", "小米", "微信读书"]
    companys = []
    users = []
    for company in default_companys:
        companys.append(Company(name=company, location="China", create_time=datetime.datetime.now(), leader="yzq"))
    session.add_all(companys)
    session.commit()
    company_models = session.query(Company).filter(Company.leader == 'yzq').all()
    print(f"{Fore.CYAN}获取所有公司")
    for i in company_models:
        print(i.name)
    print(f"{Fore.WHITE}插入数据")
    for item in range(0, 10):
        # grains.append(GrainData(weight=str(rand_length()),price=str(rand_length()),company=fake.company()))
        users.append(User(username=fake.name(), nickname=fake.name(), sex="man", hobby=random_username(6, 10),email=fake.email()))
        grains.append(
            GrainData(weight=str(rand_length()), price=str(rand_length()), company=random.choice(default_companys),
                      company_id=company_models[rand_int(0, 6)].id))
        grains.append(
            GrainData(weight=str(rand_length()), price=str(rand_length()), company=random.choice(default_companys),
                      company_id=company_models[rand_int(0, 6)].id))
        articles.append(Artile(price=3.1415926, is_delete=True, money=10000.1234, language='flask',
                               create_date=datetime.date(2018, 3, 22),
                               create_datetime=datetime.datetime(2018, 3, 22, 22, 51, 00),
                               content=fake.sentence(),
                               create_time=datetime.time(22, 57, 00), content_text='text', long_text=fake.sentence()))
        employees.append(
            Employees(first_name=fake.name(), last_name=fake.name(), gender="man", hire_date=datetime.datetime.now(),
                      birth_date=datetime.datetime.now(), company_id=company_models[rand_int(0, 6)].id))
        employees.append(
            Employees(first_name=fake.name(), last_name=fake.name(), gender="woman", hire_date=datetime.datetime.now(),
                      birth_date=datetime.datetime.now(), company_id=company_models[rand_int(0, 6)].id))

    session.add_all(grains)
    session.add_all(articles)
    session.add_all(users)
    session.add_all(employees)
    session.commit()


def main():
    create_db()


if __name__ == "__main__":
    main()
