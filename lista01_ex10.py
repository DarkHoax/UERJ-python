#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Created on Tue Jan  7 21:15:58 2020

lista 01 - QUESTÃO 10. Uma empresa lançou um novo produto no mercado e fez uma 
pesquisa para saber se os consumidores estavam satisfeitos, para isso eles 
deveriam responder sim ‘S’ ou não ‘N’. Crie um algoritmo que leia a resposta de 
todas as pessoas e escreva a porcentagem dos que disseram sim e dos que 
disseram não. Obs: O final da leitura de dados é marcado pela resposta ‘F’.

@author: argos'''

cont = sim = nao = porcentagem_sim = porcentagem_nao = 0
while True:
    resposta = input('Gostou do produto [S], [N]: [F para "sair"]: ').upper()
    cont += 1
    if resposta == 'F': break
    if resposta == 'S':
        sim += 1
        
    else:
        nao += 1
    porcentagem_sim = (sim/cont) * 100
    porcentagem_nao = (nao/cont) * 100
    
print('SIM: {:<.2f}%\nNÃO: {:<.2f}%'.format(porcentagem_sim, porcentagem_nao))