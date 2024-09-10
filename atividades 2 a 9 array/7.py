import numpy as np

s = np.array([])
for i in range(10):
    num = int(input("informe 10 valores inteiros: "))
    s = np.append(s,num)
max = max(s)
pos = np.where(s==max)
print("o maior valor é de: ",max,"e se encontra na posição: ", pos)

