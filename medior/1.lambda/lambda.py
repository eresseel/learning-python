# hagyomanyos fuggeny
def osszead1(a, b):
    return a+b

print(osszead1(10, 15))

# lambda
osszead2 = lambda a,b: a+b

print(osszead2(25,20))

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
paros = filter(lambda x: x % 2 == 0, lista)
# print (list(paros))

for p in paros:
    print (p)

muveletek = {
    "add": lambda a,b: a+b,
    "sub": lambda a,b: a-b,
    "mul": lambda a,b: a*b,
    "div": lambda a,b: a/b
}

print(muveletek["add"](500,7))
add = muveletek["add"](500,7)
print(add)
add = muveletek["sub"](500,7)
print(add)