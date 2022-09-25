from random import randint

i = idade = media = soma = 0
while i < 5:
	idade = randint(18, 64)
	print(f"\n\tIdades:\n\t{idade}\n")
	soma += idade
	i += 1

media = (soma // 5)
print(f"\tMédia de {media} anos")
	
	