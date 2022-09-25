eur = 5.5307
usd = 5.0624
gbp = 6.6964


print('DESEJE A OPÇÃO: ')
print('\n1 - Passar R$ para alguma moeda estrangeira')
print('2 - Passar moeda estrangeira para R$')

while True:
	try:
		opcao = input('\nDigite uma opção [1 ou 2]: ').strip().lower()
		if opcao == '': raise Exception
		if opcao.isalpha(): raise Exception		
		break
	except Exception:
		print('Valor errado')

if opcao == '1':
	rs = float(input('Digite um valor R$'))
	print(f'\nR$ {rs:<.2f} -> ${rs/usd:<.2f}')
	print(f'R$ {rs:<.2f} -> €{rs/eur:<.2f}')
	print(f'R$ {rs:<.2f} -> £{rs/gbp:<.2f}')

elif opcao == '2':
	while True:
		try:
			moeda = input('Digite uma moeda [USD, GBP, EUR]: ').strip().lower()
			break
		except Exception:
			print('Moeda errada...')
	
	if moeda == 'usd':
		while True:
			try:
				nusd = float(input('Digite o valor do Dólar: '))
				break
				if nusd < 0: raise ValueError
			except ValueError:
				print('Valor incalculável')
				
		
		print(f'\n${nusd:<.2f} -> R${usd*nusd:<.2f}')

	elif moeda == 'eur':
		while True:
			try:
				neur = float(input('Digite o valor do Euro: '))
				break
				if neur < 0: raise ValueError
			except ValueError:
				print('Valor incalculável')
				
		
		print(f'\n€{neur:<.2f} -> R${eur*neur:<.2f}')

	elif moeda == 'gbp':
		while True:
			try:
				ngbp = float(input('Digite o valor da Libra: '))
				break
				if ngbp < 0: raise ValueError
			except ValueError:
				print('Valor incalculável')
		print(f'\n£{ngbp:<.2f} -> R${gbp*ngbp:<.2f}')
	else:
		print('Moeda não listada')

else:
	print('Opção inválida')
