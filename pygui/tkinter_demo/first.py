# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('800x600')

var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=15,
             height=2)
# l = tk.Label(window, text='OMG! this is TK!', bg='green', font=('Arial', 12), width=15, height=2)
l.pack()
e = tk.Entry(window, show="^")
e.pack()
on_hit = False
t = tk.Text(window, height=3)

t.pack()
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')


def printpoint():
    v=lb.get(lb.curselection())
    l.config(text='you are fol')
    var.set(v)

b1 = tk.Button(window, text='insertpoint', width=15,
               height=2, command=printpoint)
b1.pack()
var2=tk.StringVar()
var2.set((12,34,56,78))
lb=tk.Listbox(window,listvariable=var2)
listitems=[1,2,3,4]
for er in listitems:
    lb.insert('end',er)
lb.pack()
window.mainloop()
