from tkinter import *
from math import sin, pi

class OscilloGraphe(Canvas):
    "kitérés/id görbe rajzolására szolgáló specializált vászon"
    def __init__(self, boss =None, width_=200, height_=150):
        "A grafika constructora : tengelyek és vízszintes skála."
        # a szül widget elkészítése : ő
        Canvas.__init__(self) # a szül osztály ő
        self.configure(width=width_, height=height_) # constructorának hívása
        self.width_, self.height_ = width_, height_ # tárolás
        # tengelyek megrajzolása :
        self.create_line(10, height_/2, width_, height_/2, arrow=LAST) # X tengely
        self.create_line(10, height_-5, 10, 5, arrow=LAST) # Y tengely
        # 8 osztású skála rajzolása :
        step = (width_-25)/8. # vízszintes skála intervallumai
        for t in range(1, 9):
            stx = 10 + t*step # +10, hogy az origótól eljöjjünk
            self.create_line(stx, height_/2-4, stx, height_/2+4)

    def drawCurve(self, freq=1, phase=0, ampl=10, colo='red'):
        "1 sec id tartamra es kitérés/id görbe rajzolása"
        curve =[] # koordináták listája
        step = (self.width_-25)/1000. # az X-skála 1 sec-nak felel meg
        for t in range(0,1001,5): # amit 1000 ms-ra osztunk fel
            e = ampl*sin(2*pi*freq*t/1000 - phase)
            x = 10 + t*step
            y = self.height_/2 - e*self.height_/25
            curve.append((x,y))
        n = self.create_line(curve, fill=colo, smooth=1)
        return n # n = a rajz sorszáma

#### Kód az osztály tesztelésére : ####

if __name__ == '__main__':
    root = Tk()
    gra = OscilloGraphe(root, 250, 180)
    gra.pack()
    gra.configure(bg ='ivory', bd =2, relief=SUNKEN)
    gra.drawCurve(2, 1.2, 10, 'purple')
    root.mainloop()