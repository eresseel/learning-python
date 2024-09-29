# Írjon egy programot, ami kiíratja a 7­es szorzótábla első 20 tagját, csillaggal jelölve azokat,
# amelyek 3­nak többszörösei.
# Példa :   7   14   21 * 28   35   42 * 49

for i in range(1, 21):
    if (i*7) % 3 == 0:
        print(f"{i*7}*")
    print(i*7)