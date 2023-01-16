import tkinter
win=tkinter.Tk()
win.title('hello wodk')
win.geometry('400x300')
entry = tkinter.Entry(win)
def showinfo():
    # 获取输入的内容
    print(entry.get())
def main():

    entry.pack()
    button = tkinter.Button(win, text="按钮", command=showinfo)
    button.pack()
    win.mainloop()

if __name__ == '__main__':
    main()