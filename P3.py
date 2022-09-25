'''Elabore um programa que leia uma matriz retangular de tamanho mxn (m e n são lidos) elementos reais e 
determine o menor termo da matriz. Imprimir a matriz lida e o resultado obtido com mensagens
indicativas. Os valores devem ter 2 casas decimais.

não pode usar a função min() ou a biblioteca Numpy
m e n devem ser validados como valores inteiros e maiores ou iguais a 2'''

def Style():
    print('\n','~='*10)

def Gera():
    #Gera linhas por colunas
    while True:
        try:
            m = int(input('Digite um termo para m: '))
            n = int(input('Digite um termo para n: '))
            if m < 2 or n < 2:
                raise ValueError
            break
        except ValueError:
            print("MATRIZ INVÁLIDA, TENTE NOVAMENTE!")
    return m, n

def Forma(m, n):
    #Constroi a Matriz
    a = [None] * m
    for i in range(m):
        a[i] = [None] * n
        for j in range(n):
            while True: #Loop para nao sair [x][y] para [x+1][y + 1]
                try:
                    a[i][j] = float(input('\nDigite A = ['+str(i+1)+'],['+str(j+1)+']: '))
                    break
                except ValueError:
                    print('Erro na matriz. Digite novamente...')
    return a

def Minimo(a):
    menor = a[0][0]
    for r in range(len(a)):
        nums = a[r]
        for n in nums:
            menor = n if menor > n else menor
    return menor

def Impr(a, menor):
    #Printa a funcao
    Style()
    print('O menor valor da matriz eh {:.2f}'.format(menor))
    Style()
    print ('\nMatriz Lida\n')
    for i in range(m):
        for j in range(n):
            print ('| {:.2f} |'.format(a[i][j]),end=' ')
        print()
    return

#Programa principal
m, n  = Gera()
a = Forma(m, n)
menor = Minimo(a)
Impr(a, menor)