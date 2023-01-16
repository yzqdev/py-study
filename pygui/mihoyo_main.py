
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: cos_spider.py
@time: 2021/10/19 22:43
"""
import json
import os
import re
import sys
from hashlib import md5

import httpx
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QTextCursor, QIcon
from PySide6.QtWidgets import QFileDialog, QMessageBox

from mihoyo.style_constant import extra
from mihoyo.ui.mihoyo_ui import Ui_Form
from mihoyo.ui.single_cos_page import SingleCosPage
from util.utils import thread_it
# from qt_material import apply_stylesheet
headers = {
    'cookie': '',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50"
}


class MihoyoMain(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(MihoyoMain, self).__init__()
        self.file_directory = "d:/images/mihoyo/home/"
        self.single_cos=""

        # apply_stylesheet(self, theme='light_cyan.xml',extra=extra)
        self.setupUi(self)
        with open("mihoyo/ui/main.qss", "r") as f:
            _style = f.read()
            self.setStyleSheet(_style)
        self.diskTextEdit.setText(self.file_directory)

    @Slot()
    def on_selectFolderPushButton_clicked(self):
        file_dialog = QFileDialog(self)

        self.file_directory = file_dialog.getExistingDirectory(self, dir="d:/tmp", caption="打开文件夹")
        self.diskTextEdit.setText(self.file_directory)

    @Slot()
    def on_homePushButton_clicked(self):
        url_head = 'https://bbs-api.mihoyo.com/post/wapi/getForumPostList?forum_id=49&gids=2&is_good=false&is_hot=true&last_id='
        if not os.path.exists(self.file_directory):
            os.mkdir(self.file_directory)
        for i in range(1, 10):
            print(i)
            thread_it(self.get_cos_imgs, url_head + str(i) + '&page_size=20')
            # self.get_cos_imgs(url_head + str(i) + '&page_size=20')
    @Slot()
    def on_singleCosBtn_clicked(self):
        self.single_cos=SingleCosPage()
        self.single_cos.show()
        pass
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        # message为窗口标题
        # Are you sure to quit?窗口显示内容
        # QtGui.QMessageBox.Yes | QtGui.QMessageBox.No窗口按钮部件
        # QtGui.QMessageBox.No默认焦点停留在NO上
        reply = QMessageBox.question(self, '退出',
                                     "确定要退出吗?",
                                     QMessageBox.Yes |
                                     QMessageBox.No,
                                     QMessageBox.No)
        # 判断返回结果处理相应事项
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # 将图片保存到文件
    def save2file(self, title, urls):
        if not os.path.exists(self.file_directory + title):
            os.mkdir(self.file_directory + title)
        for url in urls:
            print(url.get("url"))
            resp = httpx.get(url.get('url'))
            self.homeTextBrowser.append(url.get('url'))
            self.homeTextBrowser.moveCursor(QTextCursor.End)
            file_name = self.file_directory + title + '/' + md5(resp.content).hexdigest() + '.jpg'
            if not os.path.exists(file_name):
                with open(file_name, 'wb') as f:
                    f.write(resp.content)
                self.homeTextBrowser.append(f'正在下载：{file_name}')
                self.homeTextBrowser.moveCursor(QTextCursor.End)
                # 下载完一张刷新一次 防止界面卡死崩溃
                self.update()

            else:
                print('已下载', file_name)

    def get_cos_imgs(self, api_url):
        res = httpx.get(url=api_url, headers=headers)

        cos_dic = json.loads(res.content)
        cos_list = cos_dic.get('data').get('list')

        for i in cos_list:
            print(cos_list.index(i))
            print("url=https://bbs.mihoyo.com/ys/article/" + i.get('post').get("post_id"))
            title = i.get('post').get('subject')
            # 文件名不能有特殊字符
            real_title = re.sub(r'[\\\/\:\*\?\"\<\>\|\!\n]', "_", title)
            print(real_title)
            self.homeTextBrowser.append(real_title)
            self.save2file(real_title, i.get('image_list'))


def start():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    wig = MihoyoMain()
    wig.setWindowIcon(QIcon('mihoyo/ui/favicon.ico'))
    wig.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    start()
