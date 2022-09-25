from random import *
 
 cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
 
 print('Quer jogar?')
 resp = input('[S/N]: ').upper()
 
 if resp == 'N':
 	print('Adeus')
 if resp == 'S':
 	print('Sua carta é {}'.format(choice(cartas)))