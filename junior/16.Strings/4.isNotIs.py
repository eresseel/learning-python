szam1 = 4
szam2 = 4

print(szam1 == szam2)

# innentol is
szam = 8

if type(szam) is int:
    print("Int")
    
if type(szam) is not str:
    print("nem int tipus")

igaz = True

print(type(igaz) is not bool)

class Szemely:
    pass
sz1 = Szemely()
sz2 = Szemely()

if type(sz1) is Szemely:
    print("Class")
else:
    print(type(sz1))

print (sz1 is sz2)
sz2 = sz1
print (sz1 is sz2)

if isinstance(sz1, Szemely):
    print("Szemely tipus")