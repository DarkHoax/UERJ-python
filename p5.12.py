'''
Dizemos que uma matriz quadrada inteira é um quadrado mágico se a soma dos elementos de 
cada coluna e a soma dos elementos das diagonais principal e secundária são todas iguais. 
Elabore um programa Python que grave em um arquivo uma quantidade indeterminada de 
dados numéricos inteiros. Ler estes dados e verificar se os dados lidos correspondem a um 
quadrado mágico de uma matriz quadrada de mxm elementos.
'''
def line():
    print('='*70)


def read_file():
    while True:
        try:
            cols = int(input('Número de colunas/linhas: '))
            if cols <= 0: raise
            break
        except: print('Erro, tente novamente: ')
    with open('info12.txt', 'w+') as file:
        for i in range(cols**2):
            while True:
                try:
                    n = input('Número: ')
                    test = int(n)
                    file.write(n+'\n')
                    break
                except: print('Erro, tente novamente: ')
    return cols


def read_matrix():
    with open('info12.txt','r') as file:
        index = 0
        list_of_values = file.readlines()
        a = [None] * cols
        for i in range(cols):
            a[i] = [None] * cols
            for j in range(cols):
                a[i][j] = list_of_values[index]
                index += 1
    return a

lista = []
def sum_lines(a):
    for i in range(cols):
        soma = 0
        for j in range(cols):
            soma += int(a[i][j])
        lista.append(soma)
    return lista


def sum_colunes(a):
    for j in range(cols):
        soma = 0
        for i in range(cols):
            soma += int(a[i][j])
        lista.append(soma)
    return lista


def diagonal_principal(a):
    soma = 0
    for i in range(cols):
        soma += int(a[i][i])
    lista.append(soma)
    return lista


def diagonal_secundaria(a):
    soma = 0
    i = 0
    j = cols-1
    while i < cols:
        soma += int(a[i][j])
        i += 1
        j -= 1
    lista.append(soma)
    return lista


def impr(a):
    line()
    for l in range(cols):
        for c in range (cols):
            print(f'[{int(a[l][c]):^5}]', end = '')
        print()
    line()
    magico = True
    indice = 1
    while magico and indice < len(lista):
        if lista[indice] != lista[0]:
            magico = False
        indice += 1
    if magico:
        print('A matriz é um quadrado mágico.')
    else:
        print('A matriz não é um quadrado mágico.')
    return
#print(lista)
#main
cols = read_file()
matrix = read_matrix()
lista = sum_lines(matrix)
lista = sum_colunes(matrix)
lista = diagonal_principal(matrix)
lista = diagonal_secundaria(matrix)
impr(matrix)


