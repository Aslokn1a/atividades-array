#exercicio 10
import numpy as np
v = np.array([])
for i in range(15):
    num = int(input("informe as notas dos alunos: "))
    v = np.append(v,num)

media = sum(v)/np.size(v)
print("a média geral é de: ",media)


