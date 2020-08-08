#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Created on Wed Mar 25 18:15:28 2020

∆ 1.12.3. A conversão de graus Farenheit para centígrados é obtida por 
(C × 9/5) + 32. Fazer um algoritmo que calcule e escreva uma tabela de 
centígrados em função de graus Farenheit, que variam de 50 a 150 de 1 em 1.
@author: argos'''
celsius = 49
for i in range(celsius, 151):
    f = (celsius * 9/5) + 32
    celsius += 1
    print('{:<.2f}°C = {:<.2f}°F'.format(celsius, f))
