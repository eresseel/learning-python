# Írjon egy programot = ami átszámolja a kiindulásként megadott egészszámú másodpercet
# évekké = hónapokká = napokká = percekké és másodpercekké.
# (Használja a modulo operátort : % ).

ev = honap = nap = ora = perc = masodperc = 0
sec = 64248442392 #int(input("Add meg a masodpercet: "))

masodperc = sec % 60
perc = int((sec / 60) % 60)
ora = int((sec / (60*60))) % 24
nap = int((sec / (60*60*24))) % 31
honap = int((sec / (60*60*24*31))) % 12
ev = int(sec / (60*60*24*31*12))

print (f"{ev}-{honap}-{nap} {ora}:{perc}:{masodperc}")