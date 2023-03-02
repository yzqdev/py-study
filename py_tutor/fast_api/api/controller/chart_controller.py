#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: chart_controller.py
@time: 2023/1/22 16:06
"""
from operator import itemgetter

import colorama
import httpx
import pygal
from fastapi import APIRouter
from pygal.style import LightColorizedStyle as LCS
from pygal.style import LightenStyle as LS

chart_route = APIRouter()


@chart_route.get("/getr")
def get_chart():
    # 执行API调用并存储响应
    URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
    r = httpx.get(URL)
    print("Status code:", r.status_code)
    # 将API响应存储在一个变量中
    response_dict = r.json()
    print("Total repositories:", response_dict['total_count'])
    # 研究有关仓库的信息
    repo_dicts = response_dict['items']
    names, stars = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])
        stars.append(repo_dict['stargazers_count'])
    # 可视化
    my_style = LS('#333366', base_style=LCS)
    chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
    chart.title = 'Most-Starred Python Projects on GitHub'
    chart.x_labels = names
    chart.add('', stars)
    chart.render_to_file('../dist/python_repos.svg')


@chart_route.get("/pycal")
def get_pycal():
    my_style = LS('#333366', base_style=LCS)
    chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
    chart.title = 'Python Projects'
    chart.x_labels = ['httpie', 'django', 'flask']
    plot_dicts = [
        {'value': 16101, 'label': 'Description of httpie.'},
        {'value': 15028, 'label': 'Description of django.'},
        {'value': 14798, 'label': 'Description of flask.'},
    ]
    chart.add('', plot_dicts)
    chart.render_to_file('../dist/bar_descriptions.svg')
    return "aaa"


@chart_route.get("/hacknews")
def hack_news():

    # 执行API调用并存储响应
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    r = httpx.get(url,timeout=10000)
    print("Status code:", r.status_code)
    print(f"{colorama.Fore}获取的数据")
    print(r.text)
    # 处理有关每篇文章的信息
    submission_ids = r.json()
    submission_dicts = []
    for submission_id in submission_ids[:30]:
        # 对于每篇文章，都执行一个API调用
        url = ('https://hacker-news.firebaseio.com/v0/item/' +
               str(submission_id) + '.json')
        print(f"{colorama.Fore}{url}")
        submission_r = httpx.get(url)
        print(submission_r.status_code)
        response_dict = submission_r.json()
        submission_dict = {
            'title': response_dict['title'],
            'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
            'comments': response_dict.get('descendants', 0)
        }
        submission_dicts.append(submission_dict)
    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                              reverse=True)
    for submission_dict in submission_dicts:
        print("\nTitle:", submission_dict['title'])
        print("Discussion link:", submission_dict['link'])
        print("Comments:", submission_dict['comments'])
    return submission_dict
