from tkinter import *
from tkinter import ttk
root = Tk()

# 创建一个空列表
theLB = Listbox(root, height=11)
theLB.pack()

# 往列表里添加数据
for item in range(11):
    theLB.insert(END, item)

mainloop()
