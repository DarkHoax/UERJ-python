from random import choice

estadios = ['AT&T Stadium', 'SoFi Stadium', 'Hard Rock Stadium', 'Mercedes-Benz Superdome', 'Mercedes-Benz Stadium', 'Allegiant Stadium', 'NRG Stadium', 'Levis Stadium', 'TIAA Bank Field', 'Raymond James Stadium', 'State Farm Stadium']

temporada = 2022
i = 0
while temporada < 2030:
	final = choice(estadios)
	
	for i in temporada:
		if final[i] == final[i - 1]:
			final = choice(estadios)
			
	print('\nNa temporada de',temporada,'o Super Bowl será no',final,'\n')
	temporada += 1