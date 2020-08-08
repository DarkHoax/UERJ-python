#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 17:32:19 2020

6. Crie um algoritmo que leia a quantidade e o preço de N produtos 
comprados por uma empresa. Ao final deve ser escrito o total gasto pela 
empresa.
@author: argos
"""

while True:
    preco = float(input('Digite o preço do produto: '))
    if preco < 0: break 