'''i = soma = 0
maiorn = ''

while True:
    try:
        nome = input('Digite um nome: ')
        if nome == '1': break
    except:
        print('Ha algum erro no texto')
    try:
        idade = int(input('Digite uma idade: '))
        i += 1
        soma += idade
    except:
        print('Ha algum erro no numero. ')

    if len(nome) > len(maiorn):
        maiorn = nome
    
    media = soma // i
print('O maior nome eh {} e a media de idades eh {} anos'.format(maiorn, media))'''

def Ler():
    soma = i = 0
    
    while True:
        try:
            nome = input('Digite um nome: ').lower()
            if nome.isnumeric(): raise
            if nome == 'sair': break
        except:
            print('O texto pode ser um numero')
        
        try:
            idade = int(input('Digite uma idade: '))
            i += 1
            soma += idade
            if idade.isalpha(): raise
        except:
            print('Voce nao digitou um numero')
    return nome, i, soma

def Calculo(nome, i, soma):
    maiorn = ''
    if len(nome) > len(maiorn):
        maiorn = nome
    media = soma // i
    return maiorn, media

def Impr(maiorn, media):
    print('O maior nome eh {} e a media de idades eh {} anos'.format(maiorn, media))
    return

nome, i, soma = Ler()
maiorn, media = Calculo(nome, i, soma)
Impr(maiorn, media)