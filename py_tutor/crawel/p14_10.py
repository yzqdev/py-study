import re

import requests

headers = {
    "Cookie": "_MHYUUID=9fe726a9-bd7d-4906-8550-137214fc8429; UM_distinctid=180a1bb1d4b74c-0185d2e707a8b9-17333273-1fa400-180a1bb1d4c7e8; ltoken=XFX5Sh6CU8lDLTrY1o5ZHTXfOZZw188EfjOdgsqh; ltuid=281049291; mi18nLang=zh-cn; _ga_9TTX3TE5YL=GS1.1.1654372827.8.0.1654372827.0; _ga=GA1.2.1902540976.1651980834; _gid=GA1.2.292957077.1655187625; acw_tc=2f6fc12316551894566741033e7b313db955a0ce7f82721440876c00c5b35f; _gat=1",
    "DS": "1672459395,Saakpn,b303087122b3f3429d80772b00f896de",
    "Host": "www.miyoushe.com",
    "Origin": "https://www.miyoushe.com",
    "Referer": "https://www.miyoushe.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "x-rpc-app_version": "2.43.0",
    "x-rpc-client_type": "4",
    "x-rpc-device_id": "b10eae5c36c0a7df82a0103b875981d6",
}
def open_url(url):
    res = requests.get(url=url, headers=headers)
    print(res.text)
    return res.text


def get_img(html):
    print("hello")
    print(html)
    p = r'<img src="[^"]*\.jpg*"'
    imglist = re.findall(p, html)
    print(imglist)
    for each in imglist:
        print(each)
    print("end")


if __name__ == '__main__':
    url = "https://www.miyoushe.com/ys/home/49"
    get_img(open_url(url))
