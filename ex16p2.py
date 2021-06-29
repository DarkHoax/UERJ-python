def Criptografa():
    try:
        frase = input('Digite uma frase: ')
        return frase
    except:
        return 'Nao possivel salvar a frase'
        


def Traduz(frase):
    saida = ''
    for i in frase:
        saida += chr(ord(i) - 1)
    return saida

def Impr(frase, saida):
    print('Frase: {}'.format(frase))
    print('Cripto: {}'.format(saida))
    return

frase = Criptografa()
saida = Traduz(frase)
Impr(frase, saida)