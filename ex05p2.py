i = j = 0
nome = input('Digite um nome: ')
if len(nome) < 4:
    print('Desculpe. Nome menor que 3 caracteres, nao sera possivel continuar.')

idade = int(input('Digite a idade: '))
if idade < 0 or idade > 150:
    print('Nao sera possivel. Pois a idade eh negativa ou maior que 150 anos')

sexo = input('Digite sexo: ').upper()
if sexo == 'M' or sexo == 'F':
    i += 1
else:
    print('Sexo nao listado')

civil = input('Digite um estado civil: ')
if civil == 'S' or civil == 'C' or civil == 'V' or civil == 'D':
    j += 1
else:
    print('Estado civil nao listado')
print('{} tem {} anos eh do sexo {} e o estado civil eh {}'.format(nome, idade, sexo, civil))