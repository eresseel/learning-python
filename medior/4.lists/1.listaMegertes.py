szamok = []
for i in range(20):
    szamok.append(i)

print(szamok)

# egyszerubb verzio

szamok = [x for x in range(20)]
print(szamok)

paros = [x for x in range(20) if x % 2 == 0]
print(paros)

paratlan = [x for x in range(1,20,2)]
print(paratlan)

nevek = ["alma", "korte", "szilva"]
print(nevek)
nevek = [nev.capitalize() for nev in nevek]
print(nevek)

nevekA = [nev for nev in nevek if nev.startswith("A")]
print(nevekA)