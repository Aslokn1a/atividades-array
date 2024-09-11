import numpy as np

v = np.array([])
c = 0
soma = 0
for i in range(10):
    num = float(input("informe 10 números reais: "))
    v = np.append(v,num)

for i in range(10):
    if v[i]>=0:
        soma = soma+v[i]
    else: 
        c=c+1
        
print("a soma dos positivos é de: ",soma,"e a quantidade de números negativos é:", c)