
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: cos_spider.py
@time: 2021/10/19 22:43
"""
import json
import os
import re
from hashlib import md5
from typing import List

import requests

headers = {
    'cookie': '',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50"
}

folder = "d:/images/mihoyo_new/"


# 将图片保存到文件
def save2file(title: str, urls: List[dict]):
    if re.search("\s", title):
        title = title.replace(" ", "")
    if not os.path.exists(folder + title):
        os.mkdir(folder + title)
    for url in urls:
        resp = requests.get(url.get('url'))
        print(url.get('url'))
        file_name = folder + title + '/' + md5(resp.content).hexdigest() + '.jpg'
        if not os.path.exists(file_name):
            with open(file_name, 'wb') as f:
                f.write(resp.content)
                f.close()
        else:
            print('已下载', file_name)


def main(api_url: str):
    res = requests.get(url=api_url, headers=headers)

    cos_dic = json.loads(res.content)
    cos_list: List = cos_dic.get('data').get('list')

    for i in cos_list:
        print(cos_list.index(i))
        print("url=https://bbs.mihoyo.com/ys/article/" + i.get('post').get("post_id"))
        title = i.get('post').get('subject')
        # 文件名不能有特殊字符
        real_title = re.sub(r'[\\\/\:\*\?\"\<\>\|\!\n]', "_", title)
        print(real_title)

        save2file(real_title, i.get('image_list'))


def fetch_cos():
    url_head = 'https://bbs-api.mihoyo.com/post/wapi/getForumPostList?forum_id=49&gids=2&is_good=false&is_hot=true&last_id='
    if not os.path.exists(folder):
        os.mkdir(folder)
    for i in range(1, 10):
        print(i)
        main(url_head + str(i) + '&page_size=20')
    return url_head
