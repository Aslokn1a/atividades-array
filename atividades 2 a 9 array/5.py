import numpy as np

num = np.array([])
pares = np.array([])

for i in range(10):
    numero = int(input("informe dez valores: "))
    num = np.append(num, numero)
#np.where é util par procurar coisas no verto tipo var = np.where(condição)
for i in range(10):
    if num[i]%2==0:
        pares = np.append(pares,num[i])

print(num, pares)

