'''Elabore um programa que leia uma matriz quadrada de tamanho mxm
elementos inteiros e, verifique se a matriz é identidade. Imprimir a matriz lida
sob a forma de tabela e o resultado obtido.'''

def Gera():
    try:
        m = int(input('Digite um termo para o quadrado: '))
    except ValueError:
        print('Erro. Tente novamente...')
        m = int(input('Digite um termo para o quadrado: '))
    return m

def Forma(m):
    M = [None] * m
    for i in range(m):
        M[i] = [None] * m
        for j in range(m):
            while True:
                try:
                    M[i][j] = float(input(f'Digite M = ['+str(i+1)'],['+str(j+1)+']: '))
                    break
                except ValueError:
                    print('Erro na matriz. Digite novamente...')
    return a

def MatrizIdent(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j and a[i][j] != 1:
                return False
            elif i != j and a[i][j] != 0:
                return False
    return True
def Resultado(a):
    if MatrizIdent(a) == False:
        print('\nA matriz nao eh identidade\n')
    else:
        print('\nA matriz eh identidade\n')

    print ('\nMatriz gerada\n')
    for i in range(m):
        for j in range (m):
            print ('|{:.2f}|'.format(a[i]][j]),end=' ')
        print()
    return


m = Gera()
M = Forma(m)
Reesultado(M)