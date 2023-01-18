#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: zip_file.py
@time: 2022/1/30 0:31
"""
import os
import threading
import time
import zipfile


class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)
        time.sleep(1)


def delete_zip():
    file = 'myarchive.zip'
    if os.path.exists(file):
        os.remove(file)


if __name__ == "__main__":
    background = AsyncZip('mydata.txt', 'myarchive.zip')
    background.start()
    print('The main program continues to run in foreground.')
    # 等待线程结束
    background.join()  # Wait for the background task to finish
    del_file=threading.Thread(target=delete_zip)
    del_file.start()
    print('Main program waited until background was done.')
