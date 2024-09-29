file = open("20.fileOlvasas.txt", 'r', encoding="utf-8")

for i in file:
    print(i.strip())

sor = file.readline()
while sor:
    print(sor.strip())
    sor = file.readline()

file.close()

with open("./20.fileOlvasas.txt", 'r', encoding="utf-8") as file:
    for sor in file:
        print(sor.strip())

with open("./20.fileOlvasas.txt", 'r', encoding="utf-8") as file:
    sor = file.readline()
    print (sor)
    sor = file.readlines()
    print (sor)
    print (sor[1])
    print (type(sor))

with open("./20.fileOlvasas.txt", 'r', encoding="utf-8") as file:
    sor = file.read()
    print (sor)
