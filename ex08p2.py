def Ler():
    try:
        frase = input('Digite uma frase: ')
    except:
        print('Nao eh um texto')
    return frase

def CalcFrase(frase):
    lista = frase.split()
    return lista

def Impr(lista):
    print(lista[0])
    print(lista[-1])
    return

frase = Ler()
lista = CalcFrase(frase)
Impr(lista)