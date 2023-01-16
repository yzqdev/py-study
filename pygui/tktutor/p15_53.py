# 捕获键盘事件
from tkinter import *

root = Tk()


def callback(event):
    print("敲击位置：", repr(event.char))


frame = Frame(root, width=200, height=200)
frame.bind("<Key>", callback)
frame.focus_set()
frame.pack()

if __name__ == '__main__':
    mainloop()
