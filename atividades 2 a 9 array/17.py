import numpy as np
notas = np.array([9.9, 9.7, 9.8, 10, 10])
soma = 0
c = 0
mini =np.where(notas == min(notas))
maxi = np.where(notas ==max(notas))
notas = np.delete(notas,maxi)
notas = np.delete(notas,mini)
print(notas)

for i in range(len(notas)):
    c=c+1
    soma=notas[i]+soma
    
med= soma/c
print(med)
