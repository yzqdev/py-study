#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: pymysqltutor.py
@time: 2019/7/3 22:16
"""
from datetime import date, datetime, timedelta

import pymysql

# 连接配置信息
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'py_db',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}
# 创建连接
connection = pymysql.connect(**config)

# 获取明天的时间
tomorrow = datetime.now().date() + timedelta(days=1)


def insert_employee():
    # 执行sql语句
    try:
        with connection.cursor() as cursor:
            # 执行sql语句，插入记录
            sql = 'INSERT INTO employees (first_name, last_name, hire_date, gender, birth_date) VALUES (%s, %s, %s, %s, %s)'
            cursor.execute(sql, ('Robin', 'Zhyea', tomorrow, 'M', date(1989, 6, 14)));
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    except:
        # 发生错误时回滚
        connection.rollback()
    finally:
        connection.close();


def search_employee():
    # 执行sql语句
    try:
        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            # 获取雇佣日期

            sql = 'SELECT first_name, last_name, hire_date FROM employees '
            cursor.execute(sql)
            # 获取查询结果
            result = cursor.fetchone()
            print(result)
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    except:
        # 发生错误时回滚
        connection.rollback()

    finally:
        connection.close();


def update_employee():
    try:
        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            # 获取雇佣日期

            sql = 'SELECT first_name, last_name, hire_date FROM employees '
            cursor.execute(sql)
            # 获取查询结果
            result = cursor.fetchone()
            print(result)
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    except:
        # 发生错误时回滚
        connection.rollback()
    finally:
        connection.close();


if __name__ == "__main__":
    search_employee()
