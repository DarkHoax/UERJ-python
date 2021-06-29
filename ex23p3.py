'''23. Elabore um programa que leia para uma lista um conjunto indeterminado de
valores inteiros. (e depois) Determinar a quantos valores são maiores que a
média.'''

def Ler():
    b = i = 0
    lista = []
    n = int(input('Digite um numero para dar fim a sequencia: '))
    while i < n:
        try:
            num = int(input('Digite um numero: '))
            b += num
            lista.append(num)
            i += 1
        except ValueError:
            print('Digite novamente...')
    return lista, num, b

def Media(lista, b):
    media = maior = 0
    m = len(lista)
    media = b / m
    for i in lista:
        if i > media:
            maior += 1
    return media, maior

def Impr(lista, media, maior):
    print('A lista {} tem media {:<.2f} e {} numeros acima da media.'.format(lista, media, maior))
    return

lista, num, b = Ler()
media, maior = Media(lista, b)
Impr(lista, media, maior)
