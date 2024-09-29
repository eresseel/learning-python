lista = [1,2,'3', None, "alma", True, '5']

try:
    print(bla)
    print(lista[4])
except NameError as e:
    print(e, " - Nem letezo")
except IndexError as e:
    print(e)

print("A program vege")

for i in lista:
    try:
        print(int(i)*2)
    except:
        continue
    except:
        pass
    else:
        pass
    finally:
        pass