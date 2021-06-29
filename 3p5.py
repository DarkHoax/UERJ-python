'''. Elabore um programa que leia dois vetores e determine o número de elementos
em comum entre 2 listas dadas como parâmetro. Exemplo: L1=[1,2,3,4,5] e
L2=[2,4]tem 2 elementos em comum.'''

def LerA():
    i = 0
    with open('3p5.txt','w+') as file:
        while True:
            try:
                n = int(input('Digite um termo para parar a sequencia: '))
                break
            except ValueError:
                print('Digite n novamente...')
        
        while i < n: 
            while True:
                try:
                    num = int(input('Digite um numero para L1: '))
                    i += 1
                    break
                    file.write(str(num)+'\n')
                except ValueError:
                    print('Nao eh um numero.')
    return

def LerB():
    j = 0
    with open('3p5-2.txt','w+') as file:
        while True:
            try:
                k = int(input('Digite um termo para parar a sequencia: '))
                break
            except ValueError:
                print('Digite n novamente...')
        
        while j < k: 
            while True:
                try:
                    num2 = int(input('Digite um numero para L1: '))
                    j += 1
                    break
                    file.write(str(num2)+'\n')
                except ValueError:
                    print('Nao eh um numero.')
    return 

def IteraA():
    l1 = []
    with open('3p5.txt','r') as file:
        k = 0
        for i in file:
            b = file.readlines()
            l1.append(int(b))
            k += 1
    return l1

def IteraB():
    l2 = []
    with open('3p5-2.txt','r') as file:
        m = 0
        for j in file:
            v = file.readlines()
            l2.append(int(v))
            m += 1
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
LerA()
LerB()
l1 = IteraA()
l2 = IteraB()
cont = Calculo(l1, l2)
Impr(l1, l2, cont)