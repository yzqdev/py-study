import os
import random
import urllib.request


def url_open(url, proxies=None):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50')

    # 使用代理ip访问
    if proxies:
        proxy = random.choice(proxies)
        proxy_support = urllib.request.ProxyHandler({'http': proxy})
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)

    response = urllib.request.urlopen(req)
    html = response.read()

    return html


def find_pic(url):
    html = url_open(url).decode('utf-8')

    # 简单暴力的查找需要的内容，但实用性不佳，下节课有教更好的方法^_^
    a = html.find('class="mainphoto" href="')
    b = html.find('"', a + 24)
    next_url = html[a + 24:b]

    c = html.find('<img src="', b)
    d = html.find('"', c + 10)
    pic_url = html[c + 10:d]

    return next_url, pic_url


def save_pic(pic_url):
    filename = pic_url.split('/')[-1]  # 获得文件的名字
    with open(filename, 'wb') as f:
        img = url_open(pic_url)
        f.write(img)


def download_ooxx(folder='../dist/ox'):
    try:
        os.mkdir(folder)
    except FileExistsError:
        # 如果该文件夹已存在则覆盖保存！
        pass

    os.chdir(folder)

    print("添加代理ip地址（ip:端口号），多个ip地址间用英文的分号隔开！")
    proxies = input("请开始输入：").split(sep=";")

    url = input("请输入URL地址：")

    try:
        pics = int(input("请输入获取的数量："))
    except ValueError:
        pics = 10
        print("输入有误，默认获取10张图片")

    for i in range(pics):
        url, pic = find_pic(url)
        print("正在保存第%d张图片..." % (i + 1))
        save_pic(pic)


if __name__ == '__main__':
    download_ooxx()
