
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: weibo_pic_spider.py
@time: 2022/1/28 19:12
"""
import json
import os
import re
import sys

import requests
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon, QKeyEvent, Qt, QTextCursor
from PySide6.QtWidgets import QFileDialog, QListWidgetItem, QMessageBox

from util.utils import get_ua, thread_it
from weibo.ui.weibo_ui import Ui_Form

global select_path




class Wig(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Wig, self).__init__()

        self.start_url = ""
        self.setupUi(self)  # 初始化UI界面
        self.userListWidget.itemClicked.connect(self.on_userList_clicked)
        # self.keywordLineEdit.keyPressEvent()
        # self.keywordLineEdit.setText("银临")
    def on_keywordLineEdit_keyPressEvent(self,e:QKeyEvent):
        if e.key()==Qt.Key_Enter:
            self.searchPushButton.click()
    @Slot()
    def on_selectFolderPushButton_clicked(self):

        file_dialog = QFileDialog(self)
        file_directory = file_dialog.getExistingDirectory(self, dir="d:/tmp", caption="标题")
        self.diskLineEdit.setText(file_directory)

    @Slot()
    def on_searchPushButton_clicked(self):
        print("searching")
        url1 = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D3%26q%3D{}%26t%3D0'
        headers = {'User-Agent': get_ua()}
        key_word = self.keywordLineEdit.text()
        global user_id_list
        user_id_list = list()
        if len(key_word) != 0:
            # 若用户输入了user_id，则去获取screen_name
            if re.match('\d{10}', key_word):
                user_id_list.append(key_word)
                url2 = f'https://m.weibo.cn/api/container/getIndex?uid={key_word}&containerid=100505{key_word}'
                r1 = requests.get(url2, headers=headers)
                _data = json.loads(r1.text)
                screen_name = _data['data']['userInfo'].get('screen_name')

                self.infoLabel.setText(f'搜索成功')
                self.infoLabel.setStyleSheet("background: green")
                QListWidgetItem(screen_name, self.userListWidget)

            # 否则根据关键字去搜索用户信息，显示在listbox中
            else:
                aim_url = url1.format(key_word)
                r = requests.get(aim_url, headers=headers)
                _json = json.loads(r.text)
                try:
                    # 若出现了IndexError则表明没有检索到用户信息
                    users = _json['data']['cards'][1].get('card_group')
                    relevant_num = len(users)

                    self.infoLabel.setText(f'搜索到了 {relevant_num} 个用户')
                    self.infoLabel.setStyleSheet("background: green")
                    for user_ in users:
                        user_info = user_.get('user')
                        user_name = user_info.get('screen_name')
                        id = user_info.get('id')
                        """
                        1.02的一种思路，使用一个列表存储screen_name和uid，两者用;(自定义字符，但应避免较少冲突)
                        当获取Uid时，直接切割字符串，取Listbox所选项索引，按索引在列表表值（uid）
                        #使用字符串拼接 格式：screen_name+';'+str(id)
                        # user_data = user_name + ';' + str(id)
                        """
                        user_id_list.append(id)
                        QListWidgetItem(user_name, self.userListWidget)
                except IndexError:  # 如果没有检索到用户，就会报列表索引错误
                    box = QMessageBox(QMessageBox.Warning, "提示", '没有检索到相关用户，请更换关键字或使用用户id搜索！', QMessageBox.NoButton,
                                      self)
                    self.infoLabel.setText(f'请更换关键字或用户id搜索！')
                    self.infoLabel.setStyleSheet("background: yellow")
                    # 没有检索到用户的话，提示之后，e1获得焦点之后，清除用户之前输入
                    # searchTextBox.bind('WM_TAKE_FOCUS', e1_clear())
        else:  # 处理没有输入关键字
            QMessageBox.warning(self, "提示", "请输入关键字！", QMessageBox.Yes)
            self.infoLabel.setText(f'请输入关键字！')
            self.infoLabel.setStyleSheet("background: red")

    @Slot()
    def on_startPushButton_clicked(self):
        key_word = self.keywordLineEdit.text()
        global select_path
        select_path = self.diskLineEdit.text()
        # 1.先判断关键字是否输入
        if len(key_word) != 0:
            # 2.再判断是否选择了磁盘
            if len(select_path) > 1:
                # 3.判断所选路径是否存在
                if not os.path.exists(select_path):
                    os.mkdir(select_path)
                if os.path.exists(select_path):
                    # 4.判断是否在列表框选择了用户名
                    try:
                        # 直接获取选中项目
                        """1.05获取Listbox user_name_selected真费劲"""
                        global user_name_selected
                        user_name_selected = self.userListWidget.currentItem().text()
                        user_name_index = self.userListWidget.currentIndex().row()

                        user_id = user_id_list[user_name_index]
                        container_id = '107603' + str(user_id)
                        start_url = f'https://m.weibo.cn/api/container/getIndex?containerid={container_id}'
                        self.start_url = start_url
                        # t1.config(state='normal')  # 将Text开启，置为可读可写状态
                        print(start_url)
                        self.infoLabel.setText(f'正在运行......')
                        self.infoLabel.setStyleSheet("background:green")

                        for pic_url in self.get_pics_url():
                            filename = pic_url.split('/')[-1]
                            # 字符串切割，切割出前10个字符串
                            filename = filename[10:]
                            thread_it(self.download_pics, pic_url, filename)

                    # 搜索后，但是没选择用户，会报TclError错误，此except就用来捕获这个异常
                    except Exception:
                        QMessageBox.warning(self, "警告", "请选择一个用户!", QMessageBox.Ok)
                        self.infoLabel.setText(f'请选择一个用户！')
                        self.infoLabel.setStyleSheet("background:red")

                    # 获取当前选中项目(使用索引)
                else:
                    QMessageBox.warning(self, "警告", "请检查路径!", QMessageBox.Ok)
                    self.infoLabel.setText(f'请检查路径！')
                    self.infoLabel.setStyleSheet("background:red")
            else:
                QMessageBox.warning(self, "警告", "您未选择磁盘!", QMessageBox.Ok)
                self.infoLabel.setText(f'请检查是否选择了磁盘！')
                self.infoLabel.setStyleSheet("background:red")
        else:
            QMessageBox.warning(self, "警告", "请输入关键字!", QMessageBox.Ok)
            self.infoLabel.setText(f'请输入关键字！')
            self.infoLabel.setStyleSheet("background:red")

    def on_userList_clicked(self):

        if len(self.diskLineEdit.text()) > 1:
            if os.path.exists(self.diskLineEdit.text()):
                QMessageBox.warning(self, "提示", f'文件将存储到：{self.diskLineEdit.text()}目录下')
            else:
                QMessageBox.warning(self, title='错误', text='选定磁盘不存在!')
                self.infoLabel.setText(f'选中的磁盘不存在！')
                self.infoLabel.setStyleSheet("background:red")
        else:
            QMessageBox.warning(self, "警告", "请先选择目录")
            self.infoLabel.setText(f'请先选定磁盘！')
            self.infoLabel.setStyleSheet("background:red")

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

    # 解析出图片地址
    def get_pics_url(self):
        i = 1
        global a_flag
        a_flag = True
        global urls
        urls = ""
        while True:
            url = self.start_url + '&page={}'.format(i)
            headers = {'User-Agent': get_ua()}
            r = requests.get(url, headers=headers)
            _json = json.loads(r.text)
            items = _json["data"]["cards"]
            flag = _json['ok']
            if flag == 1 and a_flag:  # 爬取数据标志+一个手动控制标志
                for v in items:
                    picslist = v.get('mblog')
                    if picslist is not None:
                        img_urls = picslist.get('pics')
                        if img_urls != None:
                            for img_url_ in img_urls:
                                img_url = img_url_['large']['url']
                                urls += img_url + "\n"
                                yield img_url
            else:
                print("结束了")
                # 1.06页数显示出现问题
                self.statusLabel.setText(f'***在第{i}页终止***\n')

                # t1.insert(END, f'***在第{i}页终止***\n')
                # t1.see(END)
                # t1.update()
                # if r1_var.get() == 1:

                self.statusTextBrowser.moveCursor(QTextCursor.End)
                self.update()
                big_dir = self.diskLineEdit.text() + '/' + user_name_selected
                with open(big_dir + '/' + 'urls.txt', 'w', encoding='utf-8') as f:
                    f.write(urls)

                os.startfile(big_dir)
                break
            i += 1
        # return urls

    # 下载图片
    def download_pics(self, url: str, filename: str):
        headers = {'User-Agent': get_ua()}
        r = requests.get(url, headers=headers)

        aim_path = select_path + '/' + user_name_selected
        try:
            os.makedirs(aim_path)
        except:
            pass
        with open(aim_path + '\\' + filename, 'wb') as f:
            f.write(r.content)
            # 保证焦点始终在最下
            self.statusTextBrowser.append(f'正在下载：{filename}')
            self.statusTextBrowser.moveCursor(QTextCursor.End)
            # 下载完一张刷新一次 防止界面卡死崩溃
            self.update()


def close_win(wig):
    QMessageBox.warning(wig, "提示", "程序将在5秒后退出！", QMessageBox.Ok)


def main():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    wig = Wig()
    wig.setWindowIcon(QIcon("rely/weibo.ico"))
    wig.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
