'''. Elabore um programa que leia dois vetores e determine o número de elementos
em comum entre 2 listas dadas como parâmetro. Exemplo: L1=[1,2,3,4,5] e
L2=[2,4]tem 2 elementos em comum.'''

def LerA():
    i = 0
    l1 = []
    n = int(input('Digite um termo para parar a sequencia: '))
    while i < n: 
        try:
            num = int(input('Digite um numero para L1: '))
            l1.append(num)
            i += 1
        except ValueError:
            print('Nao eh um numero.')
    return l1

def LerB():
    j = 0
    l2 = []
    k = int(input('Digite um termo para parar a sequencia: '))
    while j < k: 
        try:
            num2 = int(input('Digite um numero para L2: '))
            l2.append(num2)
            j += 1
        except ValueError:
            print('Nao eh um numero.')
    return l2

def Calculo(l1, l2):
    cont = 0
    for l in l1:
        for m in l2:
            if l == m:
                cont += 1
    return cont

def Impr(l1, l2, cont):
    print('As listas L1 = {} e L2 = {} tem {} elementos em comum'.format(l1, l2, cont))
    return

#Main Program
l1 = LerA()
l2 = LerB()
cont = Calculo(l1, l2)
Impr(l1, l2, cont)