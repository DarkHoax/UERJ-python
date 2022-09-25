n = 360
c = p = 0
for i in range(1, n + 1):
	if n % i == 0:
		c += 1
		if i % 2 == 0:
			p += 1
			print(i)
print(f'Possui {c} divisores e {p} deles são pares')