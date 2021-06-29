'''
Elabore um programa Python que grave em um arquivo uma quantidade indeterminada de 
dados numéricos reais. Depois leia os “n” primeiros valores e verifique a existência de 
elementos iguais a média, imprimindo a posição em cada elemento se encontra. Modularizar 
em pelo menos 3 funções.
'''
def line():
    print('='*86)


def read_file():
    with open('info8.txt', 'w+') as file:
        while True:
            try:
                n = input('Digite um número ou <enter> para encerrar: ')
                if n == '':break
                test = float(n)
                file.write(n+'\n')
            except: print('Erro, tente novamente: ')
    return


def read_list():
    total = media = cont = 0
    list_index = []
    with open('info8.txt', 'r') as file:
        list_numbers = file.readlines()
    for number in list_numbers:
        total += float(number)
    media = total/len(list_numbers)
    while True:
        try:
            n = int(input('Quantos valores serão lidos: '))
            if n <= 0 or n > len(list_numbers): raise
            line()
            print('Valores:')
            break
        except: print('Erro, tente novamente: ')
    for i in range(n):
        print(list_numbers[i], end='')
        if float(list_numbers[i]) >= media:
            cont += 1
            list_index.append(i)
    return list_index,cont



def result(a,b):
    line()
    print(f'Existem {b} elementos maiores ou iguais a média(nas n primeiras posições), posições: {a}')
    line()


#main
read_file()
list_index,cont = read_list()
result(list_index,cont)
        