#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: tk_main.py
@time: 2023/1/20 17:36
"""

import tkinter as tk
from tkinter import ttk, colorchooser, filedialog, HORIZONTAL, Radiobutton, W, BOTH, END
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import LEFT, Label, RIGHT, CENTER

from tktutor.comp_page import create_menu
from tktutor.tab_window import open_tab_window


def choose_file():
    fileName = filedialog.askopenfilename()
    print(fileName)


def choose_color(label: ttk.Label):
    """
    选择颜色
    """
    fileName = colorchooser.askcolor()
    print(fileName)


def set_tab1(tab1: ttk.Frame, tab_control: ttk.Notebook):
    # LabelFrame using tab1 as the parent
    tab1_first_frame = ttk.LabelFrame(tab1, text='我的python ')
    tab1_first_frame.grid(column=1, row=0, padx=8, pady=4)
    first_tab = ttk.Label(tab1_first_frame, text="Enter a name:")
    first_tab.grid(column=0, row=0, sticky='W')
    ttk.Button(master=tab1, text="新窗口", command=open_tab_window).grid(column=0, row=0, padx=8, pady=4)
    photo = tk.PhotoImage(file="18.png")
    # 创建一个文本Label对象
    hint_label = ttk.Label(tab1_first_frame, text="您所下载的影片含有未成年人限制内容，\n请满18岁后再点击观看！",

                           justify=LEFT,

                           compound=CENTER,
                           font=("华康少女字体", 20),
                           foreground="cyan"
                           )
    hint_label.grid(column=4, row=0, padx=8, pady=4)
    # -----------第二个frame----------
    tab1_second_frame = ttk.LabelFrame(tab1, text='第二个 ')
    tab1_second_frame.grid(column=0, row=1, padx=8, pady=4)
    ttk.Button(tab1_second_frame, text="按钮", command=choose_color).grid(column=0, row=0, padx=8, pady=4)
    ttk.Button(tab1_second_frame, text="文件", command=choose_file).grid(column=1, row=0, padx=8, pady=4)

    # 创建一个图像Label对象
    # 用PhotoImage实例化一个图片对象（支持gif格式的图片）

    tab1_second_label = ttk.Label(first_tab, text="我的第二个窗口程序！")
    tab1_second_label.grid(column=1, row=0, padx=8, pady=4)
    img_label = ttk.Label(first_tab, image=photo)
    img_label.grid(column=0, row=2, padx=8, pady=4)
    color_label = ttk.Label(tab1_second_frame, text="颜色")
    color_label.grid(column=0, row=3, padx=8, pady=4)
    file_label = ttk.Label(tab1_second_frame, text="文件名")
    file_label.grid(column=1, row=3, padx=8, pady=4)
    # ----------------second tab ------------

    # ----------------------tab content -------------
    tab_control.pack(expand=1, fill="both")  # Pack to make visible


def set_tab2(tab2: ttk.Frame, tab_control: ttk.Notebook):
    tab2_first_frame = ttk.LabelFrame(tab2, text="第二个")
    tab2_first_frame.grid(column=0, row=0, padx=8, pady=4)
    first_tab = ttk.Label(tab2_first_frame, text="Enter a name:")
    first_tab.grid(column=0, row=0, sticky='W')
    s1 = tk.Scale(tab2_first_frame, from_=0, to=42)
    s1.grid(column=0, row=3, sticky='W')

    s2 = tk.Scale(tab2_first_frame, from_=0, to=200, orient=HORIZONTAL)
    s2.grid(column=1, row=3, sticky='W')

    def show():
        print(s1.get(), s2.get())

    ttk.Button(tab2_first_frame, text="获取", command=show).grid(column=0, row=4, sticky='W')
    tab_control.pack(expand=1, fill="both")


def set_tab3(tab3: ttk.Frame, tab_control: ttk.Notebook):
    w1 = tk.Message(tab3, text="这是一则消息", width=100)
    w1.pack()

    Label(tab3, bg="red").place(relx=0.5, rely=0.5, relheight=0.75, relwidth=0.75, anchor=CENTER)
    Label(tab3, bg="yellow").place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5, anchor=CENTER)
    Label(tab3, bg="green").place(relx=0.5, rely=0.5, relheight=0.25, relwidth=0.25, anchor=CENTER)
    w2 = tk.Message(tab3, text="这是一则骇人听闻的长长长长长消息！", width=100)
    w2.pack()
    v = tk.IntVar()
    Radiobutton(tab3, text="One", variable=v, value=1).pack(anchor=W)
    Radiobutton(tab3, text="Two", variable=v, value=2).pack(anchor=W)
    Radiobutton(tab3, text="Three", variable=v, value=3).pack(anchor=W)
    Label(tab3, textvariable=v).pack(anchor=W)
    variable = tk.StringVar()
    variable.set("one")

    w = ttk.OptionMenu(tab3, variable, "one", "two", "three")
    w.pack()
    listbox = tk.Listbox(tab3)
    listbox.pack(fill=BOTH, expand=True)

    for i in range(10):
        listbox.insert(END, str(i))
    pass


def set_tab4(tab: ttk.Frame, tab_controller: ttk.Notebook):
    tab4_first_frame = ttk.LabelFrame(tab, text="第二个")
    tab4_first_frame.pack()
    ttk.Button(tab4_first_frame, text="弹框",command=create_menu).grid(column=0, row=0, sticky='W')



win = tk.Tk()
win.title("FishC Demo")
tabControl = ttk.Notebook(win)  # Create Tab Control

tab1 = ttk.Frame(tabControl)  # Create a tab
tabControl.add(tab1, text='Tab 1')  # Add the tab
tab2 = ttk.Frame(tabControl)  # Add a second tab
tabControl.add(tab2, text='Tab 2')  # Make second tab visible

tab3 = ttk.Frame(tabControl)  # Add a second tab
tabControl.add(tab3, text='Tab 3')  # Make second tab visible
tab4 = ttk.Frame(tabControl)  # Add a second tab
tabControl.add(tab4, text='Tab 4')  # Make second tab visible
set_tab1(tab1, tabControl)
set_tab2(tab2, tabControl)
set_tab3(tab3, tabControl)
set_tab4(tab4, tabControl)


def main():
    pass


if __name__ == "__main__":
    win.mainloop()
