# -*- coding: Latin-1 -*-
from tkinter import *
def nyomtat():
    ch1 = e.get() # az Entry widget egy utf8 stringet ad vissz
    ch2 = ch1.encode("Latin-1") # utf8 -> Latin-1 konverzió
    print (ch2)

f = Tk()
e = Entry(f)
e.pack()
Button(f, text ="kiírni", command = nyomtat).pack()
f.mainloop()