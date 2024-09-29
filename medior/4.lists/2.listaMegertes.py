matrixZeros1 = [[0 for x in range(4)] for y in range(4)]
print(matrixZeros1)
matrixZeros2 = [[0]*4]*4
print(matrixZeros2)

matrixPrint = lambda mat: ([print(row) for row in mat], print())

matrixPrint(matrixZeros1)
matrixIdentity = [[1 if x==y else 0 for x in range(4)] for y in range(4)]
matrixPrint(matrixIdentity)