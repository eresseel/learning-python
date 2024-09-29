with open("./34.stringManipulalas2.txt", "r", encoding="UTF-8") as inFile:
    szoveg = ""
    sor = inFile.readline()

    while sor:
        szoveg += sor.lstrip().replace("Matild", "Rebeka")
        sor = inFile.readline()

    print(szoveg)

    with open("./34.Rebeka.txt", "w", encoding="UTF-8") as outFile:
        outFile.write(szoveg)