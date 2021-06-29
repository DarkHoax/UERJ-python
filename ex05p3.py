'''Elabore um programa que leia uma matriz quadrada A de tamanho m, calcule o
número de zeros contidos na matriz. Imprimir a matriz lida sob a forma de tabela
e o resultado obtido.'''

def GeraMatrix():
    #Gera uma matriz quadrada
    matriz = []

    try:
        m = int(input('Digite um termo para fazer uma matriz quadrada [m x m]: '))
    except ValueError:
        print('Nao digitou um valor ou digitou uma letra')
    
    #Aqui se forma a matriz
    a = [None] * m
    for i in range(m):
        a[i] = [None] * m
        for j in range(m):
            while True:
                try:
                    a[i][j] = int(input('A = ['+str(i + 1)+'],['+str(j + 1)+'] --> '))
                    break
                    matriz.append(a[i][j])
                except ValueError:
                    print('Valor nao eh um numero valido. Tente novamente...')
    return matriz

def ContaZeros(matriz):
    #O codigo ira percorrer cada linha da matriz a procura de zero
    cont = 0
    for z in range(len(matriz)):
        if z == 0:
            cont += 1
    return cont

def Impr(matriz, cont):
    print('O total de zeros na matriz eh {}'.format(cont))
    for l in range(len(matriz)):
        for c in range(len(matriz)):
            print('[{}]'.format(matriz[l][c]), end='')
        print()
    return

matriz = GeraMatrix()
cont = ContaZeros(matriz)
Impr(matriz, cont)