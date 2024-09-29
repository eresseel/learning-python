from tkinter import *

abl1 = Tk()
txt1 = Label(abl1, text = 'Elso mezo :')
txt2 = Label(abl1, text = 'Második :')
mezo1 = Entry(abl1)
mezo2 = Entry(abl1)
txt1.pack(side =LEFT)
txt2.pack(side =LEFT)
mezo1.pack(side =RIGHT)
mezo2.pack(side =RIGHT)
abl1.mainloop()