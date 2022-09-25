mc = mf = mediac = mediaf = 0

v = d = e = overall = 0
for i in range(1, 18):
	c = int(input(f'\n\tDigite o seu placar da rodada {i}: '))
	mc += c
	f = int(input(f'\tDigite o placar adversário da rodada {i}: '))
	mf += f
	
	if c > f:
		v += 1
	elif f > c:
		d += 1
	else:
		e += 1
	
	mediac = mc // 17
	mediaf = mf // 17
	
if e >= 1:
	overall += (v + (e * 0.5))/17	
	print(f'\n\tSeu placar é {mediac} a {mediaf}')
	print(f'\n\tV = [{v}] | D = [{d}] | E = [{e}]')
	print(f'\n\tAVG: {overall:.3f}')
else:
	overall += v/17
	print(f'\n\tSeu placar é {mediac} a {mediaf}')
	print(f'\n\tV = [{v}] | D = [{d}] | E = [{e}]')
	print(f'\n\tAVG: {overall:.3f}')
