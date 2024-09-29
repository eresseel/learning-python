mondas = "Bagoly mondja verebnek, hogy nagy feju"
nevek = ["alma", "korte", "szilva"]
szotar = {"alma":2, "korte":3, "szilva":1}

if ("Golya" in mondas):
    print("Talalat")
else:
    print("Nem nyert")

if ("alma" in nevek):
    print("Talalat")
else:
    print("Nem nyert")

if ("alma" not in nevek):
    print("Talalat")
else:
    print("Nem nyert")

if ("alma" in szotar): # csak a kulcs alapjan keres
    print("Talalat")
else:
    print("Nem nyert")