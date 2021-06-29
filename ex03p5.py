'''Elabore um programa Python que grave em um arquivo uma quantidade indeterminada de
valores inteiros. Depois leia os valores gravados para uma matriz de mxn (m e n são lidos)
valores inteiros determine e imprima o maior valor de cada coluna; validar os dados.'''
def linha():
    print('_'*20)
def Ler():
    while True:
        try:
            m = int(input('Digite um termo para a quantidade de linhas: '))
            break
        except ValueError:
            print('Numero invalido para linhas de matrizes')
    while True:
        try:
            n = int(input('Digite um termo para a quantidade de colunas: '))
            break
        except ValueError:
            print('Numero invalido para linhas de matrizes')
    
    mult = m * n

    with open('ex03p5.txt','w+') as file:
        for i in range(mult):
            while True:
                try:
                    num = int(input('Digite um numero: '))
                    break
                except ValueError:
                    print('Numero invalido. Tente novamente...')
            file.write(str(num)+'\n')
    return m, n

def LerArq(m, n):
    l = 0
    with open('ex03p5.txt', 'r') as file:
        v = file.readlines()
        a = [None] * m
        for i in range(m):
            a[i] = [None] * n
            for j in range(n):
                a[i][j] = v[l]
                l += 1
    return a

def Calculo(a):
    maior = -1
    total = 0
    for i in range(len(a[0])):
        for j in range(len(a)):
            if int(j) > maior:
                total = a[i][j]
    linha()    
    print('O maior valor da coluna '+str(j+1)+' eh {}'.format(total))
    linha()
    return total

def Impr(a):
    for i in range(m):
        for j in range(n):
            print('|{:.2f}|'.format(int(a[i][j])), end = '')
        print()
    return

#PRORAMA PRINCIPAL
m, n = Ler()
a = LerArq(m, n)
total = Calculo(a)
Impr(a)
