a = 10
b = 20

def osszeadas1():
    print(a+b)

def osszeadas2(a, b, c=4):
    return a+b+c

def osszeadas3(*args): #barmennyi parametert fogad, nem kotelezo args-nak nevezni, csak konvencio
    return sum(args)

def udvozlesek(*args):
    koszones = "Ennyi fele koszones letezik: "
    for i in args:
        koszones += i
        koszones += ", "
    print (koszones[0:len(koszones)-2])

osszeadas1()
print(osszeadas2(2,2))
osszeadas3(1,2,3,4,5)
udvozlesek("Szia", "Hello", "Csa")