#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Created on Mon Mar 16 18:16:08 2020

∆ 1.12.1. Fazer um algoritmo que:

- Leia um número indeterminado de linhas contendo cada uma a idade de um indivíduo.
A última linha que não entrará nos cálculos, contém o valor da idade igual a zero.

- Calcule e escreva a idade média deste grupo de indivíduos.

@author: argos'''

cont = media = idades = 0
while True:
    idade = int(input('Idade: '))
    cont += 1
    if idade < 0: break
    idades += idade
    media = (idades/cont)
print('O grupo tem a idade de {:<.1f} anos'.format(media))
