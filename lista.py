def imprimir(n):
	for i in range(1, n + 1):
		for j in range(1, i + 1):
			print(i, end=' ')
		print()
#Main
n = int(input('Entre com um inteiro: '))
imprimir(n)