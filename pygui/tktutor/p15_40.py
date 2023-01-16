from tkinter import *

root = Tk()


def callback():
    print("~被调用了~")


# 创建一个弹出菜单
menu = Menu(root, tearoff=False)
menu.add_command(label="撤销", command=callback)
menu.add_command(label="重做", command=callback)

frame = Frame(root, width=512, height=512)
frame.pack()


def popup(event):
    menu.post(event.x_root, event.y_root)


# 绑定鼠标右键
frame.bind("<Button-3>", popup)

mainloop()
