mc = mf = mediac = mediaf = 0

v = d = e = overall = 0
for i in range(1, 14):
	gc = int(input(f'\nDigite o seu placar da rodada {i}: '))
	mc += gc
	gf = int(input(f'Digite o placar adversário da rodada {i}: '))
	mf += gf
	
	if gc > gf:
		v += 1
	elif gf > gc:
		d += 1
	else:
		e += 1
	
	mediac = mc // 13
	mediaf = mf // 13
	
if e >= 1:
	overall += v/13
	gp = mc/13
	ga = mf/13
	
	print(f'\n\tSeu placar é {mediac} a {mediaf}')
	
	print(f'\n\tV = [{v}] | D = [{d}] | E = [{e}]')
	
	print(f'\n\tGOLS A FAVOR: [{mc:.2f}]\n\tGOLS CONTRA: [{mf:.2f}]')
	
	print(f'\n\tRATIO GOLS -> 1 GOL(S) SOFRIDOS A CADA {mc/mf:.2f} GOL(S) FEITO')
	
	print(f'\n\tMédia de gols por jogos: {gp:.2f} gols\n\tMédia de gols sofridos por jogos: {ga:.2f} gols')
	
	print(f'\n\tAVG: {overall:.3f}')

else:
	overall += v/13
	gp = mc/13
	ga = mf/13
	
	print(f'\n\tSeu placar é {mediac} a {mediaf}')
	
	print(f'\n\tV = [{v}] | D = [{d}] | E = [{e}]')
	
	print(f'\n\tGOLS A FAVOR: [{mc:.2f}]\n\tGOLS CONTRA: [{mf:.2f}]')
	
	print(f'\n\tRATIO GOLS -> 1 GOL(S) SOFRIDOS A CADA {mc/mf:.2f} GOL(S) FEITO')
	
	print(f'\n\tMédia de gols por jogos: {gp:.2f} gols\n\tMédia de gols sofridos por jogos: {ga:.2f} gols')
	
	print(f'\n\tAVG: {overall:.3f}')
