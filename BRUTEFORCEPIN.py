from random import choice

def Ler():
	with open('numeros.txt', 'w+') as file:
		for i in range(1000, 10000):
			file.write(str(i)+'\n')
	return
	
def Copia():
		lista = []
		with open('numeros.txt', 'r') as file:
			senha = file.readlines()
			lista.append(senha)
		return lista

def Impr(lista):
	for i in lista:
		valor = choice(i)
		print(f'O PIN gerado: {valor}')
	return

Ler()
lista = Copia()
Impr(lista)