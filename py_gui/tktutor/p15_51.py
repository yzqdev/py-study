from tkinter import *

root = Tk()


def create():
    top = Toplevel()
    top.title("FishC Demo")
    top.attributes("-alpha", 0.8)

    msg = Message(top, text="I love FishC.com")
    msg.pack()


Button(root, text="创建顶级窗口", command=create).pack()

if __name__ == '__main__':
    mainloop()
