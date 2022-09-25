from random import choice

estadios = ['AT&T Stadium', 'SoFi Stadium', 'Hard Rock Stadium', 'Caesars Superdome', 'Mercedes-Benz Stadium', 'Allegiant Stadium', 'NRG Stadium', 'Levis Stadium', 'TIAA Bank Field', 'Raymond James Stadium', 'State Farm Stadium', 'U.S. Bank Field', 'Lucas Oil Stadium']

temporada = 2022

while temporada < 2030:
	final = choice(estadios)
	print('\nNa temporada de',temporada,'o Super Bowl será no',final,'\n')
	temporada += 1