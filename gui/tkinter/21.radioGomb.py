from tkinter import *

class RadioDemo(Frame):
    """Demó : a rádiógomb widgetek használata'"""
    def __init__(self, boss =None):
        """Egy adatbeviteli mez és 4 rádiógomb létrehozása"""
        Frame.__init__(self)
        self.pack()
        # Szöveget tartalmazó adatbeviteli mez : ő
        self.texte = Entry(self, width =30, font ="Arial 14")
        self.texte.insert(END, "A programozás nagyszerű")
        self.texte.pack(padx =8, pady =8)
        # A 4 bet stílus magyar és technikai neve : ű
        styleFontHu =["Normál", "Kövér", "Dőlt", "Kövér/Dőlt"]
        styleFontTk =["normal", "bold", "italic" , "bold italic"]
        # Az aktuális stílust egy Tkinter 'változó-objektumba mentjük' ;
        self.choiceFont = StringVar()
        self.choiceFont.set(styleFontTk[0])
        # A 4 rádiógomb létrehozása' :
        for n in range(4):
            bout = Radiobutton(self,
            text = styleFontHu[n],
            variable = self.choiceFont,
            value = styleFontTk[n],
            command = self.changeFont)
            bout.pack(side =LEFT, padx =5)

    def changeFont(self):
        """Az aktuális bet stílus helyettesítése"""
        font_ = "Arial 15 " + self.choiceFont.get()
        self.texte.configure(font =font_)

if __name__ == '__main__':
    RadioDemo().mainloop()