import numpy as np

# atividade 10 
v = np.array([])
for i in range(15):
    num = int(input("informe as notas dos alunos: "))
    v = np.append(v,num)

media = sum(v)/np.size(v)
print("a média geral é de: ",media)
#-------------------------------------------------------------------------------------
#atividade 11
#v = np.array([])
#c = 0
#soma = 0
#for i in range(10):
#    num = float(input("informe 10 números reais: "))
#    v = np.append(v,num)
#for i in range(10):
#    if v[i]>=0:
#        soma = soma+v[i]
#    else: 
#        c=c+1
#print("a soma dos positivos é de: ",soma,"e a quantidade de números negativos é:", c)

#-------------------------------------------------------------------------------------

#atividade 12
#c1=0
#c2=19
#v = np.array([])
#for i in range(20):
#    num = int(input("informe 20 números inteiros: "))
#    v = np.append(v,num)
#print(v)
#for i in range(10):
#    f = v[c1]
#    v[c1] = v[c2]
#    v[c2] = f
#    c1=c1+1
#    c2=c2-1    
#print(v)

#-------------------------------------------------------------------------------------

#atividade 13
#v = np.array([])
#can = int(input("informe a quantidade de candidatos: "))
#vot = int(input("informe a quantidade de votantes: "))
#for i in range(can): #gerar o vetor com todos os candidatos tendo votos zerados
#    v = np.append(v,0)
#for i in range(vot):
#    num = int(input("informe em qual candidato irás votar: (0 para voto nulo)"))
#    v[num-1]=v[num-1]+1    
#for i in range(can):
#    print("o candidato",i+1, "recebeu", v[i], "votos")

#-------------------------------------------------------------------------------------

#atividade 14
#v = np.array([])
#c=0
#while c<100:
#    num = int(input("informe o número de mátricula dos 100 alunos: "))
#    if num in v:
#        print("essa matricula já foi cadastrada")
#        #print(v) foi usado para testar o código
#    else:
#        v = np.append(v,num)
#        c=c+1
#print("todas as matriculas são: ")

#-------------------------------------------------------------------------------------

#15
#c=0
#v = np.array([])
#par = np.array([])
#imp = np.array([])
#n = int(input("informe a quantidade de itens desejado para o vetor: "))
#for i in range(n):
#    num = int(input("informe um valor inteiro: "))
#    v = np.append(v,num)
#for i in range(n):
#    v[i]
#    if v[i]%2!=0:
#        imp=np.append(imp,v[i])
#    else: 
#        par = np.append(par,v[i])
#print("números impares do vetor: ",imp,"e ","números pares: ", par)

#-------------------------------------------------------------------------------------

#atividade 16
#a = np.array([])
#b = np.array([])
#c = np.array([])
#con = 0
#n1 = int(input("informe a quantidade de itens desejado para o vetor: "))
#n2 = int(input("informe a quantidade de itens desejado para o vetor: "))
#for i in range(n1):
#    num = int(input("informe valores ordenados para o vetor a: "))
#    a = np.append(a,num)
#for i in range(n2):
#    num = int(input("informe valores ordenados para o vetor b: "))
#    b = np.append(b,num)
#if n1>n2:
#    while con<n2:
#        c = np.append(c,a[con])
#        c = np.append(c,b[con])
#        con = con+1
#    while con<n1:
#        c = np.append(c,a[con])
#        con = con+1
#elif n2>n1:
#    while con<n1:
#        c = np.append(c,a[con])
#        c = np.append(c,b[con])
#        con = con+1
#    while con<n2:
#        c = np.append(c,b[con])
#        con = con+1
#else:
#    while con<n1:
#        c = np.append(c,a[con])
#        c = np.append(c,b[con])
#        con = con+1         
#print(c)

#-------------------------------------------------------------------------------------

#atividade 17
#notas = np.array([9.9, 9.7, 9.8, 10, 10])
#soma = 0
#c = 0
#mini =np.where(notas == min(notas))
#maxi = np.where(notas ==max(notas))
#notas = np.delete(notas,maxi)
#notas = np.delete(notas,mini)
#print(notas)

#for i in range(len(notas)):
#    c=c+1
#    soma=notas[i]+soma
    
#med= soma/c
#print(med)