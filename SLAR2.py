mpf = mpc = 0
v = e = d = overall = 0
l = ['s', 'n']

from random import choice

for i in range(1, 11):
	pf = int(input(f'\n\tDigite quantos pontos fez na rodada {i}: '))
	pc = int(input(f'\tDigite quantos pontos sofreu na rodada {i}: '))

	if pf > pc:
		v += 1
	elif pf == pc:
		e += 1
	else:
		d += 1
		
	mpf += pf // 10
	mpc += pc // 10
	
	
if e >= 1:
	overall += (v + (e * 0.5))/10
	pontos = ((v * 4) + (e * 2))
	
	print(f'\n\tSeu placar médio durante os 10 jogos é {mpf} - {mpc}\n\tDiferença de {abs(mpf - mpc)} pontos médios')
	
	print(f'\n\tPontos: {pontos} = Overall: {overall:3f}')
	
	print(f'\n\tV = [{v}] | D = [{d}] | E = [{e}]')
	
	print(f'\n\tRATIO PONTOS -> 1 PONTO(S) SOFRIDOS A CADA {pc/pf:.2f} PONTO(S) FEITOs')

else:
	overall += (v + (e * 0.5))/10
	pontos = ((v * 4) + (e * 2))
	
	print(f'\n\tSeu placar médio durante os 10 jogos é {mpf} - {mpc}\n\tDiferença de {abs(mpf - mpc)} pontos médios')
	
	print(f'\n\tPontos: {pontos} = Overall: {overall:3f}')
	
	print(f'\n\tV = [{v}] | D = [{d}] | E = [{e}]')
	
	print(f'\n\tRATIO PONTOS -> 1 PONTO(S) SOFRIDOS A CADA {pf/pc:.2f} PONTO(S) FEITOs')
	
	