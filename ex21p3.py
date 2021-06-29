'''Elabore um programa Python que leia nome e idade de um conjunto
indeterminado de pessoas. Imprima os valores lidos classificados em ordem
crescente por idade.'''

def Ler():
    temp=[]
    princ=[]

    while True:
        temp.append(str(input('Nome: ')))
        if temp[0] == '': break
        try:
            temp.append(float(input('Idade: ')))
        except ValueError:
            print('Salario errado')        
        princ.append(temp[:])
        temp.clear()
    return princ

def Ordena(princ):
    ordem = sorted(princ, key=lambda princ:princ[1])

    elementos = len(ordem)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if princ[i] > princ[i+1]:
                princ[i], princ[i+1] = princ[i+1], princ[i]
                ordenado = False
    return princ

def Impr(princ):
    print(princ)
    return

princ = Ler()
princ = Ordena(princ)
Impr(princ)