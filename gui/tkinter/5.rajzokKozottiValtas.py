from tkinter import *

def circle(x, y, r, color="black"):
    can.create_oval(x-r, y-r, x+r, y+r, outline=color)

def figure1():
    can.delete(ALL)
    can.create_line(100, 0, 100, 200, fill='blue')
    can.create_line(0, 100, 200, 100, fill='blue')
    radius = 15
    while radius < 100:
        circle(100, 100, radius)
        radius += 15 

def figure2():
    can.delete(ALL)
    cc =[[100, 100, 80, 'red'], # fej
    [70, 70, 15, 'blue'], # szem
    [130, 70, 15, 'blue'],
    [70, 70, 5, 'black'],
    [130, 70, 5, 'black'],
    [44, 115, 20, 'red'], # arc
    [156, 115, 20, 'red'],
    [100, 95, 15, 'purple'], # orr
    [100, 145, 30, 'purple']] # száj

    i =0
    while i < len(cc): # a lista bejárása
        el = cc[i] # minden elem maga is lista
        circle(el[0], el[1], el[2], el[3])
        i += 1

# foprograms
window = Tk()
can = Canvas(window, width=200, height=200, bg='ivory')
can.pack(side=TOP, padx=5, pady=5)
b1 = Button(window, text='1. abra', command=figure1)
b1.pack(side=LEFT, padx=3, pady=3)
b2 = Button(window, text='2. abra', command=figure2)
b2.pack(side=RIGHT, padx=3, pady=3)
window.mainloop()