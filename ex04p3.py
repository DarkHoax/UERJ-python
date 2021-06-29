'''Elabore um programa que determine o tamanho t da maior sequência de números
iguais em uma lista A. Exemplo: Supor que sejam armazenados os seguintes
valores para a lista A: [1,1,6,6,7,7,7,7,1,1,1], então t=4.'''

def Ler():
    l1 = []
    i = 0
    
    try:
        n = int(input('Digite um termo para a lista: '))
    except ValueError:
        print('Termo nao eh um numero')
        n = int(input('Digite um termo para a lista: '))
    
    while True:    
        try:
            val = int(input('Digite um valor: ')).strip().lower()
            if val == -10: break
            l1.append(val1)
            i += 1
        except:
            print('Nao eh um valor valido')
            val1 = input('Digite um numero')
            l1.append(val1)
            i += 1
    return l1

def Lista(l1):
    cont = 0
    for i in l1:
        if l1[i] == i:
            cont += 1
        