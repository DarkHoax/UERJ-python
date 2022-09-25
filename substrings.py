def prefixo(p1, p2):
	if len(p1) > len(p2):
		return False
	i = 0
	while i < len(p1):
		if p1[i] != p2[i]:
			return False
		i += 1
	return True

def ler():
	p1 = input('Digite a primeira frase: ').strip()
	p2 = input('Digite a segunda frase: ').strip()
	return p1, p2

p1, p2 = ler()
if prefixo(p1, p2):
	print('É substring')
else:
	print('Não é substring')