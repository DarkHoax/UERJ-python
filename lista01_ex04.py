#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 01:33:58 2020

4. Crie um algoritmo que leia os nomes e os preços dos produtos de uma loja e escreva
o nome do produto mais caro. Considere que a lista tem N produtos e que não existem
preços repetidos.
@author: argos"""
maiorpreco = 0
while True:
    nome = input('Digite um nome: ').lower()
    if nome == '': break
    preco = float(input('Digite o preço: '))
    
    if preco > maiorpreco:
        maiorpreco = preco

    print('{} = R$ {:<.2f} tem o maior preço'.format(nome, preco))