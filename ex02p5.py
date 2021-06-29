'''Elabore um programa Python que grave em um arquivo um número indeterminado de nomes e
salários. Depois leia estes dados e verifique se um determinado nome lido se encontra entre
os valores gravados. Exibir o nome e salário caso o nome exista ou mensagem “nome não
encontrado ‘. Usar pesquisa binaria. Os salários devem ser validados.'''
def Ler():
    with open('aam.txt', 'w+') as file:
        while True:
            try:
                name = input('Nome: ').strip().lower()
                if name == '': break
                while True:
                    try:
                        sal = float(input('Salário: '))
                        if sal < 1000.00 or sal > 999999.99: raise ValueError
                        file.write(name+','+str(sal)+'\n')
                        break
                    except: 
                        print('Salário inválido, digite novamente:')
            except: 
                print('Nome inválido, tente novamente: ')
    return 

def Grava():
     temp=[]
     princ=[]
     with open('info2.txt', 'r') as arq:
        for linha in arq:
            valores=linha.split(',')
            temp.append(valores[0])         
            temp.append(valores[1].strip('\n'))
            princ.append(temp[:])
            temp.clear()
     return princ


def PesqBin(array):
    begin = 0
    mid = 0
    end = len(array)-1
    array.sort()
    find = False
    while True:
        try: 
            item = input('Nome a ser procurado: ').strip().lower()
            if item == '': raise
            break
        except: print('Dado inválido. Tente novamente: ')
        line()
    while begin <= end:
        mid = (begin + end) // 2
        if array[mid][0] == item:
            find = True
            break
        elif array[mid][0] < item:
            begin = mid+1
        else:
            end = mid-1
    return find,mid,item


def Resul(item):
    if find:
        print('O nome -> {} foi encontrado. Salário:  R${:.2f}'.format(item, float(princ[mid][1])))
    else:
        print('O nome -> {} não foi encontrado'.format(item))


#main
Ler()
princ = Grava()
find, mid, item = PesqBin(princ)
Resul(item)



              
                                           