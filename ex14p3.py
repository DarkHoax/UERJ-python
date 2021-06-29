'''A normalização de uma matriz é realizada, dividindo cada elemento da matriz A
pelo maior elemento da linha correspondente. Elabore um programa leia uma
matriz de mxn elementos inteiros e que permita determinar a matriz
normalizada. Imprimir a matriz lida e a normalizada'''

def Gera():
    while True:
        try:
            m = int(input('Digite um termo para a linha: '))
            n = int(input('Digite um termo para a coluna: '))
            break
        except ValueError:
            print('Erro. Tente novamente...')
            m = int(input('Digite um termo para a linha: '))
            n = int(input('Digite um termo para a coluna: '))
    return m, n

def Forma(m, n):
    a = [None] * m
    for i in range(m):
        a[i] = [None] * n
        for j in range(n):
            while True:
                try:
                    a[i][j] = float(input('Digite A = ['+str(i+1)+'],['+str(j+1)+']: '))
                    break
                except ValueError:
                    print('Erro na matriz. Digite novamente...')
    return a

def Norma(a):
    mat = []
    for i in range(len(a)):
        linha = [0] * (len(a[0]))
        mat.append(linha)
    for i in range(m):
        maior = max(a)
        for j in range(n):
            mat[i][j] = a[i][j] / maior 
    return mat

def Impr(maior, a, mat):
    #Matriz original
    print('\nMATRIZ ORIGINAL')
    for i in range(m):
        for j in range(n):
            print ('|{:.2f}|'.format(a[i][j]),end=' ')
        print()

    #Matriz Normalizada
    print('\nMATRIZ NORMALIZADA')
    for l in range(m):
        for c in range(n):
            print ('|{:.2f}|'.format(mat[i][j]),end=' ')
        print()

    return

m, n = Gera()
a = Forma(m, n)
mat = Norma(a)
Impr(a, mat)