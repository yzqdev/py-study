
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: download_video.py
@time: 2021/10/19 0:03
"""

import requests


def download_videofile(video_links):
    root = 'd:/tmp/'
    index: int
    for index in range(len(video_links)):
        file_name = "video" + str(index)+".mp4"
        print("文件下载:%s" % file_name)
        r = requests.get(video_links[index], stream=True)
        with open(root + file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

        print("%s 下载完成!\n" % file_name)
    print("所有视频下载完成!")
    return


if __name__ == "__main__":
    links = [
        '']
    download_videofile(links)
