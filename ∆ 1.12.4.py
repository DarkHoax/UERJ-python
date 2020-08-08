#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Created on Mon Mar 16 22:06:12 2020

∆ 1.12.4. Um comerciante deseja fazer o levantamento do lucro das mercadorias que ele
comercializa. Para isto, mandou digitar uma linha para cada mercadoria com nome, preço de
compra e preço de venda das mesmas. Fazer um algoritmo que determine e escreva 
quantas mercadorias proporcionam:
    
    lucro < 10%
    10% ≤ lucro ≤ 20%
    lucro > 20%
    determine e escreva o valor total de compra e de venda de todas as mercadorias, 
    assim como o lucro total.

Observação: o aluno deve adotar um flag.

@author: argos'''
cont = lucro = dezpercent = vintedezpercent = vintepercent = compras = vendas = 0

while True:
    cont += 1
    nome = input('Digite o nome do produto: ')
    if nome =='': break
    compra = float(input('Preço de Compra R$'))
    venda = float(input('Preço de Venda R$'))
    
    compras += compra
    vendas += venda
    lucro = ((venda - compra)/venda) * 100
    
    if lucro <= 10:
        dezpercent += 1
        print('{} produtos tiveram 10% de lucro.\n'.format(dezpercent))
    elif lucro > 10 and lucro <= 20:
        vintedezpercent += 1
        print('{} produtos tiveram entre 10% e 20% de lucro.\n'.format(vintedezpercent))   
    
    else:
       vintepercent += 1
       print('{} produtos tiveram mais de 20% de lucros.\n'.format(vintepercent))     
    
print('{} foi comprada a R${:<.2f}\nVendida a R${:<.2f}\nE gerou {:<.1f}% de lucro.\n'.format(nome, compra, venda, lucro))
print('R${:<.2f} em compras\nR${:<.2f} em vendas\nLucro total: R${:<.2f}.\n'.format(compras, vendas, (vendas-compras)))
print('porcentagem total: {:.1f}%'.format(((vendas-compras)/vendas)*100))