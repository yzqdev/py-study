from tkinter import *

root = Tk()

text = Text(root, width=20, height=5)
text.pack()

text.insert(INSERT, "I love FishC.com!")


def show():
    print("哟，我被点了一下~")


b1 = Button(text, text="点我点我", command=show)
text.window_create(INSERT, window=b1)

if __name__ == '__main__':
    mainloop()
