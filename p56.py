'''
 Elabore um programa Python que grave em um arquivo um número indeterminado de nomes, 
idades e sexo. Depois leia estes dados e determine os dados do homem mais jovem..
'''
def line():
    print('~'*70)


def read_file():
    with open('info6.txt','w+') as file:
        while True:
            try:
                n = input('Nome: ').strip().upper()
                if n =='': break
                elif n.isalpha() and len(n) >= 3:
                    while True:
                        try:
                            age = input('Idade: ')
                            test = int(age)
                            if test <= 0: raise
                            break
                        except: print('Idade inválida, tente novamente:')
                    while True:
                                try:
                                    sex = input('Sexo: (M/F): ').strip().upper()
                                    if sex == 'M' or sex == 'F':
                                        file.write(n+','+age+','+sex+'\n')
                                        break
                                    else: raise
                                except: print('Sexo inválido, digite novamente: ')
                else: raise
            except: print('Nome inválido, tente novamente: ')
    return


def read_array():
    index = None
    lower = 150
    temp=[]
    princ=[]
    with open('info6.txt', 'r') as arq:
        for linha in arq:
            valores=linha.split(',')
            temp.append(valores[0])         
            temp.append(valores[1])#strip('\n'))
            temp.append(valores[2].strip('\n'))
            princ.append(temp[:])
            temp.clear()
    for i in range(len(princ)):
         if princ[i][2] == 'M' and int(princ[i][1]) < int(lower):
             index = i
             lower = princ[i][1]
    try:
        line()
        print(f' O nome do homem mais velho com {lower} anos é o --> {princ[index][0]}')
        line()
    except:
        print('Dados insuficientes')
        line()
    return 


#main
read_file()
read_array()
