#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: CapsuleEnv.py
@time: 2019/4/16 16:44
"""

import time
import sys
import random
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk
UNIT = 40  # pixels
MAZE_H = 600  # grid height
MAZE_W = 600  # grid width
CAPLEN = 9


class CapsuleEnv(root=tk.Tk(),object):
    def __init__(self):
        super(CapsuleEnv, self).__init__()


        self.width = 23
        root.title('maze')
        # self.geometry('600x600')
        self.action_space = ['u', 'd', 'l', 'r']
        #  创建一个Canvas，设置其背景色为白色

        self._build_env()

    def changesize(self):
        height = random.randint(1, 100)
        width = random.randint(400, 600)
        self.cavans.coords(self.rtinit, (height, width, height + 40, width + 40))

    def _build_env(self):
        self.cavans = tk.Canvas(self, bg='white', height=MAZE_H, width=MAZE_W)
        self.btn = tk.Button(self, text='改变大小', command=self.changesize)
        self.rtinit = self.cavans.create_rectangle(120, 120, 160, 160)
        self.rtfinal = self.cavans.create_rectangle(400, 10, 440, 50)

        self.cavans.pack()



if __name__ == '__main__':
    env = CapsuleEnv()
    env.mainloop()
