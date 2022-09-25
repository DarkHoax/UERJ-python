from random import choice

estadios = ['Estádio do Maracanã', 'Estádio Nilton Santos','Estádio de São Januário','Estádio Raulino de Oliveira','Estádio Cláudio Moacyr de Azevedo','Estádio Edson Passos','Estádio Antonio Gomes Viana','Arena Guanabara','Estádio Odair Gama','Estádio da Rua Bariri']

temporada = 2022

while temporada < 2029:
	final = choice(estadios)
	print('\nNa temporada de',temporada,'a final será no estádio\n',final)
	temporada += 1