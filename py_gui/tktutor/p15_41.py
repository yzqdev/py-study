from tkinter import *

root = Tk()


def callback():
    print("~被调用了~")


# 创建一个顶级菜单
menubar = Menu(root)

# 创建 checkbutton 关联变量
openVar = IntVar()
saveVar = IntVar()
exitVar = IntVar()

# 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
filemenu = Menu(menubar, tearoff=True)
filemenu.add_checkbutton(label="打开", command=callback, variable=openVar)
filemenu.add_checkbutton(label="保存", command=callback, variable=saveVar)
filemenu.add_separator()
filemenu.add_checkbutton(label="退出", command=root.quit, variable=exitVar)
menubar.add_cascade(label="文件", menu=filemenu)

# 创建 radiobutton 关联变量
editVar = IntVar()
editVar.set(1)

# 创建另一个下拉菜单“编辑”，然后将它添加到顶级菜单中
editmenu = Menu(menubar, tearoff=True)
editmenu.add_radiobutton(label="剪切", command=callback, variable=editVar, value=1)
editmenu.add_radiobutton(label="拷贝", command=callback, variable=editVar, value=2)
editmenu.add_radiobutton(label="粘贴", command=callback, variable=editVar, value=3)
menubar.add_cascade(label="编辑", menu=editmenu)

# 显示菜单
root.config(menu=menubar)

if __name__ == '__main__':
    root.mainloop()
