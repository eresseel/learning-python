#nem modosithato adathalmaz
lista = ["alma", "korte", "szilva"]
tuple1 = ("alma", "korte", "szilva","korte") #konstans

lista.append("szolo")
lista[-1] = "malna"

try:
    tuple1.append("szolo")
except:
    print("A tuple nem modosithato")

try:
    tuple1[-1] = "szolo"
except:
    print("A tuple nem modosithato")

print(tuple1[2])
tup2 = tuple(lista)
print(tup2)
tup2 = list(lista)
print(tup2)
print(tuple1.index("korte"))
print(tuple1.count("korte"))
