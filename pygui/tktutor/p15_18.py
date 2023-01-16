from tkinter import *

root = Tk()

# 创建一个空列表
theLB = Listbox(root, setgrid=True)
theLB.pack()

# 往列表里添加数据
for item in ["鸡蛋", "鸭蛋", "鹅蛋", "李狗蛋"]:
    theLB.insert(END, item)

theButton = Button(root, text="删除", command=lambda x=theLB: x.delete(ACTIVE))
theButton.pack()

if __name__ == '__main__':
    mainloop()
