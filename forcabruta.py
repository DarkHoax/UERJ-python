import string
from random import choice
import time

senha = ''
n = 0
while n < 8:
	for i in range(8):
		values = string.ascii_letters + string.digits + string.punctuation
		senha += choice(values)
	print('\nEsta é a senha: {}\n'.format(senha))
	n += 1