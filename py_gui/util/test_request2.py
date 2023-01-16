# 爬取单页内容
import requests
from lxml import etree


def main():
    url = 'https://www.qiushibaike.com/hot/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}


    # 爬取多页内容
    for page in range(9):  # 定义页数为9。
        r = requests.get('https://www.qiushibaike.com/hot/page/{}/'.format(page), headers=headers, timeout=100).text
        s = etree.HTML(r)
        xiaohua = s.xpath('//div[@class="article block untagged mb15 typs_long"]/div/a/img/@src')
        print(xiaohua)
        pass


if __name__ == '__main__':
    main()
