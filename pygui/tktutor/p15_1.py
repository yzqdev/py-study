import tkinter as tk

root = tk.Tk()
root.title("FishC Demo")

theLabel = tk.Label(root, text="我的第二个窗口程序！")
theLabel.pack()

if __name__ == '__main__':
    root.mainloop()
