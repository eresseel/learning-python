# Írjon egy programot, ami kiszámolja 13­as szorzótábla első 50 tagját, de csak azokat írja ki,
# melyek 7­nek többszörösei.

i = 0
j = 1
while j != 50:
    if (i*13 % 7) == 0:
        print (f"{i*13}")
        j +=1
    i += 1