import string
from random import choice
import time

senha = ''

try:
	n = int(input('\tDigite o comprimento da senha: '))
	
except n < 5:
	print('Senha curta ou fraca')

i = time.time()
for i in range(n):
	values = string.ascii_letters + string.digits + string.punctuation
	senha += choice(values)
f = time.time()
	
tempo = ((f-i)//3600000)
print('\n\tEsta é a senha: {}'.format(senha))
print('\nTempo: {:.0f} horas à ser quebrada'.format((tempo)))
