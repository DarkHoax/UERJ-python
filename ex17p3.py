'''Elabore um programa Python que armazene em duas listas uma quantidade
indeterminada de nomes e salários. Depois verifique se um determinado nome
se encontra entre os valores lidos. Caso exista exibir o nome e o salario ou
mensagem indicativa. Usar pesquisa binaria. Flag a livre escolha'''

def le():
    temp=[]
    princ=[]

    while True:
        temp.append(str(input('Nome: ')))
        if temp[0] == '': break
        try:
            temp.append(float(input('Salario: ')))
        except ValueError:
            print('Salario errado')        
        princ.append(temp[:])
        temp.clear()    
    return princ

def pb(princ):
    ordem = sorted(princ, key=lambda princ:princ[0])
    inicio, fim = 0, len(ordem)-1
    achei = False
    p = input('Nome a procurar: ')

    while inicio<=fim:
        meio = (inicio+fim)//2 
        if ordem[meio][0] == p:            
            achei = True
            break
        elif ordem[meio][0] < p:
            inicio = meio + 1
        else:
            fim = meio - 1  
    return ordem, achei, meio, p             
        
def impr(princ,achei,i,p):
    if achei:
        print('O {} tem o salario de R${:<.2f}'.format(princ[i][0], princ[i][1]))
    else:
        print('{} não foi encontrado'.format(p))
    return

princ = le()
ordem, achei, i, p = pb(princ)
impr(ordem,achei,i,p)