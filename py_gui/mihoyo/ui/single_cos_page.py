
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: single_cos_page.py
@time: 2022/1/29 4:06
"""
import json
import os

import httpx
from PySide6.QtCore import Slot
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from mihoyo.constant import headers
# from qt_material import apply_stylesheet

from mihoyo.style_constant import extra
from mihoyo.ui.single_cos import Ui_SingleCosWindow
from util.utils import get_ua, thread_it


class SingleCosPage(QMainWindow, Ui_SingleCosWindow):
    def __init__(self):
        super(SingleCosPage, self).__init__()
        self.user_name_selected = None
        self.post_url = None
        self.offset = None
        self.covers=[]
        self.user_id_list = []
        self.file_directory = "d:/images/mihoyo/single_cos/"
        # apply_stylesheet(self, theme='light_cyan.xml',extra=extra)
        # with open("mihoyo/ui/main.qss", "r") as f:
        #     _style = f.read()
        #     self.setStyleSheet(_style)
        self.setupUi(self)
        self.keywordLineEdit.setText("河野")
        self.diskLineEdit.setText(self.file_directory)



    def show(self) -> None:
        super(SingleCosPage, self).show()

    @Slot()
    def on_selectFolderBtn_clicked(self):
        file_dialog = QFileDialog(self)

        self.file_directory = file_dialog.getExistingDirectory(self, dir="d:/tmp", caption="打开文件夹")
        self.diskLineEdit.setText(self.file_directory)

    @Slot()
    def on_openFolderBtn_clicked(self):
        os.startfile(self.file_directory)

    @Slot()
    def on_searchBtn_clicked(self):
        print("点击搜索")
        search_url = f"https://bbs-api.mihoyo.com/user/wapi/searchUser?gids=2&keyword={self.keywordLineEdit.text()}&size=20"

        response = httpx.get(search_url, headers=headers)
        if len(self.keywordLineEdit.text()) != 0:
            print(response.status_code)
            print(response.text)
            if response.status_code == 200:
                _json = json.loads(response.text)

                self.userListWidget.clear()
                for user in _json["data"]["users"]:
                    self.userListWidget.addItem(user["nickname"])
                    self.user_id_list.append(user["uid"])
        else:
            QMessageBox.warning(self, "提示", "请输入关键字！", QMessageBox.Yes)

    @Slot()
    def on_startBtn_clicked(self):
        print("开始爬取...")
        for pic_url in self.get_pics_url():
            filename = pic_url.split('/')[-1]
            # 字符串切割，切割出前10个字符串
            filename = filename[10:]
            thread_it(self.download_pic, pic_url, filename)
        print("cover图")

        for cover in self.covers:
            print(cover)
            filename = cover.split('/')[-1]
            # 字符串切割，切割出前10个字符串
            filename = filename[10:]
            # self.download_pic(cover, filename)
            thread_it(self.download_pic, cover, filename)

        QMessageBox.information(self, "提示", "爬取完成！", QMessageBox.Yes)

    def download_pic(self, url: str, filename: str):
        headers = {'User-Agent': get_ua()}
        r = httpx.get(url, headers=headers)

        aim_path = self.file_directory + self.user_name_selected
        try:
            os.makedirs(aim_path)
        except IOError:
            pass
        with open(aim_path + '\\' + filename, 'wb') as f:
            f.write(r.content)
            # 保证焦点始终在最下
            self.textBrowser.append(f'正在下载：{filename}')
            self.textBrowser.moveCursor(QTextCursor.End)
            # 下载完一张刷新一次 防止界面卡死崩溃
            self.update()

    def get_pics_url(self):
        headers = {'User-Agent': get_ua()}
        self.user_name_selected = self.userListWidget.currentItem().text()
        user_name_index = self.userListWidget.currentIndex().row()
        self.offset = 0
        user_id = self.user_id_list[user_name_index]
        print(user_id)
        i = 1
        if len(user_id) == 0:
            QMessageBox.warning(self, "提示", "请选择用户！", QMessageBox.Yes)
        else:

            while True:
                self.post_url = f"https://bbs-api.mihoyo.com/post/wapi/userPost?gids=2&offset={self.offset}&size=20&uid={user_id}"
                print("请求地址:", self.post_url)
                res = httpx.get(self.post_url, headers=headers)
                _data = json.loads(res.text)
                self.offset = _data["data"]["next_offset"]
                is_last = _data["data"]["is_last"]

                for post in _data["data"]["list"]:
                    if len(post['post']["cover"])>0:
                        self.covers.append(post['post']["cover"])
                    if len(post["post"]["images"]) > 0:

                        for img_url in post["post"]["images"]:
                            print(img_url)
                            yield img_url


                if is_last:
                    break