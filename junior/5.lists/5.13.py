# Írjon egy programot, ami megkeresi egy adott lista legnagyobb elemét. Például, ha a [32, 
# 5, 12, 8, 3, 75, 2, 15], listára alkalmaznánk, akkor a következőt kellene kiírnia :
# a lista legnagyobb elemének az értéke 75.

number = [32, 5, 12, 8, 3, 75, 2, 15]
number.sort()
print(number[-1])