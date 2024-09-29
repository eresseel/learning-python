"""
Írjon egy programot, ami megvizsgálja egy számlista minden elemét (például az előző
példa listáját) azért, hogy két új listát hozzon létre. Az egyik csak az eredeti lista páros
számait tartalmazza, a másik a páratlanokat. Például, ha a kiindulási lista az előző gyakorlat
listája, akkor a programnak egy  páros listát  kell létrehoznia, ami a [32, 12, 8, 2]  ­t
tartalmazza és egy páratlan listát ami [5, 3, 75, 15] ­t tartalmazza. Trükk : Gondoljon
az előzőekben említett modulo (%) operátor használatára !
"""

number = [32, 5, 12, 8, 3, 75, 2, 15]
paros = []
paratlan = []

for i in range(len(number)):
    if number[i] % 2 == 0:
        paros.append(number[i])
    else:
        paratlan.append(number[i])

print(f"Paros: {paros}")
print(f"Paratla: {paratlan}")