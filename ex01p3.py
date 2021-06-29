'''1. Elabore um programa que leia o vetor A com 5 valores inteiros. Determine um
vetor com a seguinte lei de formação: Os termos de ordem impar de A são
multiplicados por 3 Os termos de ordem par de A são multiplicados por 2'''

def Ler():
    i = 0
    while i < 5:
        a = []
        num = int(input('Digite um numero: '))
        a.append(num)
        i += 1
    return a

def Calcula(a):
    for i in len(a):
        if i % 2 == 1:
            i *= 3
        else:
            i *= 2
    return a
def Impr(a):
    print('{}'.format(a))
    return

a = Ler()
a = Calcula(a)
Impr(a)
