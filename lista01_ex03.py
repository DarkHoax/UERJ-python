#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 22:57:09 2020

lista 01 - QUESTÃO 03. Crie um algoritmo que leia uma quantidade de N números 
inteiros calcule e escreva quantidade de números pares e ímpares e a média 
aritmética dos números pares.
@author: argos """

par = impar = cont = media = 0
while True:
    n = int(input('Digite um número: '))
    cont += 1
    if n < 0: break
    if n % 2 == 0:
        par += 1
        media += cont/n
    else:
        impar += 1
    print('Tem {} pares e a média aritmética é {:<.2f}'.format(par, media))
    print('Tem {} impares'.format(impar))