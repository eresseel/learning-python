"""
Írjon egy programot, ami kiíratja egy lista összes elemét. Ha például a fenti gyakorlat t2
listájára alkalmaznánk, akkor a következőt kellene kapnunk : 
Január Február Március Április Május Június Július Augusztus Szeptember 
Október November December
"""
t2 = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június',
 'Július', 'Augusztus', 'Szeptember', 'Október', 'November', 'December']

t3 = ""

for i in range(len(t2)):
    t3 += t2[i]+ " "

print (t3)