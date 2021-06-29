'''Elabore um programa que leia uma matriz quadrada A de tamanho m, calcule o
número de zeros contidos na matriz. Imprimir a matriz lida sob a forma de tabela
e o resultado obtido.'''

def GeraMatrix():
    #Gera uma matriz quadrada
    matriz = []    
    while True:
        try:
            m = int(input('Digite um termo para fazer uma matriz quadrada [m x m]: '))
            break
        except ValueError:
            print('Nao digitou um valor ou digitou uma letra')
    termos = m ** 2

    with open('5p5.txt','w+') as file:
        for i in range(termos):
            while True:
                try:
                    n = int(input('Digite um numero: '))
                    break
                except ValueError:
                    print('Numero errado. Tente novamente...')
                file.write(str(n)+'\n')
    return m

def Ler(m):
    #Aqui se forma a matriz
    with open('5p5.txt','r') as file:
        k = 0
        v = file.readlines()
        a = [None] * m
        for i in range(m):
            a[i] = [None] * m
            for j in range(m):
                a[i][j] = v[k]
                k += 1
            matriz.append(a[i][j])
    return a, matriz

def ContaZeros(matriz):
    #O codigo ira percorrer cada linha da matriz a procura de zero
    cont = 0
    for z in range(len(matriz)):
        if z == 0:
            cont += 1
    return cont

def Impr(a, cont):
    print('O total de zeros na matriz eh {}'.format(cont))
    for l in range(len(a)):
        for c in range(len(a)):
            print('[{}]'.format(a[l][c]), end='')
        print()
    return

m = GeraMatrix()
a, matriz = Ler(m)
cont = ContaZeros(a)
Impr(a, cont)