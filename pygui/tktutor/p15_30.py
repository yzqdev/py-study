from tkinter import *
import hashlib

root = Tk()

text = Text(root, width=30, height=5, undo=True)
text.pack()

text.insert(INSERT, "I love FishC.com!")


def show():
    text.edit_undo()


Button(root, text="撤销", command=show).pack()

if __name__ == '__main__':
    mainloop()
