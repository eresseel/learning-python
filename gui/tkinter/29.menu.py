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

if __name__ == '__main__':
    app = Application()
    app.mainloop()