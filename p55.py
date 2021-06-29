'''Elabore um programa Python que grave em um arquivo um número indeterminado de nomes e 
idades. Depois leia estes dados e classifique por idade. Exibir os valores na ordem em que 
foram lidos e depois ordenados.'''

def line():
    print('='*70)

def read_file():
    with open('info5.txt', 'w+') as file:
        while True:
            try:
                name = input('Nome: ').strip().upper()
                if name == '': break
                elif name.isalpha() and len(name) >= 3:
                    while True:
                        try:
                            age = input('Idade: ')
                            test = int(age)
                            if test >= 0:
                                file.write(name+','+age+'\n')
                                break
                        except: print('Idade invalida, digite novamente: ')
                else: raise
            except: print('Nome inválido, tente novamente: ')
    return 


def read_array():
    temp = []
    princ = []
    with open('info5.txt','r') as file:
        for line in file:
            values = line.split(',')
            temp.append(values[0])
            temp.append(values[1])
            princ.append(temp[:])
            temp.clear()
    return princ


def sort_and_print(a):
    line()
    print('Lista na ordem lida: ')
    print(f"{'Nome':<30}{'Idade':>17}")
    for i in range(len(a)):
        print(f'{a[i][0]:<30}{a[i][1]:>17}', end='')  
    array_sorted = sorted(a, key=lambda lista:lista[1])
    line()
    print('Lista ordenada por idade: ')
    for i in range(len(array_sorted)):
        print(f'{array_sorted[i][0]:<30}{array_sorted[i][1]:>17}', end='')
    line()
    return


#main
read_file()
princ = read_array()
sort_and_print(princ)