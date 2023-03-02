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

from utils.json_response import json_res

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
async def dic_t(id: int, q: Optional[str] = None):  # q不是必须的
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
    dic_from_key = dict.fromkeys(dic_list, '2211')
    return {"dic_first": dic_first, "dic_second": student, "keys": list(stu_first_keys),
            'dic_second_update': dic_update,
            'dic_items': student.items(), 'dicFromKey': dic_from_key}


@list_router.get("/dict3")
async def dict3():  # q不是必须的
    dic_first = dict(one=1, two=2, three=3)
    tinydict = {'Name': 'Zara', 'Age': 7}

    print("Value : %s" % tinydict.keys())
    return {'dic_first': dic_first, "keys": list(tinydict.keys())}


@list_router.get("/dictOrder")
def dic_order():
    from collections import OrderedDict
    favorite_languages = OrderedDict()
    favorite_languages['phil'] = 'python'
    favorite_languages['jen'] = 'python'
    favorite_languages['sarah'] = 'c'
    favorite_languages['edward'] = 'ruby'

    for name, language in favorite_languages.items():
        print(name.title() + "'s favorite language is " + language.title() + ".")
    return favorite_languages


@list_router.get("/github_star")
def github_star():
    import httpx

    # 执行API调用并存储响应
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = httpx.get(url)
    print("Status code:", r.status_code)
    # 将API响应存储在一个变量中
    response_dict = r.json()
    print("Total repositories:", response_dict['total_count'])
    # 探索有关仓库的信息
    repo_dicts = response_dict['items']
    print("Repositories returned:", len(repo_dicts))
    # 研究第一个仓库
    repo_dict = repo_dicts[0]
    print("\nKeys:", len(repo_dict))
    for key in sorted(repo_dict.keys()):
        print(key)
    return json_res(200, "success", response_dict)
