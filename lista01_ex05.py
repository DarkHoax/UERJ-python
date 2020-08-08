#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:56:45 2020

5. Crie um algoritmo que imprima o peso total que será carregado por um 
caminhão. Sabe-se que este caminhão carrega 25 caixas. O peso de cada caixa 
deve ser informado pelo usuário.

@author: argos
"""
caixas = total = 0
while caixas < 25:
    peso = float(input('Digite o peso da caixa: '))
    caixas += 1
    print('Caixa {} pesa {:<.2f} kg'.format(caixas, peso))