def Ler():
    try:
        frase = input('Digite uma frase: ').strip().lower()
    except:
        print('Nao eh um texto')
    return frase

def Analisa(frase):
    v = b = 0
    for i in frase:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            v += 1
        if i == ' ':
            b += 1
    return v, b

def Impr(v, b):
    try:
        print('\nExistem {} vogais e {} espacos em brancos'.format(v, c))
    except:
        print('Impossivel printar')
    return

frase = Ler()
v, c = Analisa(frase)
Impr(v, c)