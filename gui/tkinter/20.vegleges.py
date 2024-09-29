from oscillo import *
from curseurs import *

class ShowVibra(Frame):
    """Harmónikus rezg mozgások bemutatása"""
    def __init__(self, boss =None):
        Frame.__init__(self) # a szül osztály constructora ő
        self.colour = ['dark green', 'red', 'purple']
        self.trace = [0]*3 # kirajzolandó görbék listája
        self.control = [0]*3 # kontrolpanelek listája

        # vászonpéldány létrehozása az x és y koordináta-tengelyekkel :
        self.gra = OscilloGraphe(self, width_ =400, height_=200)
        self.gra.configure(bg ='white', bd=2, relief=SOLID)
        self.gra.pack(side =TOP, pady=5)

        # 3 vezérl panel (cursorok) létrehozása : ő
        for i in range(3):
            self.control[i] = ChoiceVibra(self, self.colour[i])
            self.control[i].pack()

        # Az ábrák kirajzolását indító események definiálása :
        self.master.bind('<Control-Z>', self.showCurves)
        self.master.title('Harmónikus rezg mozgások')
        self.pack()

    def showCurves(self, event):
        """A három kitérés-id grafikon (újra)kirajzolása """
        for i in range(3):
            # El ször töröljük az (esetleges) el z ábrát : ő ő ő
            self.gra.delete(self.trace[i])
            # Aztán kirajzoljuk az új ábrát :
            if self.control[i].chk.get():
                self.trace[i] = self.gra.drawCurve(
                colo = self.colour[i],
                freq = self.control[i].freq,
                phase = self.control[i].phase,
                ampl = self.control[i].ampl)

#### Kód az osztály teszteléséhez : ###
if __name__ == '__main__':
    ShowVibra().mainloop()