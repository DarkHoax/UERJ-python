from random import choice

def Stadiums():
	ano = 2021

	estadio = ['Estádio do Maracanã', 'Estádio Morumbi', 'Estádio Mineirão', 'Estádio do Engenhão', 'Estádio da Independência', 'Arena MRV', 'Allianz Arena', 'Neo-Química Arena']
	
	while ano < 2070:
		final = choice(estadio)
		print('\nNo ano',ano,'a final será no',final)
		ano += 1
	
	return ano, final
	
ano, final = Stadiums()