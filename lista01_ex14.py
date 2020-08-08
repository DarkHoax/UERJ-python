#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Created on Wed Jan  8 00:29:53 2020
lista 01 - QUESTÃO 14. Crie um algoritmo que:
    a) Leia a idade de N pessoas.
    b) Calcule e mostre a idade média desse grupo de indivíduos. Escreva também 
    a porcentagem de pessoas entre 21 e 65 anos inclusive.
@author: argos'''
media = cont = porcent = workable = soma = 0
while(True):
    idade = int(input('Idade: '))
    soma += idade
    cont += 1
    if idade < 0: break

    if idade >= 21 and idade <= 65:
        workable += 1
        porcent = (workable/cont) * 100
    media = (soma/cont)
print('MÉDIA DE IDADES: {:<.2f}\nPORCENTAGEM DE PESSOAS ENTRE 21~65 ANOS: {:<.2f}'.format(media, porcent))