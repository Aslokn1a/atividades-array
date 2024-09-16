import numpy as np
c1=0
c2=19
v = np.array([])
for i in range(20):
    num = int(input("informe 20 números inteiros: "))
    v = np.append(v,num)
print(v)
for i in range(10):
    f = v[c1]
    v[c1] = v[c2]
    v[c2] = f
    c1=c1+1
    c2=c2-1
    
print(v)