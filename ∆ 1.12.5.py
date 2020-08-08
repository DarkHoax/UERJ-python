#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Created on Wed Mar 25 18:44:09 2020

∆ 1.12.5. Supondo que a população de um país A seja da ordem de 90.000.000 de 
habitantes com uma taxa anual de crescimento de 3% e que a população de um país 
B seja, aproximadamente, de 200.000.000 de habitantes com uma taxa anual de 
crescimento de 1,5%, fazer um algoritmo que calcule e escreva o número de anos 
necessários para que a população do país A ultrapasse ou iguale a população do 
país B, mantidas essas taxas de crescimento.
@author: argos'''
a = 90000000
b = 200000000
cont = 0
while b > a:
    a += (a * 0.03)
    b += (b * 0.015)
    cont += 1
    if a > b:
        print('A ultrapassou B em {} ano(s)'.format(cont))
        print('População de A {} pessoas\nPopulação de B {} pessoas'.format(a, b))
    elif a == b:
        print('A igualou B em {} ano(s)'.format(cont))
        print('População de A {:<.1f} pessoas\nPopulação de B {:<.1f} pessoas'.format(a, b))