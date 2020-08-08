#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Created on Wed Jan  8 00:03:06 2020

lista 01 - QUESTÃO 11. Crie um algoritmo que calcule a soma dos N primeiros 
números inteiros ímpares e positivos. O valor de N deve ser lido do usuário.

@author: argos'''
soma = 0
n = int(input('Digite um número: '))
for i in range(0, n + 1):
    if i > 0:
        if i % 2 == 1:
            soma += i
print('{:<.2f}'.format(soma))