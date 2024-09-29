szoveg = "Az en csajom Rebeka es 28 eves "
szoveg2 = "          Ma este iszok egy korso sort               "
adatok1 = "0,1,2,3,4,5,6,7"
adatok2 = "Eni;Zsoka;Andi"
print(szoveg)

szoveg = szoveg.replace("Rebeka", "Zsebibaba").replace("28","29") + "es nagyon szeretem ot."
print(szoveg)

print(szoveg.index("Zsebibaba"))
print(len(szoveg))
print(szoveg.startswith("Az"))
print(szoveg.endswith("ot."))

print(szoveg[13:22])
print(szoveg[-3])
print(szoveg2.lstrip())
print(szoveg2.rstrip())
print(szoveg2.strip())
print(adatok1.split(","))
print(adatok2.split(";"))