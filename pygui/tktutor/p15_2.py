# p64-2.py
import tkinter as tk


class App:
    def __init__(self, root):
        frame = tk.Frame(root)
        frame.pack()

        self.hi_there = tk.Button(frame, text="打招呼", fg="blue", command=self.say_hi)
        self.hi_there.pack(side=tk.LEFT)

    def say_hi(self):
        print("互联网的广大朋友们大家好，我是小甲鱼！")


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)

    root.mainloop()
