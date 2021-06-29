'''Elabore um programa Python que grave em um arquivo um número indeterminado de nomes e
idades. Depois leia estes dados e classifique por idade. Exibir os valores na ordem em que
foram lidos e depois ordenados..'''

def Grava():
    with open('ex05p5.txt','w+') as file:
        while True:
            nome = input('Nome: ').strip().lower()
            temp.append(nome)
            if nome == '': break
            
            while True:
                try:
                    idade = int(input('Idade: '))
                    temp.append(idade)
                    break
                except ValueError:
                    print('Idade nao correspondida')
            file.write(nome+' '+idade+'\n')
    return

def Ler():
    temp = []
    princ = []
    with open('ex05p5.txt','r') as file:
        for i in file:
            v = i.split()
            temp.append(v[0])
            temp.append(v[1])
            princ.append(temp[:])
        print(princ)
        temp.clear() 
    return princ

def Ordena(a):
    print('Lista na ordem lida: ')
    print('{}{}'.format(nome, idade))
    for i in range(len(a)):
        print('{}{}'.format(a[i][0], a[i][1]), end='') 
 
    s = sorted(a, key=lambda lista:lista[1])
    print('Lista ordenada por idade: ')
    for i in range(len(s)):
        print('{}{}'.format(s[i][0], s[i][1]), end='')
    return


#PROGRAMA PRINCIPAL
Grava()
princ = Ler()
Ordena(princ)