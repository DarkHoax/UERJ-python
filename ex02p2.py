def Ler():
    frase = input('Digite uma frase: ')
    return frase

def Inverte(frase):
    #Tira os espacos em brancos
    vazio = frase.replace(' ','')
    #Inverte a frase
    inverso = vazio[::-1]
    
    return vazio, inverso

def Impr(frase, vazio, inverso):
    print('A frase {} '.format(frase), end='')
    if vazio==inverso:
        print('é palidroma')
    else:
        print('não é palíndroma')
    return

frase = Ler()
vazio, inverso = Inverte(frase)
Impr(frase, vazio, inverso)