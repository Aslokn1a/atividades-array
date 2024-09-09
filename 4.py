import numpy as np 

num = np.array([]) # x e y vão servir par escolher a posição no vetor
x = int(input("informe um valor entre 0 e 7: "))
y = int(input("informe um outro valor entre 0 e 7: "))
for i in range(8):
    numero = int(input("informe 8 valores: "))
    num = np.append(num,numero)
#soma recebe a soma dos números nas posições desejadas
soma = num[x]+num[y]
print(num, soma)