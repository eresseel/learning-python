while False:
    pass #ha nem tudom mi legyen a ciklusban akkor a pass szot kell beirni, nem csinal semmit

for i in range(10):
    if i == 5:
        break
    print (i)

szam = 0
while True:
    print(szam)
    szam += 1
    if szam == 5:
        break

for i in range(10):
    if i == 5:
        continue
    print(i)

szamlalo = 0
while True:
    szamlalo += 1
    if szamlalo % 2 == 0:
        continue
    print(szamlalo)
    if szamlalo > 20:
        break