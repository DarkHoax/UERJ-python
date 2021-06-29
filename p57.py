'''
Elabore um programa Python que grave em um arquivo uma quantidade indeterminada de 
valores inteiros. Depois leia os dados para uma matriz A, quadrada de mxm(m é lido) valores 
inteiros. Construir a matriz B de mesmas dimensões tal que:
A primeira linha de B é a primeira linha de A somado com a segunda linha de A
A segunda linha de B é o fatorial dos termos da segunda linha de A
A terceira linha de B é a terceira linha de A vezes 3
Exibir as duas matrizes sob a forma e tabela..
'''
import math


def line():
    print('='*70)


def read_file():
    while True:
        try:
            m = int(input('Número de linhas da matriz: '))
            if m > 0: break
            else: raise
        except: print('Erro, tente novamente: ')
    terms = m**2
    a = 1
    with open('info7.txt', 'w+') as file:
        for i in range(terms): 
            while True:
                try:
                    n = input('Digite o termo: ')
                    test = int(n)
                    file.write(n+'\n')
                    break
                except: print('Erro, tente novamente: ')
    return m


def read_matrix(): 
    with open('info7.txt','r') as file:
        a = [None]*m
        for i in range(m):
            a[i] = [None]*m
            for j in range(m):
                a[i][j] = int(file.readline())
    return a


def generate():
    b = [None]*m
    for i in range(m):
        b[i] = [None]*m
    return b


def assign(a,b):
    for i in range(m):
        try:
            b[0][i] = a[0][i] + a[1][i]
            b[1][i] = math.factorial(int(a[1][i]))
            b[2][i] = a[2][i]*3
        except: print('Ordem menor que 3.'), line()
    for j in range(m):
        for i in range(3,m):
            try:
                b[i][j] = a[i][j]
            except: print('Ordem menor que 3.')
    return b


def impr(a,b):
    line()
    print('Matriz A:')
    for i in range(m):
        for j in range (m):
            print(f'[{int(a[i][j]):^5.2f}]', end = '')
        print()
    line()
    print('Matriz B:')
    for i in range(m):
        for j in range(m):
            print(f'[{int(b[i][j]):^5.2f}]', end= '')
        print()
    return


#main
m = read_file()
array = read_matrix()
b = generate()
b = assign(array,b)
impr(array,b)
