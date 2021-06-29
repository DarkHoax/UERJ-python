def Gera():
    #Gera linhas por colunas
    while True:
        try:
            m = int(input('Digite um termo para m: '))
            if m < 2:
                raise ValueError
            break
        except ValueError:
            print("MATRIZ INVÁLIDA, TENTE NOVAMENTE!")
    return m

def Forma(m):
    M = [None] * m
    for i in range(m):
        M[i] = [None] * m
        for j in range(m):
            while True:
                try:
                    M[i][j] = float(input('Digite M = ['+str(i+1)+'],['+str(j+1)+']: '))
                    break
                except ValueError:
                    print('Erro na matriz. Digite novamente...')
    return M

def MatrizIdent(M):
    for i in range(len(M)):
        for j in range(len(M)):
            if i == j and M[i][j] != 1:
                return False
            elif i != j and M[i][j] != 0:
                return False
    return True
def Resultado(M):
    if MatrizIdent(M) == False:
        print('\nA matriz nao eh identidade\n')
    else:
        print('\nA matriz eh identidade\n')

    print ('\nMatriz gerada\n')
    for i in range(m):
        for j in range (m):
            print ('|{:.2f}|'.format(M[i][j]),end=' ')
        print()
    return


m = Gera()
M = Forma(m)
Resultado(M)