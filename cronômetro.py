from time import sleep
import os

os.system('clear')
h = m = s = 0
f = '00'
while True:
	if s < 60:
		if s < 10:
			print(f'{h}:{m}:0{s}')
			sleep(1)
			os.system('clear')
		else:
			print(f'{h}:{m}:{s}')
			sleep(1)
			os.system('clear')
		s += 1
	if s == 60:
		s = 0
		m += 1
	if m == 60:
		m = 0
		h += 1
		
		