#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: comp_page.py
@time: 2023/1/20 20:49
"""
from tkinter import *
from tkinter import ttk


def create_panel():
    m1 = PanedWindow()
    m1.pack(fill=BOTH, expand=1)

    left = Label(m1, text="left pane")
    m1.add(left)

    m2 = PanedWindow(orient=VERTICAL)
    m1.add(m2)

    top = Label(m2, text="top pane")
    m2.add(top)

    bottom = Label(m2, text="bottom pane")
    m2.add(bottom)

    mainloop()


def panel_label():
    m = PanedWindow(orient=VERTICAL)
    m.pack(fill=BOTH, expand=1)

    top = Label(m, text="top pane")
    m.add(top)

    bottom = Label(m, text="bottom pane")
    m.add(bottom)

    m.mainloop()


def check_page():
    root = Tk()

    GIRLS = ["西施", "王昭君", "貂蝉", "杨玉环"]

    v = []

    for girl in GIRLS:
        v.append(IntVar())
        b = Checkbutton(root, text=girl, variable=v[-1])
        b.pack(anchor=W)

    root.mainloop()


def list_box_operation():
    root = Tk()

    # 创建一个空列表
    theLB = Listbox(root, setgrid=True)
    theLB.pack()

    # 往列表里添加数据
    for item in ["鸡蛋", "鸭蛋", "鹅蛋", "李狗蛋"]:
        theLB.insert(END, item)

    theButton = Button(root, text="删除", command=lambda x=theLB: x.delete(ACTIVE))
    theButton.pack()

    root.mainloop()


def create_menu():
    root = Tk()

    def callback():
        print("~被调用了~")

    # 创建一个顶级菜单
    menubar = Menu(root)

    # 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
    filemenu = Menu(menubar, tearoff=False)
    filemenu.add_command(label="打开", command=callback)
    filemenu.add_command(label="保存", command=callback)
    filemenu.add_separator()
    filemenu.add_command(label="退出", command=root.quit)
    menubar.add_cascade(label="文件", menu=filemenu)

    # 创建另一个下拉菜单“编辑”，然后将它添加到顶级菜单中
    editmenu = Menu(menubar, tearoff=False)
    editmenu.add_command(label="剪切", command=callback)
    editmenu.add_command(label="拷贝", command=callback)
    editmenu.add_command(label="粘贴", command=callback)
    menubar.add_cascade(label="编辑", menu=editmenu)

    # 显示菜单
    root.config(menu=menubar)

    root.mainloop()


def create_text():
    root = Tk()

    text = Text(root, width=30, height=5)
    text.pack()

    text.insert(INSERT, "I love FishC.com!")

    text.tag_add("tag1", "1.7", "1.12", "1.14")
    text.tag_add("tag2", "1.7", "1.12", "1.14")
    text.tag_config("tag1", background="yellow", foreground="red")
    text.tag_config("tag2", foreground="blue")

    root.mainloop()


def create_option_menu():
    root = Tk()

    variable = StringVar()
    variable.set("one")

    w = ttk.OptionMenu(root, variable, "one", "two", "three")
    w.pack()

    root.mainloop()
def create_option():
    OPTIONS = [
        "California",
        "458",
        "FF",
        "ENZO",
        "LaFerrari"
    ]

    root = Tk()

    variable = StringVar()
    variable.set(OPTIONS[0])

    w = OptionMenu(root, variable, *OPTIONS)
    w.pack()

    def callback():
        print(variable.get())

    Button(root, text="点我", command=callback).pack()

    root.mainloop()
def func_menu():
    root = Tk()

    def callback():
        print("~被调用了~")

    mb = Menubutton(root, text="点我", relief=RAISED)
    mb.pack()

    filemenu = Menu(mb, tearoff=False)
    filemenu.add_checkbutton(label="打开", command=callback, selectcolor="yellow")
    filemenu.add_command(label="保存", command=callback)
    filemenu.add_separator()
    filemenu.add_command(label="退出", command=root.quit)
    mb.config(menu=filemenu)

    root.mainloop()
def show_info():
    root = Tk()

    Label(root, text="作品：").grid(row=0, column=0)
    Label(root, text="作者：").grid(row=1, column=0)

    e1 = Entry(root)
    e2 = Entry(root)
    e1.grid(row=0, column=1, padx=10, pady=5)
    e2.grid(row=1, column=1, padx=10, pady=5)

    def show():
        print("作品：《%s》" % e1.get())
        print("作品：%s" % e2.get())

    Button(root, text="获取信息", width=10, command=show) \
        .grid(row=3, column=0, sticky=W, padx=10, pady=5)
    Button(root, text="退出", width=10, command=root.quit) \
        .grid(row=3, column=1, sticky=E, padx=10, pady=5)

    root.mainloop()