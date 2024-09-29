from tkinter import *
import Pmw
from random import randrange

# az ikonokat tartalmazó file-ok nevei (GIF formátumú ):
images =('Martin_p.gif','Martin_p.gif','Martin_p.gif','Martin_p.gif','Martin_p.gif')
textes =('mentés','pillangó','játékos 1','játékos 2','Help')

class Application(Frame):
    def __init__(self):
        Frame.__init__(self)
        # Egy <buborék help> objektum létrehozása (egy elegend ) : ő
        tip = Pmw.Balloon(self)
        # Eszköztár létrehozása (ez egy egyszer keret) : ű
        toolbar = Frame(self, bd =1)
        toolbar.pack(expand =YES, fill =X)
        # A létrehozandó gombok száma : 
        nBut = len(images)
        # A gombok ikonjainak persistens változókban kell lenni.
        # Egy lista megteszi :
        self.photoI =[None]*nBut

        for b in range(nBut):
            # Ikon létrehozása (PhotoImage Tkinter objektum) :
            self.photoI[b] =PhotoImage(file = images[b])

            # Gomb létrehozása.:
            # Egy "lambda" kifejezést használunk arra hogy a hívott
            # metódusnak parancsként adjunk át egy argumentumot :
            but = Button(toolbar, image =self.photoI[b], relief =GROOVE,
            command = lambda arg =b: self.action(arg))
            but.pack(side =LEFT)

            # egy gomb összekapcsolása egy helpszöveggel :
            tip.bind(but, textes[b])

        self.ca = Canvas(self, width =400, height =200, bg ='orange')
        self.ca.pack()
        self.pack()

    def action(self, b):
        "a gomb ikonja a vászonra van másolva"
        x, y = randrange(25,375), randrange(25,175)
        self.ca.create_image(x, y, image =self.photoI[b])

Application().mainloop()