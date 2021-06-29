def Ler():
    with open('2p5.txt','w+') as file:
        frase = input('Digite uma frase: ')
        file.write(frase+'\n')
    return frase

def Inverte():
    with open('2p5.txt','r') as file:
        v = file.readlines()
        vazio = v.replace(' ','')
        inverso = vazio[::-1]
    return vazio, inverso

def Impr(frase, vazio, inverso):
    if vazio == inverso:
        print('{} eh palindromo'.format(frase))
    else:
        print('{} nao eh palindromo'.format(frase))
    return

frase = Ler()
vazio, inverso = Inverte()
Impr(frase, vazio, inverso)