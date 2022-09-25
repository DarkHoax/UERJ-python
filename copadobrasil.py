from random import choice

estadios = ['Maracanã','Mané Garrincha', 'Morumbi','Mineirão','Arena do Grêmio', 'Castelão','Beira-Rio', 'Arena Fonte Nova','Neo Química Arena','Engenhão','Arena Pernambuco','Mangueirão', 'Arena da Amazônia','Allianz Parque','Arena da Baixada','Arena Pantanal','Governador João Castelo','Pacaembu','Arena das Dunas']

temporada = 2022

while temporada < 2033:
	final = choice(estadios)
	print('\nEm',temporada,'a final da Copa do Brasil será no estádio',final,'\n')
	temporada += 1