def Gera():
    try:
        m = int(input('Digite um termo para o quadrado: '))
    except ValueError:
        print('Erro. Tente novamente...')
        m = int(input('Digite um termo para o quadrado: '))
    return m

def Forma(m):
    a = [None] * m
    for i in range(m):
        a[i] = [None] * m
        for j in range(m):
            while True:
                try:
                    a[i][j] = float(input('Digite A = ['+str(i+1)+'],['+str(j+1)+']: '))
                    break
                except ValueError:
                    print('Erro na matriz. Digite novamente...')
    return a

def SomaSecundaria(a, m):
    soma = 0
    for i in range(-1,(-m-1), -1): # percorre a lista do último item ao primeiro
        for j in range(-1,(-m-1), -1): # o mesmo de cima
            if i == j:
                soma += a[i][j]
    return soma

def Impr(soma, a):
    if m < 1:
        print('Matriz Invalida')
    elif m == 1:
        for i in range(m):
            for j in range (m):
                print ('{:.2f}|'.format(a[i][j]),end=' ')
        print()
    else:
        print('\nA soma da diagonal secundaria eh {}\n'.format(soma))
        print ('\nMatriz Lida\n')
        for i in range(m):
            for j in range (m):
                print ('|{:.2f}|'.format(a[i][j]),end=' ')
            print()
    return


m = Gera()
a = Forma(m)
soma = SomaSecundaria(a, m)
Impr(soma, a)