#osregi mod
szoveg1 = "A te neved %s, es %d eves vagy" % ("Laci", 30)
print(szoveg1)

#nem olyan regi
szoveg2 = "A te neved {}, es {} eves vagy".format("Laci", 30)
print(szoveg2)

#uj mod (f string)
nev = "Laci"
kor = 30
szoveg3 = f"A te neved {nev}, es {kor} eves vagy"
print(szoveg3)

nevek_szotar = {"alma":28, "korte": 14, "szilva":10}

for nev, kor in nevek_szotar.items():
    print(f"A te neved {nev}, es {kor} eves vagy")
    print(f"A te neved {nev}, es {kor-4} eves vagy")