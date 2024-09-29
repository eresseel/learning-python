a = 5
print("Fuggvenyen kivul az 'a' erteke: " + str(a))

def test():
    a = 10
    print("Fuggvenyen belul az 'a' erteke: " + str(a))

test()
print("Fuggvenyen kivul az 'a' erteke: " + str(a))

def test2():
    global a 
    a = 15
    print("Fuggvenyen belul az 'a' erteke: " + str(a))

test2()
print("Fuggvenyen kivul az 'a' erteke: " + str(a))