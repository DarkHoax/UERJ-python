def ler():
	a = float(input('Digite um valor: '))
	b = float(input('Digite outro valor: '))
	return a, b

def calc(a, b):
	media = (a+b)/2
	return media
	
def impr(media, a, b):
	print(f'A média de {a:.0f} e {b:.0f} é {media:.1f}')
	return

a, b = ler()
media = calc(a, b)
impr(media, a, b)