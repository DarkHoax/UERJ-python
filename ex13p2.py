def Ler():
    try:
        frase = input('Digite uma frase: ')
    except NameError:
        print('Houve algum erro na escrita')
    return frase

def Inverte(frase):
    try:
        lista = frase.split()
        lista1 = lista[-1]
        inv = lista1[::-1]
    except:
        print('Houve algum erro na inversao.')
    return inv

def Impr(inv):
    try:
        print('A ultima palavra invertida eh: {}'.format(inv))
    except: 
        print('Houve erro de impressao')
    return

frase = Ler()
inv = Inverte(frase)
Impr(inv)
