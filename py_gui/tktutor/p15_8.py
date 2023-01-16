from tkinter import *

master = Tk()

v = IntVar()

if __name__ == '__main__':
    Radiobutton(master, text="One", variable=v, value=1).pack(anchor=W)
    Radiobutton(master, text="Two", variable=v, value=2).pack(anchor=W)
    Radiobutton(master, text="Three", variable=v, value=3).pack(anchor=W)

    mainloop()
