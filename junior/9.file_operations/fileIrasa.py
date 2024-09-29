with open("./21.fileIrasa.txt", 'w', encoding="utf-8") as file:
    szoveg = "almÁK\nalma\nkorte\n"
    file.write(szoveg)

with open("./21.fileIrasa.txt", 'r', encoding="utf-8") as inFile:
    print(inFile.readlines())

with open("./21.fileIrasa.txt", 'a', encoding="utf-8") as appendFile:
    ujsor = "nem akarasnak nyoges a vege"
    appendFile.write(ujsor)

with open("./21.fileIrasa.txt", 'r', encoding="utf-8") as inFile:
    print(inFile.readlines())