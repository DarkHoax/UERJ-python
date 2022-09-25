''' calculadora de bilionário'''
rico = 0

sal = float(input('Digite seu salário líquido [livre de impostos]: '))

des = float(input('Digite suas despesas: '))

sobrou = sal - des 

print(f'\nSeu salário: R$ {sal:.2f}\nSuas depesas: R${des:.2f}\nSobrou: R${sobrou:.2f}')

inv = input('\nVocê investe? [S/N]: ').upper()

if inv == 'N':
	rico += sobrou
	ano += 1
	if rico >= 1000000000:
		print('Você ficaria bilionário em {ano} anos e teria R${rico:.2f}')