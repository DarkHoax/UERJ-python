def Ler():
    try:
        frase = input('Digite uma frase: ').strip().lower()
        if frase.isnumeric():
            print('isso eh um numero')
            raise
    except:
        print('Isso nao eh um texto')
    return frase

def Analisa(frase):
    try:    
        lista = frase.split()
        lista1 = lista[0]
        inv = lista1[::-1]
    except:
        print('Nao foi possivel cortar')
    return inv

def Impr(inv):
    try:
        print('\nA primeira palavra invertida eh {}'.format(inv))
    except:
        print('Nao foi printado por ser um numero')
    return

frase = Ler()
inv = Analisa(frase)
Impr(inv)