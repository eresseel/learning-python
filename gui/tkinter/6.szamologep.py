from tkinter import *
from math import *

def kiertekeles(event):
    chain.configure(text = "Eredmeny = " + str(eval(mezo.get())))

ablak = Tk()
mezo = Entry(ablak)
mezo.bind("<Return>", kiertekeles)
mezo.pack()
chain = Label(ablak)
chain.pack()
ablak.mainloop()