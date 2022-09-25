from random import choice
def line():
	print('='*31)

programmers = ['Argos A. Maia', 'Leo', 'Julia', 'Jonathan', 'Lucca', 'Matheus', 'Lucas Couto', 'Jonas', 'R. Barroso', 'R. Kauer', ]

potb = ['Tolima', 'Talleres', 'Athl. Paranense', 'Fortaleza', 'Corinthians', 'Emelec', 'Veléz', 'Cerro']

i = j = 0 
'''
i = representa o índice dos times primeiros colocados
j = representa o índice dos times primeiros colocados
'''
line()
print('='*5,'SORTEIO DAS OITAVAS','='*5)
line()
while i < 8:
	timea = choice(pota)
	timeb = choice(potb)
	i += 1
	pota.remove(timea)
	potb.remove(timeb)
	while i > j:
		print(f'\n\tJOGO {i}')
		print(f'\n\t{timea} vs {timeb}')
		j += 1