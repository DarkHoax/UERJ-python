from random import choice

times = ['América Mineiro', 'Atletico Mineiro', 'Atletico Goianiense', 'Atletico Paranaense', 'Bahia', 'Ceará', 'Chapecoense', 'Corithians', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras', 'Bragantino', 'Santos', 'São Paulo', 'Sport']

timesb = ['América Mineiro', 'Atletico Mineiro', 'Atletico Goianiense', 'Atletico Paranaense', 'Bahia', 'Ceará', 'Chapecoense', 'Corithians', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras', 'Bragantino', 'Santos', 'São Paulo', 'Sport']

a = b = 0

for r in range(1, 20):
	print(f'RODADA {r}\n')

	for i in times:
		i = choice(times)
		a += 1
	
		for j in timesb:
			j = choice(timesb)
			b += 1
	if i == j:
		for i in times:
			i = choice(times)
			times.remove(i)
			a += 1
	
			for j in timesb:
				j = choice(timesb)
				timesb.remove(j)
				b += 1
	else:
		print(f'{i} - {j}\n')
r += 1