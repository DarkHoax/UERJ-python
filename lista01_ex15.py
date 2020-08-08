#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Created on Fri Jan 10 19:26:47 2020

lista 01 - QUESTÃO 15. Num frigorífico existem 90 bois. Cada boi traz preso em 
seu pescoço um cartão contendo seu número de identificação e seu peso. Crie um 
algoritmo que escreva o número e peso do boi mais gordo e do boi mais magro.
Além disso, responda: se houver dois ou mais bois com o mesmo peso, maior que
todos os demais, este algoritmo escreverá o número de qual deles?
@author: argos'''

boi_gordo = boi_magro = 0

for i in range(0, 91):
    identificacao = int(input('Digite o id do boi: '))
    peso = int(input('Peso do boi: '))
    if peso > boi_gordo:
        boi_gordo = peso
        for pesos in peso:
            if peso[pesos] == peso:
                if identificacao[pesos] < identificacao:
                    print('Boi gordo é {} com {:<.2f} kg'.format(identificacao[pesos], boi_gordo))
    elif boi_magro < peso:
        boi_magro = peso
        for pesos in peso:
            if peso[pesos] == peso:
                if identificacao[pesos] < identificacao:
                    print('Boi magro é {} com {:<.2f} kg'.format(identificacao[pesos], boi_magro))