'''Dizemos que uma matriz quadrada inteira é um quadrado mágico se a soma dos elementos de
cada coluna e a soma dos elementos das diagonais principal e secundária são todas iguais.
Elabore um programa Python que grave em um arquivo uma quantidade indeterminada de
dados numéricos inteiros. Ler estes dados e verificar se os dados lidos correspondem a um
quadrado mágico de uma matriz quadrada de mxm elementos.'''

def Ler():
    while True:
        try:
            m = int(input('Diga um termo m: '))
            break
            if m < 2: raise ValueError
        except ValueError:
            print('Erro no termo m')

    t = m ** 2

    with open('ex10p5.txt','w+') as file:
        for i in range(t):
            while True:
                try:
                    n = int(input('Digite um numero:'))
                    file.write(str(n)+'\n')
                    break
                except ValueError: 
                    print('Erro ao digitar n')
    return m

def Matrix(m):
    with open('ex10p5.txt', 'r') as file:
        k = 0
        valores = file.readlines()
        a = [None] * m
        for i in range(m):
            a[i] = [None] * m
            for j in range(m):
                a[i][j] = valores[k]
                k += 1
    return a

def Calculo(a):
    dp = ds = 0
    somac = 0
    somal = 0
    resul = 0

    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                dp += int(a[i][j])

    for i in range(-1,(-len(a)-1), -1): # percorre a lista do último item ao primeiro
        for j in range(-1,(-len(a)-1), -1): # o mesmo de cima
            if i == j:
                ds += int(a[i][j])

    for i in range(len(a[0])):
        for j in range(len(a)):
            somac = a[i][j]
    
    for i in range(len(a[0])):
        for j in range(len(a)):
            somal = a[i][j] + a[i+1][j+1]

    if dp == ds == somac == somal:
        return True
    else:
        return False
    
    return dp, ds, somac

def Impr(a):
    if Calculo(a) == True:
        print('\nEh um quadrado magico\n')
    else:
        print('\nNao eh um quadrado magico\n')

    print('\nMATRIZ')
    for i in range(m):
        for j in range(m):
            print ('|{:.2f}|'.format(int(a[i][j]),end=' '))
        print()
    
    return

m = Ler()
a = Matrix(m)
Calculo(a)
Impr(a)