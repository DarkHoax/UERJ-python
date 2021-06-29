'''Elabore um programa que leia duas listas de igual comprimento e permita
intercalar os seus elementos. 

Exemplo: [’a’,10,’b’,20,’c’,30,’d’,40] e o resultado
depois de intercalar as listas: L1=[’a’,’b’,’c’,’d’] e L2= [10,20,30,40]. 
O programa deverá verificar se as listas são de igual comprimento'''

def LerA():
    i = 0
    l1 = []
    resp1 = input('Deseja digitar uma lista de numeros [N] ou Caracteres [C]?: ').strip().upper()
    if resp1 == 'N':
        try:
            termo1 = int(input('Digite um termo para L1: '))
        except ValueError:
            print('Nao foi digitado um numero para o termo 1')
        while i < termo1:
            try:
                num = int(input('Digite um numero para L1: '))
                l1.append(num)
                i += 1
            except ValueError:
                print('Nao digitou um numero')
    
    if resp1 == 'C':
        try:
            termo1 = int(input('Digite um termo para L1: '))
        except ValueError:
            print('Nao foi digitado um numero para o termo 1')
        while i < termo1:
            try:
                car = input('Digite um caractere para L1: ')
                l1.append(car)
                i += 1
            except:
                print('Digitou um caractere invalido')
    return l1

def LerB():
    j = 0
    l2 = []
    resp2 = input('Deseja digitar uma lista de numeros [N] ou Caracteres [C]?: ').strip().upper()
    if resp2 == 'N':
        try:
            termo1 = int(input('Digite um termo para L1: '))
        except ValueError:
            print('Nao foi digitado um numero para o termo 1')
        while i < termo2:
            try:
                num = int(input('Digite um numero para L1: '))
                l2.append(num)
                j += 1
            except ValueError:
                print('Nao digitou um numero')
    
    if resp2 == 'C':
        try:
            termo2 = int(input('Digite um termo para L1: '))
        except ValueError:
            print('Nao foi digitado um numero para o termo 1')
        while j < termo2:
            try:
                car = input('Digite um caractere para L1: ')
                l2.append(car)
                j += 1
            except:
                print('Digitou um caractere invalido')
    return l2

def Calculo(l1, l2):
    l3 = []
    try:
        if len(l1) == len(l2):
            l3 = l1 + l2
        else:
            return print('Lista sao de tamanhos diferentes')
    except EOFError:
        print('Deu erro no cruzamento das listas')
    return l3

def Impr(l1, l2, l3):
    print('L1 = {}\nL2 = {}'.format(l1, l2))
    print('A concatenacao da lista eh L3 = {}'.format(l3))

l1 = LerA()
l2 = LerB()
l3 = Calculo(l1, l2)
Impr(l1, l2, l3)