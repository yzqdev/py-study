import json
import os
import re
import threading
from tkinter import *
from tkinter import messagebox, ttk

import requests
# pillow库
from PIL import Image, ImageTk

from util.utils import get_ua

"""
1.07使用check button 实现下载完打开文件夹操作，注册了enter、esc热键，优化了一些体验
1.08 1.更新了关键字、磁盘、用户判断逻辑
   2.将之前的线程池改为多线程来执行下载操作
1.13说明：如果在下载过程变慢，可能是软件正在解析图片地址或者就是您的网络不行
"""


class WeiBo_pics_Spider(object):
    def __init__(self, start_url):
        self.start_url = start_url

    # 解析出图片地址
    def get_pics_url(self):
        i = 1
        global a_flag
        a_flag = True
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
                                yield img_url
            else:
                # 1.06页数显示出现问题
                t1.insert(END, f'***在第{i}页终止***\n')
                t1.see(END)
                t1.update()
                if r1_var.get() == 1:
                    big_dir = disk + ':/WeiBo_Pics'
                    os.startfile(big_dir)
                break
            i += 1

    # 下载图片
    def download_pics(self, url, filename):
        headers = {'User-Agent': get_ua()}
        r = requests.get(url, headers=headers)
        big_dir = disk + ':/WeiBo_Pics'
        aim_path = big_dir + '/' + user_name_selected
        try:
            os.makedirs(aim_path)
        except:
            pass
        with open(aim_path + '\\' + filename, 'wb') as f:
            f.write(r.content)
            # 保证焦点始终在最下
            t1.see(END)
            # 下载完一张刷新一次 防止界面卡死崩溃
            t1.insert(END, f'{filename}\n')
            window.update()


def wb_search():
    # 先清空lsibox1内容，便于新内容显示
    userListbox.delete(0, END)
    url1 = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D3%26q%3D{}%26t%3D0'
    headers = {'User-Agent': get_ua()}
    key_word = searchTextBox.get()
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
            centerLabel.place(x=120, y=42)
            l3_var.set(f'搜索成功')
            centerLabel['background'] = 'green'
            userListbox.insert(END, screen_name)
        # 否则根据关键字去搜索用户信息，显示在listbox中
        else:
            aim_url = url1.format(key_word)
            r = requests.get(aim_url, headers=headers)
            _json = json.loads(r.text)
            try:
                # 若出现了IndexError则表明没有检索到用户信息
                users = _json['data']['cards'][1].get('card_group')
                relevant_num = len(users)
                centerLabel.place(x=105, y=42)
                l3_var.set(f'搜索到了 {relevant_num} 个用户')
                centerLabel['background'] = 'green'
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
                    userListbox.insert(END, user_name)
            except IndexError:  # 如果没有检索到用户，就会报列表索引错误
                messagebox.showinfo(title='提示', message='没有检索到相关用户，请更换关键字或使用用户id搜索！')
                centerLabel.place(x=85, y=42)
                l3_var.set(f'请更换关键字或用户id搜索！')
                centerLabel['background'] = 'yellow'
                # 没有检索到用户的话，提示之后，e1获得焦点之后，清除用户之前输入
                searchTextBox.bind('WM_TAKE_FOCUS', e1_clear())
    else:  # 处理没有输入关键字
        messagebox.showinfo(title='info', message='请输入关键字！')
        centerLabel.place(x=110, y=42)
        l3_var.set(f'请输入关键字！')
        centerLabel['background'] = 'red'


def wb_pics_parse():
    key_word = searchTextBox.get()
    select_path = c1.get()
    # 1.先判断关键字是否输入
    if len(key_word) != 0:
        # 2.再判断是否选择了磁盘
        if len(select_path) == 1:
            # 3.判断所选路径是否存在
            if not os.path.exists(select_path):
                # 4.判断是否在列表框选择了用户名
                try:
                    # 直接获取选中项目
                    """1.05获取Listbox user_name_selected真费劲"""
                    global user_name_selected
                    user_name_selected = userListbox.get(userListbox.curselection())
                    user_name_index = userListbox.curselection()[0]
                    user_id = user_id_list[user_name_index]
                    container_id = '107603' + str(user_id)
                    start_url = f'https://m.weibo.cn/api/container/getIndex?containerid={container_id}'
                    spider = WeiBo_pics_Spider(start_url)
                    t1.config(state='normal')  # 将Text开启，置为可读可写状态
                    centerLabel.place(x=120, y=42)
                    l3_var.set(f'正在运行......')
                    centerLabel['background'] = 'green'
                    for pic_url in spider.get_pics_url():
                        filename = pic_url.split('/')[-1]
                        # 字符串切割，切割出前10个字符串
                        filename = filename[10:]
                        thread_it(spider.download_pics, pic_url, filename)

                # 搜索后，但是没选择用户，会报TclError错误，此except就用来捕获这个异常
                except TclError:
                    messagebox.showwarning(title='警告', message='请选择一个用户！')
                    centerLabel.place(x=105, y=42)
                    l3_var.set(f'请选择一个用户！')
                    centerLabel['background'] = 'red'

                # 获取当前选中项目(使用索引)
            else:
                messagebox.showwarning(title='警告', message='请检查路径！')
                centerLabel.place(x=80, y=42)
                l3_var.set(f'请检查路径！')
                centerLabel['background'] = 'red'
        else:
            messagebox.showwarning(title='警告', message='您未选择磁盘!')
            centerLabel.place(x=85, y=42)
            l3_var.set(f'请检查是否选择了磁盘！')
            centerLabel['background'] = 'red'
    else:
        messagebox.showwarning(title='警告', message='请输入关键字！')
        centerLabel.place(x=110, y=42)
        l3_var.set(f'请输入关键字！')
        centerLabel['background'] = 'red'


def open_disk():
    disk = c1.get()
    big_dir = disk + ':/WeiBo_Pics'
    if len(disk) == 1:
        try:
            if not os.path.exists(big_dir):
                os.mkdir(big_dir)
            os.startfile(big_dir)
        except:
            messagebox.showwarning(title='警告', message='选中的磁盘不存在！')
            centerLabel.place(x=110, y=42)
            l3_var.set(f'选中的磁盘不存在！')
            centerLabel['background'] = 'red'
    else:
        messagebox.showwarning(title='警告', message='您未选中磁盘！')
        centerLabel.place(x=115, y=42)
        l3_var.set(f'您未选中磁盘！')
        centerLabel['background'] = 'red'


def window_quit():
    ret = messagebox.askyesno(title='提示', message='是否要退出？')
    if ret == True:
        window.destroy()
        window.quit()


def e1_clear():
    searchTextBox.delete(0, END)


def print_path(event):
    # 要使用完整的路径
    global disk
    disk = c1.get()
    disk_path = c1.get() + ':/'
    if len(disk) == 1:
        if os.path.exists(disk_path):
            messagebox.showinfo(title='提示', message=f'文件将存储到：{disk}:/WeiBo_Pics目录下')
        else:
            messagebox.showerror(title='错误', message='选定磁盘不存在!')
            centerLabel.place(x=100, y=42)
            l3_var.set(f'选中的磁盘不存在！')
            centerLabel['background'] = 'red'
    else:
        messagebox.showwarning(title='警告', message='请先选定磁盘！')
        centerLabel.place(x=120, y=42)
        l3_var.set(f'请先选定磁盘！')
        centerLabel['background'] = 'red'


def switch():
    if r1_var.get() == 0:
        r1_var.set(1)
    else:
        r1_var.set(0)


def escape(event):
    window_quit()


def enter(event):
    wb_search()


'''解决程序卡死的重要方法，避免子线程和Ui线程在同一个线程'''


def thread_it(func, *args):
    """将函数打包进线程"""
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.daemon = True
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()


if __name__ == '__main__':
    window = Tk()
    width = 310
    height = 395
    screenWidth = window.winfo_screenwidth()  # 获取显示区域的宽度
    screenHeight = window.winfo_screenheight()  # 获取显示区域的高度
    left = (screenWidth - width) / 2
    top = (screenHeight - height) / 2
    window.geometry("%dx%d+%d+%d" % (width, height, left, top))
    window.resizable(0, 0)
    window.title('微博图片采集工具-v1.08')
    # 设置图标
    ico_path = r'rely/icon.ico'
    window.iconbitmap(ico_path)
    # 插入图片到Label中
    photo = Image.open("rely/weibo.ico")  # 括号里为需要显示在图形化界面里的图片
    photo = photo.resize((150, 40))  # 规定图片大小
    img0 = ImageTk.PhotoImage(photo)
    centerImg = ttk.Label(window, imag=img0, justify='center')
    centerImg.pack()

    l3_var = StringVar()
    centerLabel = ttk.Label(window, background='yellow', textvar=l3_var)
    centerLabel.place(x=120, y=42)
    l3_var.set('还没搜索')

    centerImg = ttk.Label(window, text='关键字或\n用户id：')
    centerImg.place(x=13, y=60)

    searchTextBox = ttk.Entry(window, justify='center')
    searchTextBox.place(x=80, y=65)

    l4 = ttk.Label(window, text='磁盘:')
    l4.place(x=13, y=100)

    disk_list = ['C', 'D', 'E', 'F', 'G', 'H', 'I']
    c1 = ttk.Combobox(window, justify='center', state='readonly', width=17, value=disk_list)
    # Combobox默认选中索引为0的项目 即 C盘
    c1.bind('<<ComboboxSelected>>', print_path)
    c1.place(x=80, y=100)

    r1_var = IntVar()
    r1_var.set(1)  # 默认选中为1
    check1 = Checkbutton(window, text='下载完\n打开文件夹', command=switch)
    check1.place(x=223, y=90)

    searchBtn = ttk.Button(window, text='搜索', command=lambda: thread_it(wb_search), width=7)
    searchBtn.place(x=230, y=63)

    l5 = ttk.Label(window, text='用户列表:')
    l5.place(x=13, y=150)
    lb1_var = StringVar()
    userListbox = Listbox(window, justify='center', listvariable=lb1_var, width=20, height=4)
    userListbox.place(x=80, y=135)

    startBtn = ttk.Button(window, text='开始爬取', command=lambda: thread_it(wb_pics_parse, ), width=7)
    startBtn.place(x=230, y=160)

    statusLabel = ttk.Label(window, text='状态：')
    statusLabel.place(x=13, y=280)

    t1 = Text(window, width=23, font=('times new roman', 10), state='disable')
    t1.place(x=80, y=230, height=140)

    openFolderBtn = ttk.Button(window, text=' 打开\n文件夹', width=7, command=open_disk)
    openFolderBtn.place(x=230, y=230)

    openFolderBtn = ttk.Button(window, text='退出', width=7, command=window_quit)
    openFolderBtn.place(x=230, y=315)

    f1 = ttk.LabelFrame(window)
    f1.place(x=65, y=350)
    statusLabel = ttk.Label(f1, text='敬告：本软件仅供学习交流使用！', foreground='red')
    statusLabel.pack(anchor="w", fill=X)

    # 绑定esc键---退出
    window.bind('<Escape>', escape)
    # 使用return键给输入框Entry绑定enter事件---search搜索
    searchTextBox.bind('<Return>', enter)

    # 加入主窗口销毁事件
    window.protocol('WM_DELETE_WINDOW', window_quit)
    window.mainloop()
