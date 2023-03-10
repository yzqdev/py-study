#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: fun_controller.py
@time: 2023/1/7 23:56
"""
from fastapi import APIRouter

from crawel import github520
from utils.json_response import json_res

fun_router = APIRouter()


def person_info_var(arg, *vartuple):
    print(arg)
    for var in vartuple:
        print(f'我属于不定长参数部分:{var}')
    return


other = {'城市': '北京', '爱好': '编程'}


def per_info(name, number, **kw):
    print(f'名称:{name},学号:{number},其他:{kw}')
    return f'名称:{name},学号:{number},其他:{kw}'


@fun_router.get("/turplevar")
async def fun_a():
    print('------------不带可变参数------------------')
    person_info_var('小萌')
    print('------------带两个可变参数------------------')
    person_info_var('小萌', 21, 'beijing')
    print('------------带5个可变参数----------------')
    person_info_var('小萌', 21, 'beijing', 123, 'shanghai', 'happy')
    data= {
        "person": person_info_var('嘻嘻'),
        'per_info': per_info('小智', 1002, 城市=other['城市'], 爱好=other['爱好'])
    }
    return  json_res(200,"success",data)


@fun_router.get("/tutor")
async def tutor():
    hosts = github520.main(True)
    return {
        "ips": hosts
    }
