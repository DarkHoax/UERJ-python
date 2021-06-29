'''
Elabore um programa Python que grave em um arquivo uma quantidade indeterminada de
dados numéricos inteiros. Depois leia estes dados para uma matriz quadrada de m x m valores
inteiros – sabe-se que m é lido. Calcule e imprima os termos resultantes do somatório dos
termos da 1a coluna com o somatório dos termos da 2a 
linha e subtraído do somatório dos
termos da diagonal principal. Validar os dados.
'''
def line():
    print('*'*70)


def read_file(): #< --- Ler o arquivo
    while True:
        try:   
            cols = int(input('Número de colunas/linhas: '))
            if cols > 0 :break
            else: raise
        except: print('Erro, digite novamente: ')
    terms = cols**2
    with open('info.txt', 'w+') as file:
        for i in range(terms):
            while True:
                try:
                    n = input('Digite um número inteiro: ')
                    n1 = int(n)
                    file.write(n+'\n')
                    break
                except: print('Erro, digite novamente: ')
    return cols


def read_matrix(cols): #< --- Atribuir os valores do arquivo em uma matriz
    with open('info.txt','r') as file:
        index = 0
        list_of_values = file.readlines()
        a = [None] * cols
        for i in range(cols):
            a[i] = [None] * cols
            for j in range(cols):
                a[i][j] = list_of_values[index]
                index += 1
    return a


def operations(a): #< --- Operações com a matriz
    diagonal = 0
    sum_of_lines = 0
    resultado = 0
    for i in range(len(a)):
        diagonal += int(a[i][i])
        if cols > 1:
            sum_of_lines += (int(a[0][i]) + int(a[1][i]))
        else: sum_of_lines = int(a[i][i])
    resultado = sum_of_lines - diagonal
    return resultado


def result(a,b): #< --- Imprimindo
    line()
    print('Matriz A:')
    for i in range(cols):
        for j in range (cols):
            print('[{:.2f}]'.format(int(b[i][j])), end = '')
        print()
    line()
    print('Resultado da operação -> {}'.format(a))
    line()


#main
cols = read_file()
matrix = read_matrix(cols)
resultado = operations(matrix)
result(resultado,matrix)

    





    
    