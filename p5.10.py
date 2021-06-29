'''
Elabore um programa Python que grave em dois arquivos listas alfa-numéricas. Calcular e 
exibir a intercalação dos dois arquivos. Por exemplo, arquivo1=['a','b','c','d'] e arquivo2= 
[10,20,30,40] resultará em ['a',10,'b',20,'c',30,'d',40]. 
'''
def line():
    print('*'*70)


def read_files():
    while True:
        try:
            size = int(input('Tamanho dos arquivos: '))
            if size <= 0: raise
            break
        except: print('Erro, digite um número: ')
    with open('info10.1.txt', 'w+') as file:
        print('Arquivo 1: ')
        for i in range(size):
            while True:
                    try:
                        a = input('Elemento: ')
                        file.write(a+'\n')
                        break
                    except: print('Erro, tente novamente: ')
        line()
    print('Arquivo 2:')
    with open('info10.2.txt', 'w+') as fileV2:
        for i in range(size):
         while True:
                try:
                    b = input('Elemento: ') 
                    fileV2.write(b+'\n')
                    break
                except: print('Erro, tente novamente: ')
    return size


def read_array():
    array1 = []
    array2 = []
    final_array = []
    with open('info10.1.txt', 'r') as file:
        list_of_elements = file.readlines()
        for element in list_of_elements:
            array1.append(element.strip('\n'))
    with open('info10.2.txt', 'r') as file2:
        list_of_elements2 = file2.readlines()
        for element in list_of_elements2:
            array2.append(element.strip('\n'))
    for i in range(size):
        final_array.append(array1[i])
        final_array.append(array2[i])
    return array1,array2,final_array


def result(a,b,c):
    line()
    print(f' Arquivo 1: {a}')
    line()
    print(f'Arquivo 2: {b}')
    line()
    print(f'Arquivo resultado: {c}')


#main
size = read_files()
array1,array2,final_array = read_array()
result(array1,array2,final_array)

