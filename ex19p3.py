'''Elabore um programa que leia para uma lista um conjunto indeterminado de
valores inteiros. Determinar e exibir a média dos valores lidos com 2 casas
decimais. Flag a livre escolha'''

def Ler():
    lista = []
    num = i = 0
    j = int(input('Digite um termo para a sequencia: '))
    while i < j:
        try:
            n = int(input('Digite um valor inteiro: '))
            num += n
            lista.append(n)
            i += 1
        except ValueError:
            print('Algo errado.')

    return lista, num

def Media(lista, num):
    media = 0
    m = len(lista)
    media = num / m
    return media

def Impr(lista, media):
    print('A media da lista {} eh {:<.2f}'.format(lista, media))
    return

lista, num = Ler()
media = Media(lista, num)
Impr(lista, media)