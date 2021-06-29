def Ler():
    try:
        frase = input('Digite uma frase ou palavra: ').lower()
    except:
        print('Nao eh um texto')
    return frase

def Contador(frase):
    v = c = 0
    try:
        for i in frase:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                v += 1
            else:
                c += 1
    except:
        print('Nao foi digitado um texto')
    return v, c

def Impr(v, c):
    print('Existem {} vogais nessa frase'.format(v))
    print('Existem {} consoantes nessa frase'.format(c))
    return

frase = Ler()
v, c = Contador(frase)
Impr(v, c)