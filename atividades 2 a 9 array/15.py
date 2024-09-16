import numpy as np
c=0
v = np.array([])
par = np.array([])
imp = np.array([])
n = int(input("informe a quantidade de itens desejado para o vetor: "))
for i in range(n):
    num = int(input("informe um valor inteiro: "))
    v = np.append(v,num)
for i in range(n):
    v[i]
    if v[i]%2!=0:
        imp=np.append(imp,v[i])
    else: 
        par = np.append(par,v[i])
print("números impares do vetor: ",imp,"e ","números pares: ", par)