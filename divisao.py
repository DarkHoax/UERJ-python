while True:
	try:
		a = float(input("Entre com um valor: "))
		b = float(input("Entre com outro valor: "))
		c = a/b
		print(f'\n\t{c:.2f}')
		break
	except ZeroDivisionError:
		print("Erro de divisão")
	except ValueError:
		print("String")