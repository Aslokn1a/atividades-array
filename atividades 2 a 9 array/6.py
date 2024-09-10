import numpy as np

s = np.array([])
for i in range(10):
    num = int(input("informe 10 valores inteiros: "))
    s = np.append(s,num)
max = max(s)
mim = min(s)
print("o maior valor é de: ",max,"e o menor valor é de:",mim)
