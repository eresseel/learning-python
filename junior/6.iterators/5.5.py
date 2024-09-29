"""
Egy régi indiai legenda szerint a sakkjátékot egy öreg bölcs találta ki. A király meg akarta
azt neki köszönni és azt mondta, hogy jutalmul bármilyen ajándékot megad érte. Az öreg
azt kérte, hogy adjon neki egy kevés rizset öreg napjaira, pontosan annyi szem rizset, hogy
az általa feltalált játék első kockájára 1 szemet, 2 második kockára kettőt, a harmadikra
négyet, és így tovább egészen a 64­ik kockáig.
Írjon   egy   Python   programot,   ami   kiíratja   a   sakktábla   64   kockájának   mindegyikére
elhelyezett rizsszemek számát. Számolja ki ezt a számot kétféleképpen
­ a rizsszemek pontos száma (egész szám) 
­ a rizsszemek száma tudományos jelölésmódban (valós szám)
"""
n = 1
for i in range (1,65):
    print (f"{i}. kockan levo rizsszem: {n}")
    n*= 2