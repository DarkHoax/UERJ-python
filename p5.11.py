'''
Elabore um programa Python que grave em um arquivo uma sequencia numérica. Crie uma 
função que leia os dados gravados e determine o tamanho t da maior sequencia de números 
iguais. Exemplo: Supor que sejam armazenados os seguintes valores: [1,1,6,6,7,7,7,7,1,1,1], 
então t=4. 
'''
def line():
    print('*'*70)


def read_file():
    with open('info11.txt', 'w+') as file:
        while True:
            try:
                n = input('Número: ')
                if n == '': break
                test = float(n)
                file.write(n+'\n')
            except: print('Erro, digite um número: ')
    return 


def read_array():
    with open('info11.txt', 'r') as file:
        array = []
        list_of_numbers = file.readlines()
        for number in list_of_numbers:
            array.append(number)
    return array


def check(a):
    counter = 0
    element = a[0]
    for i in range(len(a)):
        if element != a[i]:
            element = a[i]
        else:
            counter += 1
    line()
    print(f'A maior sequência de números repetidos é {counter}')
    line()
    return 


#main
read_file()
array = read_array()
check(array)                  

