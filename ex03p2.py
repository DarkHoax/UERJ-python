def Ler():
    nome = input('Digite um nome [pode usar palavras em minusculo ou maiusccula]: ').strip()
    return nome
def InvNome(nome):
    #Inverte o nome
    inverte = nome[::-1]
    return inverte

def Impr(nome, inverte):

    print('O nome {} ao contrario eh {}.'.format(nome, inverte.upper()))
    return

nome = Ler()
inverte = InvNome(nome)
Impr(nome, inverte)