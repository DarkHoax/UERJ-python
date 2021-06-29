'''Elabore um programa Python que grave em um arquivo uma quantidade indeterminada
de valores inteiros. Depois leia os dados para uma matriz A. . Crie um programa Python que
tenha uma função que permita normalizar uma matriz de números inteiros dada como
parâmetro A normalização de uma matriz é realizada, dividindo cada elemento da matriz A pelo
maior elemento da linha correspondente'''

def linha():
    print('='*60)


def Ler():
    while True:
        try:
            l = int(input('Digite a quantidade de linhas:  ')) 
            c = int(input('Digite a quantidade de colunas: '))
            if l < 1 or c < 1: raise ValueError
            break
        except ValueError:
            print('Dado inválido. Tente novamente: ')
    t = l * c
    with open('ex14p5.txt','w+') as file:
        for i in range(t):
            while True:
                try:
                    n = int(input('Digite um valor: '))
                    break
                except ValueError:
                    print('Tente novamente...')
            file.write(str(n)+'\n')
    return l, c

def Grava(l, c):
    with open('ex14p5.txt','r') as file:
        k = 0
        v = file.readlines()
        a = [None] * l
        for i in range(l):
            a[i] = [None]* c 
            for j in range(c):
                a[i][j]= v[k]
                k += 1
    return a

def Normaliza(a):
    normalizada = []
    for i in range (len(a)):
            linha = [0] * (len(a[0]))
            normalizada.append(linha)
    for i in range (l):
        maior = max(a[i])
        for j in range (c):
            normalizada[i][j] = a[i][j] / maior
    return normalizada
    


def Impr(a, normalizada):
    linha()
    print('Matriz principal:')
    for i in range(l):
        for j in range(c):
            print('[{:.2f}]'.format(int(a[i][j])), end = '')
        print()
    linha()
    print('Matriz normalizada: ')
    for i in range(l):
        for j in range(c):
            print('[{:.2f}]'.format(int(normalizada[i][j])), end = '')
        print()


l, c = Ler()
a = Grava(l, c)
normalizada = Normaliza(a)
Impr(a, normalizada)