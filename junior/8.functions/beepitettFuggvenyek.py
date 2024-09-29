print(abs(-78))
nevek1 = ["Xena", "Bozsi", "Vica", "Eni", "Ildi", "Zsuszi", "Evi"]

for index, nev in enumerate(nevek1):
    print(index, nev)

print(hex(125))
print(int(87.23))
print(int("87")) #atkonvertalja int-re
print(len("alma"))
print(max(7,2,4))
print(min(7,2,4))
print(2**2)
print(pow(2,2))

print(range(100))
print(range(50, 100))
print(range(50, 100, 2))
print(list(reversed(nevek1)))
print(round(12.6))
print(round(12.514543554345, 2)) #mennyi szamjegyet mutat meg
print(sum([1,2,3,4,5])) #listaba vagy tuple ben kell megadni
print(sum((1,2,3,4,5))) #listaba vagy tuple ben kell megadni
print(type(3.2)==float)