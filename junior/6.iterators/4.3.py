"""
Írjon egy programot, ami euróban kifejezett pézösszegeket kanadai dollárba vált át és az
eredményt egy táblázatba írja ki. A táblázatban a pézösszegek « geometriai haladvány »
szerint növekedjenek úgy, mint az alábbi példában : 
1 euro = 1.65 dollar 
2 euro = 3.30 dollar 
4 euro = 6.60 dollar 
8 euro = 13.20 dollar 
stb. ( 16384 euronál kell megállni)
"""
szam = 1
print (f"{szam} euro = {szam*1.65} dollar")
for i in range(1,16384):
    szam *= 2
    print (f"{szam} euro = {szam*1.65} dollar")