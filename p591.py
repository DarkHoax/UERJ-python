'''
Elabore um programa Python que grave em um arquivo um conjunto indeterminado de palavras
Leia as palavras deste arquivo e crie uma função que permita contar o número de ocorrências de uma 
expressão nas palavras. Exemplo: a expressão 'ana' está presente 4 vezes nas palavras 'banana, 
mariana, e diana'. 
'''
def line():
    print('*'*70)


def read_file():
    with open('info9.txt', 'w+') as file:
        while True:
            try:
                word = input('Palavra: ').upper().strip()
                if word == '': break
                elif word.isalpha():
                    file.write(word+'\n')
                else: raise
            except: print('Erro, digite uma palavra: ')
    return


def read_array():
    list_of_words = []
    with open('info9.txt', 'r') as file:
        list_words = file.readlines()
        for word in list_words:
            list_of_words.append(word.strip('\n'))
    print(list_of_words)
    print(list_of_words[0])
    return list_of_words

read_file()
list_of_words = read_array()