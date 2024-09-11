import numpy as np

v = np.array([])

for i in range(20):
    num = int(input("informe 20 números inteiros: "))
    v = np.append(v,num)
    
print(v)
v2 = v
print(v2)