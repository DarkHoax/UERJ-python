def checa(list):
	elem = list[0]
	for a in list:
		if a > elem:
			elem = a
	return elem
print(checa([4, 4, 8, -3]))