lista1 = ["Xena", "Bocsi", "Vica", "Eni", "Ildi"]

print(lista1)
print(lista1[0]) #indexeles
print(lista1[-1]) #szeleteles utolso elem

print(lista1[0:2]) #szeleteles
print(lista1[2:4]) #szeleteles
print(lista1[2:]) #szeleteles
print(lista1[:3]) #szeleteles

lista2 = [[1,2,3,4], [4,5,6], [7,8,9]]
print(lista2[2])
print(lista2[2][1])

tartomany = range(100)
print(list(tartomany))