#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: Capsule_func.py
@time: 2019/4/17 14:19
"""

import random
import tkinter as tk

MAZE_H=500
MAZE_W=500
root = tk.Tk()
if __name__ == '__main__':
    root.title('simulation')
    root.geometry('600x550')
    cavans = tk.Canvas(root, bg='white', height=MAZE_H, width=MAZE_W)
    cavans.pack()


def changesize():
    height = random.randint(1, 500)
    width = random.randint(1, 500)
    cavans.coords(rtinit, (height, width, height + 40, width + 40))














































btn = tk.Button(root, text='改变大小', command=changesize)
btn.pack()
rtinit = cavans.create_rectangle(120, 120, 160, 160)
rtfinal = cavans.create_rectangle(400, 10, 440, 50)
root.mainloop()
