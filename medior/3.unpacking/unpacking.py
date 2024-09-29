# iteralhato objectumok kicsomagolasa
lista1 = range(10)

print(list(lista1))
print(*lista1)

lista2 = [0]*9
print(lista2)

lista3 = lista2 # ez referencia vagy alias
lista2[0] = 87
print(lista2)
print(lista3)

lista4 = [0]*9
lista5 = [*lista4] # ez mar nem alias
lista4[0] = 87
print(lista4)
print(lista5)

def func(*args, **kwargs): #valtozo szamu argumentum megadasa
    print(args)
    print(kwargs)

func()
func(10,20,30,40, **{"nev1":"Andi", "nev2":"Aniko"})

nevek = ["alma", "korte", "szilva"]
korok = [1,2,3]

nevKor = [*nevek], [*korok]
print(nevKor)

szoveg = "Hello! Hogy vagy?"
szovegLista = [*szoveg]
print(szovegLista)
udv = "".join(szovegLista)
print(szovegLista)
print(udv)