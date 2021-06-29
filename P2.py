def GeraN():
    #Gera um numero N que eh a qtd de pares
    try:
        n = int(input('Escreva um valor para N: '))
        if n < 0: raise 
    except Exception:
        print('Digitou um valor menor que 0. Digite novamente...')
        n = int(input('Escreva um valor para N:'))
    return n
    
def LerPalavra(n):
    #Percorre as 3 decisoes de n e gera 3 vezes 2 palavras
    for i in range(1, n + 1):
        p1 = input('\nDigite a primeira palavra ').strip().lower()
        p2 = input('\nDigite a segunda palavra ').strip().lower()    
    return p1,p2

def Analisa(p1, p2):
    #Analisa os sufixos
    sufixo = False

    if len(p1) > len(p2):
        return sufixo

    i = 0
    while len(p2) > i:
        if p1[i] != p2[i]:
            return sufixo
        i += 1
    sufixo = True
    return sufixo

def Resultado(sufixo, p1, p2):
    #Imprime
    if sufixo:
        print('A palavra {} é sufixo de {}'.format(p2, p1))
    else:    
        print('A palavra {} não é sufixo de {}'.format(p2, p1))
    return
n = GeraN()
p1, p2 = LerPalavra(n)
sufixo = Analisa(p1, p2)
Resultado(sufixo, p1, p2)