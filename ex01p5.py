def Ler():
    while True:
        try:
            col = int(input('Digite as colunas: '))
            if col > 1: break
            else: raise
        except: print('Erro, digite novamente')
    termo = col ** 2
    with open('ex01p5.txt','w+') as file:
        for i in range(termo):
            while True:
                try:
                    n = int(input('Digite um numero inteiro: '))
                    file.write(str(n)+'\n')
                    break
                except: print('Erro, digite novamente: ')
    return col

def Matriz(col):
    with open('ex01p5.txt','r') as file:
        k = 0
        valores = file.readlines()
        for i in range(col):
            a[i] = [None] * col
            for j in range(col):
                a[i][j] = valores[k]
                k += 1
    return a

def Calculo(a):
    d = linhas = resul = 0
    for i in range(len(a)):
        d += int(a[i][j])
        if cols > 1:
            linhas += int(a[0][j]) + int(a[1][j])
        else: linhas = int(a[i][i])
    resul = d - linhas
    return resul

def Impr(resul, a): #< --- Imprimindo
    print('Matriz A:')
    for i in range(cols):
        for j in range (cols):
            print('[{:.2f}]'.format(int(a[i][j])), end = '')
        print()
    print('Resultado da operação -> {}'.format(resul))


#main
col = Ler()
a = Matriz(col)
resul = Calculo(a)
Impr(resultado,matrix)