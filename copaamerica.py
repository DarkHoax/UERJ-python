from random import choice

pota = ['Brazil', 'Argetina', 'Uruguai', 'Mexico']
potb = ['Colômbia', 'Chile', 'Estados Unidos', 'Costa Rica']
potc = ['Peru', 'Honduras', 'Equador', 'Paraguai']
potd = ['Venezuela', 'Bolívia', 'El Salvador', 'Panamá']

ga = []
gb = []
gc = []
gd = []
i = 0

while i < 8:
	timea = choice(pota)
	timeb = choice(potb)
	timec = choice(potc)
	timed = choice(potd)

	ga.append(timea)
	gb.append(timeb)
	gc.append(timec)
	gd.append(timed)
	
	i += 1
	pota.remove(timea)
	potb.remove(timeb)
	potc.remove(timec)
	potd.remove(timed)

print('\nGRUPO A\n')
for k in ga:
	print(k)

print('\nGRUPO B\n')
for l in gb:
	print(l)


print('\nGRUPO C\n')
for m in gc:
	print(m)

print('\nGRUPO D\n')
for n in gd:
	print(n)