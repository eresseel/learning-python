jelszo = "kisuborka"

bemenet = input("Mi a jelszo? ")
proba = 0

while bemenet != jelszo:
    proba += 1
    if proba == 3:
        print ("Hozzaferes megtagadva")
        break
    print('Rossz jelszo, probald ujra! ')
    bemenet = input("Mi a jelszo? ")

if bemenet == jelszo:
    print("Hozzaferes engedelyezve")