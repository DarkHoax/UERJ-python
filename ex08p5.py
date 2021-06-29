'''Elabore um programa Python que grave em um arquivo uma quantidade indeterminada de
dados numéricos reais. Depois leia os “n” primeiros valores e verifique a existência de
elementos iguais a média, imprimindo a posição em cada elemento se encontra. Modularizar
em pelo menos 3 funções.'''

def Ler():
    i = 0
    with open('ex08p5.txt','w+') as file:    
        while True:
            while True:
                try:
                    n = int(input('Digite um numero: '))
                    file.write(str(n)+'\n')
                    i += 1
                    break
                except ValueError:
                    print('Erro')
        if n < 0: break


    #Percorre a lista
    #Todo indice j eh listado numa variavel
    c = med = 0
    with open('ex08p5.txt','r') as file:
        for j in file:
            c += int(j)
        med = c // i
    print('\nMedia: {}'+'\n'.format(med))
    
    return med

def Compara(med):
    ig = 0
    with open('ex08p5.txt', 'r') as file:
        for l in file:
            if int(l) == med:
                ig += 1
                p = len(l)
    return ig, p

def Impr(ig, p):     
    if ig == 0:
        print('\nNAO EXISTEM ELEMENTOS IGUAIS A MEDIA\n')
    else:
        print('\nO total de elementos iguais sao {} elementos.'.format(ig), end = ' ')
        print('posicoes {}'.format(p))
    return    

#PROGRAMA PRINCIPAL
med = Ler()
ig, p = Compara(med)
Impr(ig, p)