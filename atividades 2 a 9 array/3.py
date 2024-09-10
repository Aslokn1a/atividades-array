import numpy as np

num = np.array([])
pot = np.array([])
for i in range(10):
    numero = float(input("informe 10 números reais: "))
    #append server para incluir elementos no array
    num = np.append(num,numero)
    #** serve para realizar potência 
    
pot = num**2
print(num)
print(pot)
print(num**2)

