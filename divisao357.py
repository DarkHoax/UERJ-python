
n = 3

print('POR 3 resto 2, 5 resto 3, 7 resto 4')
while n < 101:
	if n % 3 == 2:
		if n % 5 == 3:
			if n % 7 ==4:
				print(f'\t{n}')
	n += 1