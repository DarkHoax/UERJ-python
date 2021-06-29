'''Elabore um programa que leia duas matrizes de tamanho mxn valores inteiros.
Determinar a matriz soma. Imprimir as matrizes lidas e a matriz soma sob a
forma de tabela. Verificar se as dimensões das duas matrizes são iguais.'''

def GeraA():
    try:
        l = int(input('Digite um termo para l: '))
        c = int(input('Digite um termo para c: '))
    except ValueError:
        print('Erro. Tente novamente...')
        l = int(input('Digite um termo para l: '))
        c = int(input('Digite um termo para c: '))
        
    a = [None] * l
    for i in range(l):
        a[i] = [None] * c
        for j in range(c):
            while True:
                try:
                    a[i][j] = float(input('Digite A = ['+str(i+1)+'],['+str(j+1)+']: '))
                    break
                except ValueError or TypeError:
                    print('Erro na matriz. Digite novamente...')
    return a

def GeraB():
    try:
        lb = int(input('Digite um termo para c: '))
        cb = int(input('Digite um termo para l: '))
    except ValueError:
        print('Erro. Tente novamente...')
        lb = int(input('Digite um termo para c: '))
        cb = int(input('Digite um termo para l: '))
        
    b = [0] * lb
    for n in range(lb):
        a[n] = [0] * cb
        for k in range(cb):
            while True:
                try:
                    b[n][k] = int(input('Digite B = ['+str(n+1)+'],['+str(k+1)+']: '))
                    break
                except ValueError or TypeError:
                    print('Erro na matriz. Digite novamente...')
    return b

def Impr(a, b, soma):
    for i in range(l):
        for j in range(c):
            valor_soma = a[i][j] + b[i][j]
            print('{} |'.format(soma), end='')
        print()

    #Forma matrizes
    print ('\nMatriz A Lida\n')
    for i in range(l):
        for j in range (c):
            print ('|{:.2f}|'.format(a[i][j]),end=' ')
        print()
    
    print ('\nMatriz B Lida\n')
    for i in range(ll):
        for j in range (cc):
            print ('|{:.2f}|'.format(b[n][k]),end=' ')
        print()
    return

a = GeraA()
b = GeraB()
res = Soma(a, b)
Impr(a, b)