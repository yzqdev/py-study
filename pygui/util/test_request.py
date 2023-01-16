
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: test_request.py
@time: 2021/10/19 0:42
"""
import requests
from lxml import etree


def main():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50'}
    start_urls = [
        "https://www.douyin.com/video/7018594690144505118",

    ]
    for i in start_urls:
        res = requests.get(url=i ,headers=headers).text
        print(res)
        print('______________________________________')
        s = etree.HTML(res)

        videolink = s.xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[2]/video/@src")
        textlink=s.xpath("//div[@id='fullscreen_capture_feedback']")

    pass


def download_videofile(video_links):
    root = 'd:/douyin_scrapy/'

    for index in range(len(video_links)):
        file_name = "video" + str(index) + ".mp4"
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
    main()
