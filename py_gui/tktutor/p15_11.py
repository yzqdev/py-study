from tkinter import *

root = Tk()

e = Entry(root)
e.pack(padx=20, pady=20)

e.delete(0, END)
e.insert(0, "默认文本...")

if __name__ == '__main__':
    mainloop()
