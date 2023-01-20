#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: canvas_page.py
@time: 2023/1/20 20:47
"""
from tkinter import  *

def main():
    root = Tk()

    w = Canvas(root, width=200, height=100)
    w.pack()

    line1 = w.create_line(0, 50, 200, 50, fill="yellow")
    line2 = w.create_line(100, 0, 100, 100, fill="red", dash=(4, 4))
    rect1 = w.create_rectangle(50, 25, 150, 75, fill="blue")

    w.coords(line1, 0, 25, 200, 25)
    w.itemconfig(rect1, fill="red")
    w.delete(line2)

    Button(root, text="删除全部", command=(lambda x=ALL: w.delete(x))).pack()

    root.mainloop()
def create_canvas():
    root = Tk()
    w = Canvas(root, width=200, height=100)
    w.pack()

    w.create_line(0, 50, 200, 50, fill="yellow")
    w.create_line(100, 0, 100, 100, fill="red", dash=(4, 4))
    w.create_rectangle(50, 25, 150, 75, fill="blue")

    root.mainloop()

def can():
    root = Tk()

    w = Canvas(root, width=200, height=100)
    w.pack()

    w.create_rectangle(40, 20, 160, 80, dash=(4, 4))
    w.create_oval(70, 20, 130, 80, fill="pink")
    w.create_text(100, 50, text="FishC")

    root.mainloop()
def create_can1():
    root = Tk()

    w = Canvas(root, width=200, height=100, background="red")
    w.pack()

    center_x = 100
    center_y = 50
    r = 50
    m=20
    points = [
        # 左上点
        center_x - int(r * m.sin(2 * m.pi / 5)),
        center_y - int(r * m.cos(2 * m.pi / 5)),
        # 右上点
        center_x + int(r * m.sin(2 * m.pi / 5)),
        center_y - int(r * m.cos(2 * m.pi / 5)),
        # 左下点
        center_x - int(r * m.sin(m.pi / 5)),
        center_y + int(r * m.cos(m.pi / 5)),
        # 顶点
        center_x,
        center_y - r,
        # 右下点
        center_x + int(r * m.sin(m.pi / 5)),
        center_y + int(r * m.cos(m.pi / 5))
    ]

    w.create_polygon(points, outline="", fill="")

    root.mainloop()
def create_can2():
    root = Tk()

    w = Canvas(root, width=200, height=100)
    w.pack()

    w.create_line(0, 0, 200, 100, fill="green", width=3)
    w.create_line(200, 0, 0, 100, fill="green", width=3)
    w.create_rectangle(40, 20, 160, 80, fill="green")
    w.create_rectangle(65, 35, 135, 65, fill="yellow")

    w.create_text(100, 50, text="FishC")

    root.mainloop()