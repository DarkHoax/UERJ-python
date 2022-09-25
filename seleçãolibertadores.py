from random import choice
def line():
	print('='*31)

pota = ['Palmeiras', 'River Plate', 'Flamengo', 'Estudiantes', 'Atl. Mineiro', 'Colon', 'Libertad', 'Boca Jrs']

potb = ['Tolima', 'Talleres', 'Athl. Paranense', 'Fortaleza', 'Corinthians', 'Emelec', 'Veléz', 'Cerro']

i = j = 0 
'''
i = representa o índice dos times primeiros colocados
j = representa o índice dos times primeiros colocados
'''
line()
print('\n\tLISTA DOS PRIMEIROS COLOCADOS\n')
for posa, k in enumerate(pota):
	print(f'\t{posa+1} - {k}')
line()

line()
print('\n\tLISTA DOS SEGUNDOS COLOCADOS\n')
for posb, l in enumerate(potb):
	print(f'\t{posb+9} - {l}')
line()
print('\n')

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