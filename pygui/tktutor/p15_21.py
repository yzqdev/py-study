from tkinter import *

root = Tk()

Scale(root, from_=0, to=42).pack()
Scale(root, from_=0, to=200, orient=HORIZONTAL).pack()

if __name__ == '__main__':
    mainloop()
