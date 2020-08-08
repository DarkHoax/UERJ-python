#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Created on Mon Mar 16 20:44:22 2020

∆ 1.12.2. Tem-se um conjunto de dados contendo a altura e o sexo (masculino, feminino) 
de 50 pessoas. Fazer um algoritmo que calcule e escreva:
- a maior e a menor altura do grupo;
- a média de altura das mulheres;
- o número de homens;

@author: argos'''

maior = menor = media = homem = i = alturas = cont = 0
while i < 5:
    altura = int(input('Digite a altura: '))
    sexo = input('SEXO [M OU F]: ').upper()
    i += 1
    
    if altura > maior:
        maior = altura
    elif menor < altura:
        menor = altura
    if sexo == 'F':
        cont += 1
        alturas += altura
        media = (alturas/cont)
    elif sexo == 'M':
        homem += (i - cont)
print('Maior altura {} cm\nMenor altura {} cm\nMédia de altura feminina {:<.2f} cm\nTem {} homens'.format(maior, menor, media, homem))
