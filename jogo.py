from random import randint as rt

sorteio = rt(0,9)

while chance == 'S':
	n = int(input('Digite um numero: '))
	if n == sorteio:
		print(f'Parabens seu imbecil, tu digitou {n} e a resposta é {sorteio}')
		chance = input('Quer continuar? [S/N]: ').strip().upper()