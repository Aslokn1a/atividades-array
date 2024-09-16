import numpy as np
v = np.array([])
can = int(input("informe a quantidade de candidatos: "))
vot = int(input("informe a quantidade de votantes: "))

for i in range(can): #gerar o vetor com todos os candidatos tendo votos zerados
    v = np.append(v,0)


for i in range(vot):
    num = int(input("informe em qual candidato irás votar: (0 para voto nulo)"))
    v[num-1]=v[num-1]+1
    
for i in range(can):
    print("o candidato",i+1, "recebeu", v[i], "votos")