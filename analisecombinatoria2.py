soma = 0
n = int(input('Digite um número: '))
for i in range(1, n + 1):
	soma += n ** i
	print(soma)
	if soma % i == 0:
		print(f'{soma} é múltiplo de {i}')