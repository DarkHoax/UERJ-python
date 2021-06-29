'''Elabore um programa Python que grave em um arquivo um número indeterminado de nomes,
idades e sexo. Depois leia estes dados e determine os dados do homem mais jovem..'''

def Ler():
    with open('ex06p5.txt','w+') as file:
        
        while True:
            nome = input('Digite o nome: ')
            if nome == '': break
            
            while True:
                try:
                    sexo = input('Digite o sexo: ').strip().upper()
                    break
                except sexo != 'M' or sexo !='F':
                    print('Sexo nao validado')
            
            while True:
                try:
                    idade = int(input('Digite a idade: '))
                    break
                except ValueError:
                    print('Idade invalida')
        file.write(nome+' '+sexo+' '+str(nome))
    
    return

def Calculos(sexo, idade):
    k = None
    menor = 1000
    temp = []
    princ = []
    with open('ex06p5.txt', 'r') as file:
        for i in file:
            v = i.split(',')
            temp.append(v[0])
            temp.append(v[1])
            temp.append(v[2]).strip('\n')
            princ.append(temp[:])
            temp.clear()

    for i in range(len(princ)):
         if princ[i][2] == 'M' and int(princ[i][1]) < int(lower):
            k = i
            menor = princ[i][1]
    
    try:
        print('O nome do homem mais velho com {} anos é o --> {}'.format(lower, princ[index][0]))
    except:
        print('Dados insuficientes')
    return 

Ler()
Calculo()
