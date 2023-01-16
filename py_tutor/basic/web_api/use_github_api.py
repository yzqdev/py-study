#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: class3.py
@time: 2019/7/4 14:26
"""
import httpx
import json
import ssl
import certifi
context=ssl._create_unverified_context()
def drink():
    print('Energy!')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}

class CocaCola:
    formula = ['caffeine', 'sugar', 'water', 'soda']


def main():
    coke = CocaCola()
    drink()
    print(ssl.get_default_verify_paths())

    # 执行API调用并存储响应
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = httpx.get(url, headers=headers,verify=False)
    print("Status code:", r.status_code)
    # 将API响应存储在一个变量中
    response_dict = r.json()
    aa = json.dumps(response_dict, ensure_ascii=False)
    with open("1.json", 'w', encoding='utf-8') as git_api:
        git_api.write(aa)
    # 处理结果


def bianli():
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }
    for name, lang in favorite_languages.items():
        print(name.title() + lang.title())


def numJewelsInStones(J: str, S: str) -> int:
    return sum(S.count(i) for i in J)


if __name__ == "__main__":
    # bianli()
    main()
    a = numJewelsInStones('aA', "adeeaarerAAeer")
    print(a)
