#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Created on Wed Mar 25 19:14:11 2020

∆ 1.12.9. Foi feita uma pesquisa para determinar o índice de mortalidade infantil 
em um certo período. Fazer um algoritmo que:
    - leia inicialmente o número de crianças nascidas no período;
    - leia, em seguida um número indeterminado de linhas, contendo, 
    cada uma, o sexo de uma criança morta (masculino, feminino) e o número de 
    meses de vida da criança. A última linha, que não entrará nos cálculos, 
    contém no lugar do sexo a palavra “vazio”;
    - determine e imprima:

a) a porcentagem de crianças mortas no período;
b) a porcentagem de crianças do sexo masculino mortas no período;
c) a porcentagem de crianças que viveram 24 meses ou menos no período.

@author: argos'''
from random import randint as rt
cont = nascida = morta = h = f = cont_meses = meses = 0
while(True):
    nativ = input('[N]asceu/[M]orreu: \n').upper()
    sexo = input('[H] ou [F], vazio para terminar: \n').upper()
    cont += 1
    if sexo == 'VAZIO': break
    
    if nativ == 'N':
        nascida += 1
    elif nativ == 'M':
        morta += 1
        if sexo == 'H':
            h += 1
            meses = rt(1,60)
        elif sexo == 'F':
            f += 1
            meses = rt(1,60)
    if nativ == 'M' and meses <= 24:
        cont_meses += 1
        print('{} crianças morreram com 24 meses ou menos'.format(cont_meses))
print('Crianças mortas: {:<.2f}%'.format((morta - cont)*100))
print('Meninos mortos: {:<.2f}%'.format(((h-morta) - cont)*100))
print('Viveram menos de 24 meses: {:<.2f}%'.format((cont_meses - cont)*100))    