"""
Írjon egy programot, ami a következő jelsorozatot írja ki :
*
**
***
****
*****
******
*******
"""

for i in range(1,7):
    for j in range(i):
        print("*", end="")
    print()