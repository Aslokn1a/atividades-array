import numpy as np

num = np.array([])

for i in range(6):
    numero = int(input("informe 6 números inteiros: "))
    #append server para incluir elementos no array
    num = np.append(num,numero)

print(num)
