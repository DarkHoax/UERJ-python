#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:27:50 2020

18. Crie um algoritmo que leia um número N e verifique se ele é primo.

@author: argos"""

numero = int(input('Digite um número: '))
primo = True
if numero > 2 and numero % 2 == 0:
    primo = False
else:
    divisor = 3
    metade = numero / 2
    while divisor < metade:
        if numero % divisor == 0:
            primo = False
            break
        divisor += 2
if primo:
    print('É primo')
else:
    print('Não é primo')