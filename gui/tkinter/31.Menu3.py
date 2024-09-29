from tkinter import *

class MenuBar(Frame):
    """Legördül menük sora"""
    def __init__(self, boss =None):
        Frame.__init__(self, borderwidth =2)
        ##### <File> menu #####
        fileMenu = Menubutton(self, text ='File')
        fileMenu.pack(side =LEFT)
        # A "legördül " rész : ő
        me1 = Menu(fileMenu)
        me1.add_command(label ='Törlés', underline =0,
        command = boss.erase)
        me1.add_command(label ='Befejezés', underline =0,
        command = boss.quit)
        # A menü integrálása :
        fileMenu.configure(menu = me1)
        ##### Menu <Zeneszek> #####
        self.musi = Menubutton(self, text ='Zenészek')
        self.musi.pack(side =LEFT, padx ='3')
        # A <Zeneszek> menu legördül része : ő
        me1 = Menu(self.musi)
        me1.add_command(label ='17. század', underline =1,
        foreground ='red', background ='yellow',
        font =('Comic Sans MS', 11),
        command = boss.showMusi17)
        me1.add_command(label ='18. század', underline =1,
        foreground='royal blue', background ='white',
        font =('Comic Sans MS', 11, 'bold'),
        command = boss.showMusi18)
        # A menü integrálása :
        self.musi.configure(menu = me1)

        ##### <Fest k> menu ##### ő
        self.pain = Menubutton(self, text ='Festok')
        self.pain.pack(side =LEFT, padx='3')
        # A "legördül " rész : ő
        me1 = Menu(self.pain)
        me1.add_command(label ='klasszikusok', state=DISABLED)
        me1.add_command(label ='romantikusok', underline =0,
        command = boss.showRomanti)
        # Almenü az impresszionista fest knek : ő
        me2 = Menu(me1)
        me2.add_command(label ='Claude Monet', underline =7,
        command = boss.tabMonet)
        me2.add_command(label ='Auguste Renoir', underline =8,
        command = boss.tabRenoir)
        me2.add_command(label ='Edgar Degas', underline =6,
        command = boss.tabDegas)
        # Az almenü integrálása :
        me1.add_cascade(label ='impresszionisták', underline=0, menu =me2)
        # A menü integrálása :
        self.pain.configure(menu =me1)

class Application(Frame):
    """F alkalmazás""" 
    def __init__(self, boss =None):
        Frame.__init__(self)
        self.master.title('Ablak menükkel')
        mBar = MenuBar(self)
        mBar.pack()
        self.can = Canvas(self, bg='light grey', height=190,
        width=250, borderwidth =2)
        self.can.pack()
        self.pack()
    def erase(self):
        self.can.delete(ALL)
    def showMusi17(self):
        self.can.create_text(10, 10, anchor =NW, text ='H. Purcell',
        font=('Times', 20, 'bold'), fill ='yellow')
    def showMusi18(self):
        self.can.create_text(245, 40, anchor =NE, text ="W. A. Mozart",
        font =('Times', 20, 'italic'), fill ='dark green')
    def showRomanti(self):
        self.can.create_text(245, 70, anchor =NE, text = "E. Delacroix",
    font =('Times', 20, 'bold italic'), fill ='blue')
    def tabMonet(self):
        self.can.create_text(10, 100, anchor =NW, text = 'Nymphéas à Giverny',
        font =('Technical', 20), fill ='red')
    def tabRenoir(self):
        self.can.create_text(10, 130, anchor =NW,
        text = 'Le moulin de la galette',
        font =('Dom Casual BT', 20), fill ='maroon')
    def tabDegas(self):
        self.can.create_text(10, 160, anchor =NW, text = 'Danseuses au repos',
        font =('President', 20), fill ='purple')

if __name__ == '__main__':
    app = Application()
    app.mainloop()