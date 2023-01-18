# coding:utf8
# 参考：https://www.jianshu.com/p/6ca1344a09db
import random
import re
from base64 import b64decode
from zlib import crc32

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTHL, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
}


def get_video_url_api(video_id='v02004190000bjqdaaq0ifkkoafl5rg0'):
    '''取视蘋地iff所在包的uri'''
    r = str(random.random())[2:]
    url_part = "/video/urls/v/l/toutiao/mp4/{}?r={}".format(video_id, r)
    s = crc32(url_part.encode())
    url = "https://ib.365yg.com{}&s={}".format(url_part, s)
    return url


def get_video_url(url):
    # 获取视频地址
    resp = requests.get(url, headers=headers)
    j_resp = resp.json()
    video_url = j_resp['data']['video_list']['video_1']['main_url']
    video_url = b64decode(video_url.encode()).decode()
    return video_url


def get_video_id(url):
    # 获取视频id
    resp = requests.get(url, headers=headers)
    # 获取video_id
    print(resp.text)
    search = re.search("\"vid\":\"([^\"]+)\",", resp.text)
    print(search.group(1))
    return search.group(1)


def main():
    url = "https://www.ixigua.com/id"
    video_id = get_video_id(url)
    if video_id == None:
        print("get video_id error")
        return
    video_url_api = get_video_url_api(video_id)
    print(video_url_api.encode())
    video_url = get_video_url(video_url_api)
    print(video_url)
    return


if __name__ == '__main__':
    main()