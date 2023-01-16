#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: multi_request.py
@time: 2021/11/1 13:44
"""
import threading
import time

import httpx
import requests

global t
headers = {
    "cookie": "vaptchaNetway=cn; PHPSESSID=3184491cd93101ce96f33431d56eb34f; Hm_lvt_affdf09dddabcdf2d681acefa474b973=1635733518,1635733840,1635743420,1635777030; ZxYQ_8cea_pc_size_c=0; ZxYQ_8cea_sid=O338tT; ZxYQ_8cea_saltkey=Vwc742F8; ZxYQ_8cea_lastvisit=1635776024; ZxYQ_8cea_sendmail=1; ZxYQ_8cea_lastact=1635779629%09index.php%09; Hm_lpvt_affdf09dddabcdf2d681acefa474b973=1635779631; ZxYQ_8cea_webpush_token=IQAAAACy0kkhAxILIRJLVnb-9w8n3L8kts3FCPgvyxgDrcldRNLIXgErxNgxpNncAsgxQ1MasT9w4o9XH2go_LUbJC9CvnWcQnGcpnTo8Jg1nByHuQ; ZxYQ_8cea_last_message_key=a0412faf4baf0b8acefba13d9dda4691; ZxYQ_8cea_last_formhash=fd053e4557e10fe948c696489b785325",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
}


def say_hello():
    for i in range(100000):
        res = requests.get("https://www.mcbbs.net/thread-696861-1-1.html", headers=headers)
        print(res)


def main():
    say_hello()


if __name__ == "__main__":
    main()
