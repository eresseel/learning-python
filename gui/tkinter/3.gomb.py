from tkinter import *

abl1 = Tk()
text1 = Label(abl1, text="Hello world", fg="#f3ca2f")
text1.pack()
gomb1 = Button(abl1, text="Kilep", command= abl1.destroy)
gomb1.pack()
abl1.mainloop()