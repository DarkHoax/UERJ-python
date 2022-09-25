def Linha():
	print('='*30)
	
import time

n = int(input('Digite um n°: '))

Linha()

print('\nAlgoritmo 1\n')
i1 = time.time()
r1 = 0

while ((r1+1)**2) <= n:
	r1 += 1
f1 = time.time()
print(r1,'\ntempo: {:.2f}'.format(f1-i1))

Linha()

print('\Algoritmo 2\n')
