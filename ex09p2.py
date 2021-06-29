def Ler():
    try:
        frase = input('Digite uma frase: ').lower()
    except:
        print('Nao eh uma frase')
    return frase

def Separa(frase):
    v = c = 0
    lista = frase.split()
    lista1 = lista[0]
    for i in lista1:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            v += 1
        else:
            c += 1
    return lista1, v, c

def Impr(lista1, v, c):
    print('\nA primeira frase eh {}\nExistem {} vogais e {} consoantes'.format(lista1, v, c))
    return

frase = Ler()
lista1, v, c = Separa(frase)
Impr(lista1, v, c)