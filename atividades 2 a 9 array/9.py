import numpy as np

vet = np.array([])
cont = 0#variável utilizada como contador

while cont<6: #while para contar somente se o valor for par
    n = int(input("informe 6 valores: "))
    while n%2!=0:#verificando se o valor é par
        n = int(input("por favor informe um valor par: "))
    #essa parte do código só sera executada se o valor informado for par
    vet = np.append(vet,n)
    cont+=1#adiciona mais 1 ao contador somente se o valor for par por causa das condições acima    
print(np.flip(vet))#np.flip server para inverter um vetor