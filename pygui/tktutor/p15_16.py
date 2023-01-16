from tkinter import *

root = Tk()

v = StringVar()


def test(content, reason, name):
    if content == "小甲鱼":
        print("正确！")
        print(content, reason, name)
        return True
    else:
        print("错误！")
        print(content, reason, name)
        return False


testCMD = root.register(test)
e1 = Entry(root, textvariable=v, validate="focusout",
           validatecommand=(testCMD, '%P', '%v', '%W'))
e2 = Entry(root)
e1.pack(padx=10, pady=10)
e2.pack(padx=10, pady=10)

if __name__ == '__main__':
    mainloop()
