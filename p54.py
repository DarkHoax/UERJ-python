'''Um grupo de amigos deseja saber quem é o mais velho. Para isso desenvolveram um 
programa Python que para ler de um arquivo o nome e idade. Elabore um programa Python
para exibir o nome do amigo mais velho – suponha que não existam pessoas que tenham 
nascido na mesma data.'''
def line():
    print('='*70)


def read_file():
    with open('info4.txt', 'w+') as file:
        while True:
            try:
                name = input('Digite o nome <enter> para encerrar: ').strip().upper()
                if name == '': break
                elif name.isalpha() and len(name) >= 3:
                    while True:
                        try:
                            age = input('Digite a idade: ')
                            test = int(age)
                            if test <= 0: raise
                            file.write(name+','+age+'\n')
                            break
                        except: print('Idade inválida, tente novamente: ')
                else: raise
            except: print('Nome inválido, tente novamente: ')
    return


def read_array():
     temp=[]
     princ=[]
     with open('info4.txt', 'r') as arq:
        for linha in arq:
            valores=linha.split(',')
            temp.append(valores[0])         
            temp.append(valores[1].strip('\n'))
            princ.append(temp[:])
            temp.clear()
     return princ
    

def check_and_print(a):
    maximum = index = 0
    for i in range(len(a)):
        if int(a[i][1]) > maximum:
            maximum = int(a[i][1])
            index = i
    try:
        line()
        print(f'Nome da pessoa mais velha com {maximum} anos: --> {a[index][0]} ')
        line()
    except: print('Dados insuficientes.'),line()
    return 

#main
read_file()
princ = read_array()
check_and_print(princ)