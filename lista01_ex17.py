#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 18:03:10 2020

    17. Uma certa firma fez uma pesquisa para saber se as pessoas gostaram ou não de um
    novo produto lançado no mercado. Para isso, forneceu o sexo do entrevistado e sua
    resposta (sim ou não). Sabendo-se que foram entrevistadas 2.000 pessoas, crie um
    algoritmo que calcule e escreva:
        
        a) o número de pessoas que responderam sim;

        b) o número de pessoas que responderam não; a porcentagem de pessoas do
        sexo masculino que responderam não.

@author: argos
"""

sim = nao = media = homem = 0
while True:
    sexo = input('Sexo, [M ou F]: ').upper()
    if sexo == '': break
    resposta = input('[S]im ou [N]ão: ').upper()
    
    if resposta == 'S':
        sim += 1
    elif resposta == 'N':
        nao += 1
    if sexo == 'M':
        homem += 1
        if resposta == 'N':
            media += (homem/nao)
print('Houveram {} sim e {} não, a porcentagem de homens que disseram não foi de {:<.2f}%'.format(sim, nao, media))
