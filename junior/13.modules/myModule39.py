def hello():
    print("Hello")

def helloMyModule():
    print(f"Hello {__name__} a myModule-bol")

def teszt():
    print("Hello teszt")

szam = 10

class Szemely:
    def __init__(self, nev, kor):
        self.nev = nev
        self.kor = kor
    def show_fields(self):
        print(self.nev, self.kor)

if __name__ == "__name__":
    hello()
    print(szam)
    Juli = Szemely("juliska", 45)
    Juli.show_fields()

teszt()