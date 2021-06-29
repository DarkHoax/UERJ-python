def Ler():
    try:
        frase = input('Digite uma frase: ')
    except:
        print('Nao eh um texto')
    return frase

def Cripto(frase):
    saida = ''
    for i in frase:
        saida += chr(ord(i) + 2)
    return saida

def Impr(frase, saida):
    print('\nFrase descriptografada: {}'.format(frase))
    print('\nFrase criptografada: {}'.format(saida))
    return

frase = Ler()
saida = Cripto(frase)
Impr(frase, saida)