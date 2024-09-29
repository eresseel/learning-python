from tkinter import *
from random import randrange

def drawLine():
    global x1, y1, x2, y2, color
    can1.create_line(x1, y1, x2, y2, width=2, fill=color)

    y2, y1 = y2+10, y1-10

def changeColor():
    global color
    pal=["purple", "cyan", "maroon", "green", "red", "blue", "orange", "yellow"]
    c =randrange(8)
    color = pal[c]

# foorogram
x1, y1, x2, y2 = 10, 190, 190, 100
color = "dark green"

abl1 = Tk()
can1 = Canvas(abl1, bg="dark grey", height=200, width=200)
can1.pack(side=LEFT)
gomb1 = Button(abl1, text="Kilep", command=abl1.quit)
gomb1.pack(side=BOTTOM)
gomb2 = Button(abl1, text="Vonalat rajzol", command=drawLine)
gomb2.pack()
gomb3 = Button(abl1, text="Mas szin", command=changeColor)
gomb3.pack()

abl1.mainloop()
abl1.destroy()