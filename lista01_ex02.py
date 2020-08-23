'''
2. Crie um algoritmo que escreva os N primeiros termos de uma progressão aritmética
(PA). 
O primeiro termo e a razão da PA devem ser informados pelo usuário.

'''

print('GERADOR DE PA')
print('='*15)

n = int(input('Digite n-termos: '))
p_termo = float(input('Digite o primeiro termo: '))
razao = float(input('Digite a razao da PA: '))
termo = p_termo
cont = 1

while cont < n:
    print('{:<.1f} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
