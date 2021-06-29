'''
Elabore um programa Python que grave em um arquivo uma quantidade indeterminada 
de valores inteiros. Depois leia os dados para uma matriz A. . Crie um programa Python que 
tenha uma função que permita normalizar uma matriz de números inteiros dada como 
parâmetro A normalização de uma matriz é realizada, dividindo cada elemento da matriz A pelo 
maior elemento da linha correspondente.
'''
def line():
    print('='*70)


def read_file():
    while True:
        try:
            lines = int(input('Número de linhas: '))
            cols = int(input('Número de colunas: '))
            break
        except: print('Erro, tente novamente: ')
    qtd_terms = lines*cols
    with open('info14.txt', 'w+') as file:
        for i in range(qtd_terms):
            while True:
                try:
                    n = input('Número: ')
                    file.write(n+'\n')
                    break
                except: print('Erro, tente novamente: ')
    return lines,cols


def read_matrix(): 
    with open('info14.txt','r') as file:
        a = [None] * lines
        for i in range(lines):
            a[i] = [None] *cols
            for j in range(cols):
                a[i][j] = int(file.readline())
    return a



def normalize(a):
    normalized = []
    for i in range (len(a)):
            line = [0] * (len(a[0]))
            normalized.append(line)
    for i in range (lines):
        maior = max(a[i])
        for j in range (cols):
            normalized[i][j] = a[i][j] / maior
    return normalized


'''def result(a,b):
    line()
    print('Matriz lida: ')
    for l in range(lines):
        for c in range (cols):
            print(f'[{a[lines][cols]:^5.2f}]', end = '')
        print()
    line()
    print('Matriz normalizada: ')
    for i in range(lines):
        for j in range(cols):
            print(f'[{b[lines][cols]:^5.2f}]', end = '')
        print()
    line()
    return'''

def impr(a,b):
    line()
    print('Matriz principal:')
    for i in range(lines):
        for j in range (cols):
            print(f'{a[i][j]:^5.2f}', end = '')
        print()
    line()
    print('Matriz Normalizada: ')
    for i in range(lines):
        for j in range(cols):
            print(f'{b[i][j]:^5.2f}', end = '')
        print()
    return


#main
lines,cols = read_file()
matrix = read_matrix()
normalized = normalize(matrix)
impr(matrix,normalized)
#result(matrix,normalized)