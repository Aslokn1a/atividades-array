import numpy as np
v = np.array([])
c=0
while c<100:
    num = int(input("informe o número de mátricula dos 100 alunos: "))
    if num in v:
        print("essa matricula já foi cadastrada")
        #print(v) foi usado para testar o código
    else:
        v = np.append(v,num)
        c=c+1
print("todas as matriculas são: ")
    
        