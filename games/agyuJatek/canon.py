from tkinter import *
from math import sin, cos, pi
from random import randrange
import canon03

class Canon(canon03.Canon):
    """Tökéletesített ágyú"""
    def __init__(self, boss, id, x, y, irany, szin):
        canon03.Canon.__init__(self, boss, id, x, y, irany, szin)

    def elmozdit(self, x, y, rel =False):
        "relatív elmozdulás, ha <rel> igaz; abszolút ha <rel> hamis"
        if rel:
            dx, dy = x, y
        else:
            dx, dy = x -self.x1, y -self.y1
        # vízszintes határok :
        if self.irany ==1:
            xa, xb = 20, int(self.xMax *.33)
        else:
            xa, xb = int(self.xMax *.66), self.xMax -20
        # csak ezek között a határok között mozdul el :
        if self.x1 +dx < xa:
            dx = xa -self.x1
        elif self.x1 +dx > xb:
            dx = xb -self.x1
        # függ leges határok : ő
        ya, yb = int(self.yMax *.4), self.yMax -20
        # csak ezek között a határok között mozdul el :
        if self.y1 +dy < ya:
            dy = ya -self.y1
        elif self.y1 +dy > yb:
            dy = yb -self.y1
        # az ágyúcs és a test elmozdulása : ő
        self.boss.move(self.cso, dx, dy)
        self.boss.move(self.test, dx, dy)
        # az új koordináták visszaadása a hívó programnak :
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy
        return self.x1, self.y1

    def animacio_vege(self):
        "végrehajtandó akciók, amikor a lövedék elérte a röppályája végét"
        # annak az ágyúnak az elmozdítása, amelyik tüzelt :
        self.appli.agyu_veletlen_mozditasa(self.id)
        # lövedék elrejtése (a vásznon kívülre küldjük) :
        self.boss.coords(self.lovedek, -10, -10, -10, -10)

    def torol(self):
        "az ágyú eltüntetése a vászonról"
        self.boss.delete(self.cso)
        self.boss.delete(self.test)
        self.boss.delete(self.lovedek)
    
class AppAgyuParbaj(Frame):
    '''Az alkalmazás f ablaka '''
    def __init__(self, larg_c, haut_c):
        Frame.__init__(self)
        self.pack()
        self.xm, self.ym = larg_c, haut_c
        self.jatek = Canvas(self, width =self.xm, height =self.ym,
        bg ='ivory', bd =3, relief =SUNKEN)
        self.jatek.pack(padx =4, pady =4, side =TOP)
        
        self.guns ={} # a jelen levõ ágyúk szótára
        self.pult ={} # a jelen levõ vezérlõpultok szótára
        self.specificites() # különb. objektumok a leszárm. oszt.okban

    def specificites(self):
        "ágyúk és vezérl panelek létrehozása"
        self.master.title('<<< Ágyúpárbaj >>>')
        id_list =[("Paul","red"),("Roméo","cyan"),
        ("Virginie","orange"),("Juliette","blue")]
        s = False
        for id, szin in id_list:
            if s:
                irany =1
            else:
                irany =-1
            x, y = self.veletlen_koord(irany)
            self.guns[id] = Canon(self.jatek, id, x, y, irany, szin)
            self.pult[id] = canon03.VezerloPult(self, self.guns[id])
            s = not s # az oldal megváltozt. minden iterrációban

    def agyu_veletlen_mozditasa(self, id):
        "véletlenszer en elmozdítja az <id> ágyút "
        gun =self.guns[id]
        dx, dy = randrange(-60, 61), randrange(-60, 61)
        # elmozdítás (az új koordináták meghatározásával) :
        x, y = gun.elmozdit(dx, dy, True)
        return x, y

    def veletlen_koord(self, s):
        "véletlen koordináták, bal (s =1) vagy jobb (s =-1)"
        y =randrange(int(self.ym /2), self.ym -20)
        if s == -1:
            x =randrange(int(self.xm *.7), self.xm -20)
        else:
            x =randrange(20, int(self.xm *.3))
        return x, y

    def goal(self, i, j):
        "la n°i ágyú jelzi, hogy eltalálta a n°j ellenfelet"
        # melyik táborhoz tartoznak ?
        ti, tj = self.guns[i].irany, self.guns[j].irany
        if ti != tj : # ellenkezõ irányúak :
            p = 1 # 1-pontot kapunk
        else: # azonos irányban vannak :
            p = -2 # szövetségest találtunk el !!
        self.pult[i].pontHozzaadasa(p)
        # akit eltaláltak veszít egy pontot :
        self.pult[j].pontHozzaadasa(-1)

    def dictionnaireCanons(self):
        "vissza adja a jelenlév ágyúkat leíró szótárat"
        return self.guns

if __name__ =='__main__':
    AppAgyuParbaj(650,300).mainloop()