#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 14:13:19 2019
2. Crie um algoritmo que escreva os N primeiros termos de uma progressão aritmética
(PA). O primeiro termo e a razão da PA devem ser informados pelo usuário.
@author: argos

Digamos que eu escolha n = 1000, então eu teria que fazer uma PA que regredisse de 1000
até o termo a0"""
cont = an = a = r = 0
n = int(input('Digite um número: '))
r = float(input('Digite a razão da PA: '))
for i in range(0, n):
    an = a * (n - 1) * r
    n -= r
    print(an[i])