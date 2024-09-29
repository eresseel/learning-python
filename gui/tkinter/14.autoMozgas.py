from tkinter import *
# eseménykezel kő
# definiálása
def move():
    "a labda elmozdulása"
    global x1, y1, dx, dy, flag
    x1, y1 = x1 +dx, y1 + dy
    if x1 >360:
        x1, dx, dy = 360, 0, 15
    if y1 >360:
        y1, dx, dy = 360, -15, 0
    if x1 <10:
        x1, dx, dy = 10, 0, -15
    if y1 <10:
        y1, dx, dy = 10, 15, 0
        can1.coords(oval1,x1,y1,x1+30,y1+30)
    if flag >0:
        abl1.after(50, move) # 50 millisec után ciklus
def stop_it():
    "az animáció leáll"
    global flag
    flag =0
def start_it():
    "az animáció elindítása"
    global flag
    if flag ==0: # azért, hogy csak egy ciklust indítsunk
        flag = 1
        move()
#========== F program ============= ő
# a következ változókat globális változókként fogjuk használni : ő
x1, y1 = 10, 10 # kezd koordináták ő
dx, dy = 15, 0 # nincs elmozdulás
flag =0 # kapcsoló
# A f -widget létrehozása ("master") : ő
abl1 = Tk()
abl1.title("Animációs gyakorlat Tkinter-rel")
# a "slave" widget-ek (canvas + oval, button) létrehozása:
can1 = Canvas(abl1,bg='dark grey',height=400,width=400)
can1.pack(side=LEFT)
oval1 = can1.create_oval(x1,y1,x1+30,y1+30,width=2,fill='red')
Button(abl1,text='Kilép',command=abl1.quit).pack(side=BOTTOM)
Button(abl1,text='Indít',command=start_it).pack()
Button(abl1,text='Leállít',command=stop_it).pack()
# az eseményfogadó indítása (f ciklus) : ő
abl1.mainloop()