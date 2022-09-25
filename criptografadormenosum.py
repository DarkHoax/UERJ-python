def Criptografa():
	frase = input('Digite uma frase: ')
	return frase

def Traduzir(frase):
	novo = ''
	for i in frase:
		novo += chr(ord(i)+3)
	return novo
	
def Impr(frase, novo):
	print(f'\nFrase: {frase}')
	print(f'\nCripto: {novo}')
	return
	
frase = Criptografa()
novo = Traduzir(frase)
Impr(frase, novo)