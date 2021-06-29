
def Ler():
    i = soma = 0
    print('Digite "a" E um numero menor que zero para o programa parar')
    while True:
        nome = input('Digite um nome ["a" para parar]: ').lower()
        idade = int(input('Digite a idade[numero menor que 0 para parar]: '))
        soma += idade
        i += 1
        if nome == 'a' and idade < 0 : break
    maiorn = ''
    if len(nome) > len(maiorn):
        maiorn = nome    
    #Cacula media de idades
    media = soma//i
    return maiorn, media

def Impr(maiorn, media):
    print('O maior nome e {} e a media de idades eh {} anos'.format(maiorn, media))
    return

maiorn, media = Ler()
Impr(maiorn, media)