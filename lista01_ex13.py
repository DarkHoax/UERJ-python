#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 00:13:16 2020

lista 01 - QUESTÃO 13. Crie um algoritmo para calcular a área de um triângulo 
qualquer, considerando que são fornecidos os comprimentos dos seus lados. 
Esse programa não pode permitir a entrada de dados inválidos, ou seja, medidas 
menores ou iguais a 0.
@author: argos
"""

a = float(input('Digite um valor para A: '))
b = float(input('Digite um valor para B: '))
c = float(input('Digite um valor para C: '))
try:
    try:
        if a > b == c or a == b > c:
            print('É TRIANGULO')
        if a == b == c:
             print('É EQUILATERO')
        elif a == b != c or a != b == c or a == c != b:
            print('É ISÓSCELES')
        else:
            print('É ESCALENO')
    except:
        print('NÃO É TRIÂNGULO')
except:
    if a <= 0 or b <= 0 or c <= 0:
        print('ERRO, VÁRIAVEL MENOR OU IGUAL A ZERO')