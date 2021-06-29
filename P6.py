#Argos Antao Maia
'''Gerar(usando random) e gravar em um arquivo 40 números aleatórios e não repetidos compreendidos entre 1 e 99.
Obs: O nome do arquivo gravado deverá ter as iniciais de seu nome.

Por exemplo: jose Silva deverá ter o nome js.txt, e assim por diante.

Ler os valores gravados e com eles criar uma matriz quadrada de mxm elementos. 

O valor de m é lido e validados para numérico inteiro entre 2 e 6 inclusive.

Usando um algoritmo de ordenação a sua escolha (bubble sort, inserction sort ou outro) 

classificar em ordem ascendente os valores da primeira coluna. 

Indicar com um comentário qual foi o algoritmo escolhido.

Imprimir a matriz lida sob a forma de tabela.

Os valores ordenados da primeira coluna devem ser impressos em uma linha com o titulo "Valores ordenados". Atenção não pode imprimir a lista sem formatar'''

from random import randint

def Ler():
    i = 0
    l = []
    with open('aam.txt','w+') as file:
        while i < 40:
            num = randint(1, 99)
            l.append(num)
            if num not in l:
                num = randint(1, 99)
                file.write(str(num)+'\n')
                i += 1
            #print(num)
            else:
                file.write(str(num)+'\n')
                i += 1
    return num

def GeraMatriz():
    while True:
        try:
            m = int(input('Digite um termo para ser o quadrado da matriz: '))
            if m < 2 or m > 6: raise ValueError
            break
        except ValueError: 
            print('M invalido. Tente novamente')

    return m

def LerMatriz(m):
    with open('aam.txt','r') as file:
        x = 0
        v = file.readlines()
        a = [None] * m
        for i in range(m):
            a[i] = [None] * m
            for j in range(m):
                a[i][j] = v[x]
                x += 1
    return a, i, j

def Escolhe(a):
    lista = []
    for i in range(m):
        lista.append(a[i][0])
    return lista

def Ordena(lista): #O Algoritmo escolhido foi o bubble sort
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                ordenado = False
    return lista

def Impr(m, a, valores):
    print('\nMatriz A:\n')
    for i in range(m):
        for j in range(m):
            print('|{:.2f}| '.format(int(a[i][j])), end = '')
        print()
    print('Valores da primeira coluna: {}'.format(lista))

num = Ler()
m = GeraMatriz()
a, i, j = LerMatriz(m)
lista = Escolhe(a)
lista = Ordena(lista)
Impr(m, a, lista)