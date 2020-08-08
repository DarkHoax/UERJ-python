#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:55:20 2020

@author: argos
"""

primos = cont = 0

numero = int(input('Digite um número: '))
for i in range(1, numero + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            cont += 1
    if cont == 2:
        print(i)
    cont = 0