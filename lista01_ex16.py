#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Created on Wed Jan 15 20:40:55 2020

AINDA HÁ ERROS NO CODIGO

16. Crie um algoritmo que:
    
    a) Leia e escreva o nome e a altura das moças inscritas em um concurso de
    beleza, até que seja digitada o nome ‘MARIA’, que marca o final da lista, 
    mas é para ser computada no concurso.
    
    b) Calcule e escreva as duas maiores alturas e quantas moças as possuem.

@author: argos'''
maior_Altura = segMaior_Altura = maior = menor = cont = 0
altura = list()
nome = list()
while True:
    cont += 1
    nome.append(input('Digite um nome [MARIA para sair do loop]: ').upper())
    if nome == 'MARIA': break
    altura.append(float(input('Digite a altura: ')))
    for i in range(0, len(nome)):
        if altura[i] >= maior_Altura:
            if altura[i] > maior_Altura:
                segMaior_Altura = maior_Altura
                maior_Altura = altura[i]
                menor = maior
                maior = 1
            else:
                maior_Altura = altura[i]
                maior += 1
        else:
            if altura[i] >= segMaior_Altura:
                if altura[i] > segMaior_Altura:
                    segMaior_Altura = altura[i]
                    menor = 1
                else:
                    segMaior_Altura = altura[i]
                    menor += 1
print('Maior {:<.2f} -> Quantidade {}\nMenor {:<.2f} -> Quantidade {}'.format(maior_Altura, maior, segMaior_Altura, menor))
