'''Elabore um programa que leia uma matriz de tamanho mxm elementos inteiros
e, determine a primeira linha ordenada de forma ascendente. Não pode usar
sort().'''

def Gera():
    while True:
        try:
            m = int(input('Digite um termo para o quadrado: '))
            break
        except ValueError or m == '':
            print('Erro. Tente novamente...')
            m = int(input('Digite um termo para o quadrado: '))
    return m

def Forma(m):
    a = [None] * m
    for l in range(m):
        a[l] = [None] * m
        for c in range(m):
            while True:
                try:
                    a[l][c] = int(input('Digite A = ['+str(l+1)+'],['+str(c+1)+']: '))
                    break
                except ValueError:
                    print('Erro na matriz. Digite novamente...')
    return a

def Ordena(a):
    pl = []
    linha = 0
    for k in range(len(a)):
        if k == a[0]:
            linha += a[li]
        pl.append(linha)
    return pl

def Bubble(pl):
    elementos = len(pl)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if pl[i] > pl[i+1]:
                pl[i], pl[i+1] = pl[i+1], pl[i]
                ordenado = False        
        print(pl)
    return pl
def Impr(pl):
    print('A linha 1 ordenada eh {}'.format(pl))
    return

m = Gera()
a = Forma(m)
pl = Ordena(a)
Impr(pl)