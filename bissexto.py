ano = 1
bissexto = 0
for i in range(ano, 2023):
	if i % 4 == 0:
		bissexto += 1
		print(f'\t{i} é bissexto\n')

print(f"\tDe ano 1 até 2022 houveram {bissexto} anos bissextos")
		