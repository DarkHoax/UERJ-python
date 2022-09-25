mpf = mpc = 0
v = e = d = 0
l = ['s', 'n']

from random import choice

for i in range(1, 11):
	pf = int(input(f'\nDigite quantos pontos fez na rodada {i}: '))
	pc = int(input(f'Digite quantos pontos sofreu na rodada {i}: '))

	if pf > pc:
		v += 1
	elif pf == pc:
		e += 1
	else:
		d += 1
		
	mpf += pf // 10
	mpc += pc // 10

print(f'\nSeu placar médio durante os 10 jogos é {mpf} - {mpc}\nDiferença de {abs(mpf - mpc)} pontos médios')


if v > e or v == e and v > d:
	print('\nAVANÇOU AOS PLAYOFFS\n')
	
	pff = int(input('\nDigite quantos pontos fez: '))
	pfc = int(input('Digite quantos pontos sofreu: '))

	if pff > pfc:
		v += 1
		print('\nFINAL DO CAMPEONATO\n')
			
		pfz = int(input('\nDigite quantos pontos fez: '))
		pfcz= int(input('Digite quantos pontos sofreu: '))
			
		if pfz > pfcz:
			v += 1
			print('\nVENCEU O CAMPEONATO\n')
			mpf += pfz // 12
			mpc += pfcz // 12	
			
			print(f'\nSeu placar médio é {mpf} - {mpc}\nDiferença de {abs(mpf - mpc)} pontos médios')

			print(f'\nTemporada encerrada na Final com:\n{v} Vitórias - {e} Empates - {d} Derrotas'')

			print('Estatistica de vitorias: {:.3f}'.format(v + (e * 0.5)/12))
				
		elif pfz == pfcz:
			es = choice(l)
				
			if es == 's':
				v += 1
				print('\nVENCEU O CAMPEONATO\n')
				mpf += pfz // 12
				mpc += pfcz // 12	
				
				print(f'\nSeu placar médio é {mpf} - {mpc}\nDiferença de {abs(mpf - mpc)} pontos médios')
	
				print(f'\nTemporada Encerrada na Final com:\n{v} Vitórias - {e} Empates - {d} Derrotas')
	
				print('Estatistica de vitorias: {:.3f}'.format(v + (e * 0.5)/12))
					
			else:
				d += 1
				print('\nPERDEU O CAMPEONATO\n')
				mpf += pfz // 12
				mpc += pfcz // 12	
				
				print(f'\nSeu placar médio é {mpf} - {mpc}\nDiferença de {abs(mpf - mpc)} pontos médios')
	
				print(f'\nTemporada Encerrada na Final com:\n{v} Vitórias - {e} Empates - {d} Derrotas')
	
				print(f'Estatistica de vitorias: {v + (e * 0.5)/12):.3f}
									
		else:
			d += 1
			print('\nPERDEU O CAMPEONATO\n')
			mpf += pfz // 12
			mpc += pfcz // 12	
			
			print(f'\nSeu placar médio é {mpf} - {mpc}\nDiferença de {abs(mpf - mpc)} pontos médios')

			print(f'\nTemporada Encerrada na semifinal com:\n{v} Vitórias - {e} Empates - {d} Derrotas')

			print('Estatistica de vitorias: {:.3f}'.format(v + (e * 0.5)/12))
			
	elif pff == pfc:
		se = choice(l)
		if se == 's':
			v += 1
			print('\nFINAL DO CAMPEONATO\n')
			
			pfz = int(input('\nDigite quantos pontos fez: '))
			pfcz= int(input('Digite quantos pontos sofreu: '))
			
			if pfz > pfcz:
				v += 1
				print('\nVENCEU O CAMPEONATO\n')
				mpf += pfz // 12
				mpc += pfcz // 12	
				
				print(f'\nSeu placar médio é {mpf} - {mpc}\nDiferença de {abs(mpf - mpc)} pontos médios')
	
				print(f'\nTemporada Encerrada com:\n{v} Vitórias - {e} Empates - {d} Derrotas')
	
				print('Estatistica de vitorias: {:.3f}'.format(v + (e * 0.5)/12))
					
			elif pfz == pfcz:
				es = choice(l)
				
				if es == 's':
					v += 1
					print('\nVENCEU O CAMPEONATO\n')
					mpf += pfz // 12
					mpc += pfcz // 12	
				
					print(f'\nSeu placar médio é {mpf} - {mpc}\nDiferença de {abs(mpf - mpc)} pontos médios')
	
					print(f'\nTemporada Encerrada com:\n{v} Vitórias - {e} Empates - {d} Derrotas')
	
					print('Estatistica de vitorias: {:.3f}'.format(v + (e * 0.5)/12))
					
				else:
					d += 1
					print('\nPERDEU O CAMPEONATO\n')
					mpf += pfz // 12
					mpc += pfcz // 12	
				
					print(f'\nSeu placar médio é {mpf} - {mpc}\nDiferença de {abs(mpf - mpc)} pontos médios')
	
					print(f'\nTemporada Encerrada na semifinal com:\n{v} Vitórias - {e} Empates - {d} Derrotas')
	
					print('Estatistica de vitorias: {:.3f}'.format(v + (e * 0.5)/12))
									
			else:
				d += 1
				print('\nPERDEU O CAMPEONATO\n')
				mpf += pfz // 12
				mpc += pfcz // 12	
			
				print(f'\nSeu placar médio é {mpf} - {mpc}\nDiferença de {abs(mpf - mpc)} pontos médios')

				print(f'\nTemporada Encerrada na final com:\n{v} Vitórias - {e} Empates - {d} Derrotas')

				print('Estatistica de vitorias: {:.3f}'.format(v + (e * 0.5)/12))
				
		else:
			d += 1
			print('PERDEU NA SEMIFINAL')
			mpf += pff // 11
			mpc += pfc // 11
				
			print(f'\nSeu placar médio é {mpf} - {mpc}\nDiferença de {abs(mpf - mpc)} pontos médios')

			print(f'\nTemporada Encerrada com:\n{v} Vitórias - {e} Empates - {d} Derrotas')

			print('Estatistica de vitorias: {:.3f}'.format(v + (e * 0.5)/11))
			
else:
	
	print(f'\nTemporada Encerrada com:\n{v} Vitórias - {e} Empates - {d} Derrotas')

	print('Estatistica de vitorias: {:.3f}'.format(v + (e * 0.5)/10))