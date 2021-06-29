'''Elabore um programa Python que grave em um arquivo uma quantidade indeterminada de
valores inteiros. Depois leia os dados para uma matriz A, quadrada de mxm(m é lido) valores
inteiros. 

Construir a matriz B de mesmas dimensões tal que:

A primeira linha de B é a primeira linha de A somado com a segunda linha de A
A segunda linha de B é o fatorial dos termos da segunda linha de A
A terceira linha de B é a terceira linha de A vezes 3
Exibir as duas matrizes sob a forma e tabela..'''
import math

def Linha():
    print('-'*20)

def Ler():
    while True:
        try:
            m = int(input('Digite um termo para m: '))
            break
            if m < 2: raise ValueError
        except ValueError:
            print('Termo invalido')
    
    termo = m ** 2
    with open('ex07p5.txt', 'w+') as file:
        for i in range(termo):
            while True:
                try:
                    n = int(input('Digite um termo: '))
                    break 
                except ValueError:
                    print('Digite um numero novamente...')
            file.write(str(n)+'\n')
    return m

def Matriz(m):
    with open('ex07p5.txt', 'r') as file:
        k = 0
        v = file.readlines()
        a = [None] * m
        for i in range(m):
            a[i] = [None] * m
            for j in range(m):
                a[i][j] = v[k]
                k += 1
    return a

def GeraOutra(a, m):
    b = [None]*m
    for i in range(m):
        b[i] = [None]*m
    
    for i in range(m):
        try:
            b[0][i] = a[0][i] + a[1][i]
            b[1][i] = math.factorial(int(a[1][i]))
            b[2][i] = a[2][i]*3
        except ValueError:
            print('Ordem menor que 3')
    for j in range(m):
        for i in range(3,m):
            try:
                b[i][j] = a[i][j]
            except ValueError: 
                print('Ordem menor que 3.')
    return b

def Impr(a, b):
    print('\nMATRIZ A\n')
    for i in range(m):
        for j in range(m):
            print('|{:.2f}|'.format(int(a[i][j])), end = '')
        print()
    Linha()

    print('\nMATRIZ B\n')
    for k in range(m):
        for l in range(m):
            print('|{:.2f}|'.format(int(b[k][l])), end = '')
        print()
    return

#PROGRAMA PRINCIPAL
m = Ler()
a = Matriz(m)
b = GeraOutra(a, m)
Impr(a, b)