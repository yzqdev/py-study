#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: user_controller.py
@time: 2023/1/7 18:12
"""
from typing import Optional

from faker import Faker

fake = Faker()

# 创建路由对象
from fastapi import APIRouter

list_router = APIRouter()

cur_list = [fake.name() * 8]


# 定义接口方法
@list_router.post("/get")
async def get_list():
    data_list = ['aaa', 'bbb', 3, 5, ['list_aa', 'list_bb']]
    data_list.append("hhhbbb")
    data_list.extend(['bbb', 'csdff'])

    return {"data": data_list, "code": 1, "msg": "请求成功"}


@list_router.post("/all")
async def all_list():
    return {"data": cur_list, "code": 1, "msg": "请求成功"}


@list_router.delete("/del/{id}")
async def del_one(id: str):
    return {"data": cur_list, "code": 1, "msg": "请求成功", 'id': id}


@list_router.post("/addList/{id}")
async def add_list():
    return {"data": cur_list, "code": 1, "msg": "请求成功"}


@list_router.get("/test/{id}")
async def test(id: int, q: Optional[str] = None):  # q不是必须的
    if q:
        return {"id": id, "q": q}
    return {"id": id}


@list_router.get("/dict")
async def dict_api():  # q不是必须的
    a = dict(one=1, two=2, three=3)
    b = {'one': 1, 'two': 2, 'three': 3}
    c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    d = dict([('two', 2), ('one', 1), ('three', 3)])
    e = dict({'three': 3, 'one': 1, 'two': 2})
    f = dict({'one': 1, 'three': 3}, two=2)
    dic_first = dict(one=1, two=2, three=3)

    # dic_first=dict(name='hhh',sex="bbb")
    dic_age = {"age": 44}
    student = {'小萌': '000', '小智': '001', '小萌1': '002'}  # 小萌赋两次值，第一次000，第二次002
    print(f'学生信息：{student}')
    dic_update = {'Name': 'Zara', 'Age': 7}
    tinydict2 = {'Sex': 'female'}
    stu_first_keys = student.keys()
    dic_update.update(tinydict2)
    dic_list = ['a', 'b', 'c']
    dic_from_key = dict.fromkeys(dic_list,'2211')
    return {"dic_first": dic_first, "dic_second": student, "keys": list(stu_first_keys), 'dic_second_update': dic_update,
            'dic_items': student.items(), 'dicFromKey': dic_from_key}


@list_router.get("/dict3")
async def dict3():  # q不是必须的
    dic_first = dict(one=1, two=2, three=3)
    tinydict = {'Name': 'Zara', 'Age': 7}


    print("Value : %s" % tinydict.keys())
    return {'dic_first': dic_first,"keys":list(tinydict.keys())}
