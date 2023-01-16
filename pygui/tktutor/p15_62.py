from tkinter import *
from tkinter import filedialog

root = Tk()


def callback():
    fileName = filedialog.askopenfilename()
    print(fileName)


Button(root, text="打开文件", command=callback).pack()

if __name__ == '__main__':
    mainloop()
