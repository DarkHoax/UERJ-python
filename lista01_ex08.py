#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 20:11:02 2020

lista 01 - QUESTÃO 08. Crie um algoritmo que leia 2 números inteiros positivos, 
A e B, e que calcule a soma de todos os números múltiplos de 4 compreendidos 
entre eles. Os valores A e B não devem ser considerados no somatório. 
Caso A seja maior do que B deve ser enviada uma mensagem para o usuário 
informando que a soma não será realizada.
@author: argos"""
soma = 0
a = int(input('Digite A: '))
b = int(input('Digite B: '))
if a > b:
    print('Erro')
    raise(SystemExit)
else:
    aux_1 = a + 1
    aux_2 = b - 1
    while aux_1 <= aux_2:
        if aux_1 % 4 == 0:
            soma += aux_1
        aux_1 += 1
    if aux_1 == b:
        print(soma)