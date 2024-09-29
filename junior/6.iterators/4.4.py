# Írjon egy programot, ami kiír egy 12 számból álló sorozatot, aminek minden tagja vagy
# egyenlő az előző taggal, vagy annak háromszorosa.

a = 1
c = 1
for i in range(13):
    print (a)
    a , c = a*3 , c+1