from tkinter import *

root = Tk()

v = StringVar()


def test1():
    if v.get() == "小甲鱼":
        print("正确！")
        return True
    else:
        print("错误！")
        e1.delete(0, END)
        return False


def test2():
    print("我被调用了......")
    return True


e1 = Entry(root, textvariable=v, validate="focusout",
           validatecommand=test1, invalidcommand=test2)
e2 = Entry(root)
e1.pack(padx=10, pady=10)
e2.pack(padx=10, pady=10)

if __name__ == '__main__':
    mainloop()
