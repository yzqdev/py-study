from tkinter import *



def login_form():
    root = Tk()

    # column 默认值是 0
    Label(root, text="用户名").grid(row=0)
    Label(root, text="密码").grid(row=1)

    Entry(root).grid(row=0, column=1)
    Entry(root, show="*").grid(row=1, column=1)
def check_form():
    root = Tk()

    # 需要一个Tkinter变量，用于表示该按钮是否被选中
    v = IntVar()

    c = Checkbutton(root, text="测试一下", variable=v)
    c.pack()

    # 如果选项被选中，那么变量v被赋值为1，否则为0
    # 我们可以用个Label标签动态地给大家展示：
    l = Label(root, textvariable=v)
    l.pack()
def login_with_hint():
    root = Tk()
    Label(root, text="账号：").grid(row=0, column=0)
    Label(root, text="密码：").grid(row=1, column=0)

    v1 = StringVar()
    v2 = StringVar()

    e1 = Entry(root, textvariable=v1)
    e2 = Entry(root, textvariable=v2, show="￥")
    e1.grid(row=0, column=1, padx=10, pady=5)
    e2.grid(row=1, column=1, padx=10, pady=5)

    def show():
        print("账号：%s" % e1.get())
        print("密码：%s" % e2.get())

    Button(root, text="芝麻开门", width=10, command=show) \
        .grid(row=3, column=0, sticky=W, padx=10, pady=5)
    Button(root, text="退出", width=10, command=root.quit) \
        .grid(row=3, column=1, sticky=E, padx=10, pady=5)

    root.mainloop()
def radio_buttons():
    root = Tk()

    group = LabelFrame(root, text="最好的脚本语言是？", padx=5, pady=5)
    group.pack(padx=10, pady=10)

    LANGS = [
        ("Python", 1),
        ("Perl", 2),
        ("Ruby", 3),
        ("Lua", 4)]

    v = IntVar()
    v.set(1)
    for lang, num in LANGS:
        b = Radiobutton(group, text=lang, variable=v, value=num)
        b.pack(anchor=W)

    mainloop()
def radio_value():
    window = Tk()
    window.title("First Window")
    selected = IntVar()
    lbl = Label(window, text="Show Value")
    rad1 = Radiobutton(window, text="First", value=1, variable=selected)
    rad2 = Radiobutton(window, text="Second", value=2, variable=selected)
    rad3 = Radiobutton(window, text="Third", value=3, variable=selected)

    def clicked():
        lbl.configure(text=selected.get())

    btn = Button(window, text="Click Me", command=clicked)
    rad1.grid(column=0, row=0)
    rad2.grid(column=1, row=0)
    rad3.grid(column=2, row=0)
    btn.grid(column=4, row=0)
    lbl.grid(column=0, row=1)
    window.mainloop()