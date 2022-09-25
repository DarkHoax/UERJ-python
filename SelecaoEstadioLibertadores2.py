from random import choice

paises = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for i in paises:
	pais = choice(paises)
	if pais == 1:
		print('A escolha do país é o Canada')
		estadios = ['Rogers Centre Stadium', 'BC Place Stadium', 'Canad Inns Stadium']
		for i in estadios:
			estadio = choice(estadios)
			print('A final da libertadores será em', estadio)
	if 