# szam = 10
import math

class Szemely:
    "alma"
    def __init__(self, nev):
        self.nev = nev

sz1 = Szemely("Andi") 
def func1(sz):
    print(sz.nev)

func1(sz1)
print(sz1.__doc__)

def negyzet(x):
    return x*x

def gyok(x):
    return x**0.5

def muvelet(func, szam):
    return func(szam)

print (muvelet(negyzet, 10))
print (muvelet(gyok, 100))
print (muvelet(math.sin, 5))
print (muvelet(lambda x: x*x*x, 10))