from tkinter import *

root = Tk()

photo = PhotoImage(file="18.png")
theLabel = Label(root,
                 text="学Python\n到FishC",
                 justify=LEFT,
                 image=photo,
                 compound=CENTER,
                 font=("华康少女字体", 20),
                 fg="white"
                 )
theLabel.pack()

if __name__ == '__main__':
    mainloop()
