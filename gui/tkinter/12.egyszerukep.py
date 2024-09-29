from tkinter import *
abl1 = Tk()
# Label(), Entry(), és Checkbutton() widget-ek létrehozása :
Label(abl1, text = 'Elso mez :').grid(sticky =E)
Label(abl1, text = 'Masodik :').grid(sticky =E)
Label(abl1, text = 'Harmadik :').grid(sticky =E)
mezo1 = Entry(abl1)
mezo2 = Entry(abl1) # ezekre a widget-ekre kés bb ő
mezo3 = Entry(abl1) # hivatkozni fogunk :
mezo1.grid(row =0, column =1) # ezért mindegyiket külön
mezo2.grid(row =1, column =1) # változóhoz rendeljük
mezo3.grid(row =2, column =1)
chek1 = Checkbutton(abl1, text ='Checkbox a megjelenítéshez')
chek1.grid(columnspan =2)
# egy bitmap képet tartalmazó 'Canvas' (vászon) widget létrehozása:
can1 = Canvas(abl1, width =160, height =160, bg ='white')
photo = PhotoImage(file ='Martin_p.gif')
can1.create_image(80,80, image =photo)
can1.grid(row =0, column =2, rowspan =4, padx =10, pady =5)
# indítás :
abl1.mainloop()