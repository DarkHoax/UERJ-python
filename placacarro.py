import string
from random import choice

letras = ""
codigo = ""
num = 0
for i in range(3):
	letras += string.ascii_letters
	codigo += choice(letras)

for i in range(4):
	num += string.digits
	num = str(num)
	nums_cod += choice(num)
	
	codigo = codigo.upper() + str(num_cod)

print(codigo)