aulas = 41
media = 0

try:
	faltas = int(input('Digite quantas faltas: '))
	if faltas < 0: raise ValueError
except ValueError:
	print('Erro de digitação')
	
if faltas > aulas:
	print('Erro. Tem mais faltas que aulas')
else:
	media = (faltas/aulas) * 100
print(f'faltas em {media:<.2f}%\nPresença em {100-media:.2f}%')
	
