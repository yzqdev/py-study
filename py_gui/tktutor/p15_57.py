from tkinter import *

root = Tk()

# column 默认值是 0
Label(root, text="用户名").grid(row=0)
Label(root, text="密码").grid(row=1)

Entry(root).grid(row=0, column=1)
Entry(root, show="*").grid(row=1, column=1)

mainloop()
