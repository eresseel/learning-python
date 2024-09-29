"""
. Írjon egy programot, ami egy szavakból álló lista elemeit egyenként megvizsgálja azért,
hogy két új listát hozzon létre. (például: ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean­Pierre',
'Sandra'] Az egyikben 6 karakternél rövidebb szavakat legyenek, a másikban 6, vagy annál
több karaktert tartalmazzonó szavak legyenek.
"""

string1 = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
rovid = []
hosszu = []

for i in range(len(string1)):
    if len(string1[i]) <= 5:
        rovid.append(string1[i])
    else:
        hosszu.append(string1[i])

print(rovid)
print(hosszu)