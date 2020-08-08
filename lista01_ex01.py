#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Mon Dec 16 20:11:11 2019

lista 01 - ex 01
A prefeitura de uma cidade resolveu fazer uma pesquisa entre os seus
trabalhadores. Para isso ela coletou alguns dados como idade, sexo (M ou F) e salário.
Crie um algoritmo que leia estes dados e que escreva ao final:
a) a média salarial dos homens, a média salarial das mulheres
b) o maior salário encontrado entre as pessoas abaixo de 30 anos.
Obs:
(1) Considere que existem N trabalhadores
(2) O final da leitura de dados é marcado por uma idade negativa.

@author: argos'''
cont = medsalh = medsalf = homem = mulher = maiorsalario = 0

while True:
    cont += 1
    idade = int(input('Digite a idade: '))
    if idade < 0: break
    sexo = input('Digite o sexo [M ou F]: ').upper()
    salario = float(input('Digite o salário: '))
    
    #CALCULA A MÉDIA DE IDADES
    if salario > maiorsalario:
        if idade < 30:
            maiorsalario = salario
    
    #CALCULA A MÉDIA SALARIAL DOS HOMENS
    if sexo == 'M':
        homem += 1
        medsalh += salario
    
    #CALCULA A MÉDIA SALARIAL DAS MULHERES
    if sexo == 'F':
        mulher += 1
        medsalf += salario
    
print('\nMÉDIA SALARIAL MASCULINA: R${:<.2f}\nMÉDIA SALARIAL FEMININA R${:<.2f}'.format(medsalh/homem, medsalf/mulher))
print('\nO MAIOR SALÁRIO PARA QEM TEM IDADE < 30, É: R${:<.2f}'.format(maiorsalario))
