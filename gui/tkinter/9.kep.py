from tkinter import *
# from PIL import Image, ImageTk

abl1 = Tk()
# a "Label" és "Entry" widgetek létrehozása:
txt1 = Label(abl1, text ="Elso mezo: ")
txt2 = Label(abl1, text ="Masodik: ")
txt3 = Label(abl1, text ="Harmadik: ")
mezo1 = Entry(abl1)
mezo2 = Entry(abl1)
mezo3 = Entry(abl1)
# egy bitmap képet tartalmazó "Canvas" widget létrehozása :
can1 = Canvas(abl1, width =160, height =160, bg ="white")
# photo = PhotoImage(Image.open("Martin_p.png"))
# item = can1.create_image(80, 80, image =photo)
# laptördelés a"grid" metódus segítségével :
txt1.grid(row =1, sticky =E)
txt2.grid(row =2, sticky =E)
txt3.grid(row =3, sticky =E)
mezo1.grid(row =1, column =2)
mezo2.grid(row =2, column =2)
mezo3.grid(row =3, column =2)
can1.grid(row =1, column =3, rowspan =3, padx =10, pady =5)
# indítás :
abl1.mainloop()