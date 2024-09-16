import numpy as np
a = np.array([])
b = np.array([])
c = np.array([])
con = 0
n1 = int(input("informe a quantidade de itens desejado para o vetor: "))
n2 = int(input("informe a quantidade de itens desejado para o vetor: "))
for i in range(n1):
    num = int(input("informe valores ordenados para o vetor a: "))
    a = np.append(a,num)
for i in range(n2):
    num = int(input("informe valores ordenados para o vetor b: "))
    b = np.append(b,num)
if n1>n2:
    while con<n2:
        c = np.append(c,a[con])
        c = np.append(c,b[con])
        con = con+1
    while con<n1:
        c = np.append(c,a[con])
        con = con+1
elif n2>n1:
    while con<n1:
        c = np.append(c,a[con])
        c = np.append(c,b[con])
        con = con+1
    while con<n2:
        c = np.append(c,b[con])
        con = con+1
else:
    while con<n1:
        c = np.append(c,a[con])
        c = np.append(c,b[con])
        con = con+1         
print(c)