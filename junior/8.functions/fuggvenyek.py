nevek1 = ["Xena", "Bozsi", "Vica", "Eni", "Ildi", "Zsuszi", "Evi", 10]
nevek2 = ["Pityu", "Ati", "Peti", "Bence", "Feri"]

def nevPrinter(nevLista):
    for nev in nevLista:
        if isinstance(nev, str):
            print(nev.upper())
        else:
            print("Nem string tipusu: " + str(type(nev)))

nevPrinter(nevek1)