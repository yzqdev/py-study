#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: tk_demo.py
@time: 2023/1/20 17:57
"""
from tkinter import Tk,ttk
import tkinter as tk

def main():
    root = Tk()
    frm = tk.Frame(root )
    frm.grid()
    tk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()


if __name__ == "__main__":
    main()
