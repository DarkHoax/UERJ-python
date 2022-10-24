from random import choice

nome = ['Nem', 'Bem-Te-Vi', 'Bochecha', 'Trajado', 'Trakinas', 'Chacrinha', 'Messi Careca','Tevez', 'Índio', 'Russinho', 'Milho', 'Alemão', 'Coroinha', 'Jesus', 'Vozão']

locais = ['do Rodo', 'da Providência', 'do 18', 'de Santa Cruz', 'da Vila da Penha', 'da Pavuna', 'do Vintém', 'da Rocinha', 'da CDD', 'do Tanque', 'de Manguinhos']

for i in nome:
	nomes = choice(nome)
	adj = choice(locais)
	print(nomes,adj)
