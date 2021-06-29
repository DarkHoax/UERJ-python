#Argos Antao Maia - Matricula: 201910054111
'''Ler para uma lista o nome,idade e sexo de um grupo indeterminado de pessoas.

As informações lidas devem ser validadas da seguinte forma:

nome: máximo 30 caracteres - se for maior pedir para abreviar o nome
Idade: entre 18 e 80 anos - pedir para re digitar
sexo: m-masculino f-feminino ou o- não declarado - pedir para re digitar
Vc deverá usar o comando try para validar as informações.
Usando bubble sort classificar em ordem ascendente (de a-z) por nome.

Exibir a lista com todos os campos na ordem lida e depois ordenada.

Ponto extra: O aluno que usar selection sort,  insertion sort ou shell sort corretamente irá ganhar 0,5 pontos extra.

Atenção: não pode usar sort() ou sorted()'''

def Ler():
    h = m = o = 0
    lista = []
    princ = []
    #Categoriza o nome
    while True:
            lista.append(input('Digite um nome: ').strip().upper())
            if len(lista[0]) > 30: raise
            if lista[0] == 'PARE': break
            try:
                lista.append(Idade())
                lista.append(Sexo())
            except Exception:
                print('Abrevie o nome. Por favor digite novamente...')

    princ.append(lista[:])
    print('Lista original: {}'.format(princ))
    lista.clear()
    return princ

def Idade():
#Categoriza idade
    try:
        idade = int(input('Digite uma idade: '))
        if idade < 18 or idade > 80: raise
    except ValueError:
        print('Houve um erro na idade. Por favor digite novamente...')
    return idade

def Sexo():
    #Categoriza o sexo
    try:
        sexo = input('Digite um sexo [M ,F, O]: ').strip().upper()
        if sexo in 'M' or sexo in 'F' or sexo in 'O': return sexo
        else: raise
            
    except Exception:
        print('Erro. Por favor digite novamente...')
    



def Bubble(princ):
    #Ordena
    p = lambda princ: princ[0]
    elementos = len(p)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if p[i] > p[i+1]:
                p[i], p[i+1] = p[i+1], p[i]
                ordenado = False        
    return p

def Impr(princ):
    print('Lista Ordenada: {}'.format(princ))
    return


while True:
    princ = Ler()
    idade = Idade()
    sexo = Sexo()

p = Bubble(princ)
Impr(princ)