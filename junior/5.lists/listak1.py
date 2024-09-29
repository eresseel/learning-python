#mutable - modosithato objektumok

lista1 = [] #ures lista masneven tomb

print(lista1)
lista1.append(100) #elem hozzaadasa
lista1.append(300)
lista1.append(300)
lista1.append("alma")
lista1.append("korte")
lista1.append("korte")
print(lista1)
lista1.remove("korte")
print(lista1)
lista1.insert(2, "szilva")
print(lista1)
lista1.reverse()
print(lista1)
lista1.clear()
print(lista1)

lista2 = [15,2,355,64,1,6]
print(lista2)
lista2.sort()
print(lista2)

lista3 = ["korte", "szilva", "alma"]
print(lista3)
lista3.sort()
print(lista3)
print(len(lista3))