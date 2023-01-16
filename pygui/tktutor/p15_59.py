from tkinter import *

root = Tk()


def callback():
    print("正中靶心")

if __name__ == '__main__':
    Button(root, text="点我", command=callback).place(relx=0.5, rely=0.5, anchor=CENTER)

    mainloop()
