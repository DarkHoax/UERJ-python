'''1. Elabore um programa que leia o vetor A com 5 valores inteiros. Determine um
vetor com a seguinte lei de formação: Os termos de ordem impar de A são
multiplicados por 3 Os termos de ordem par de A são multiplicados por 2'''

def Ler():
    i = 0
    a = []
    with open('1p5.txt','w+') as file:
        while i < 5:
            while True:
                try:
                    num = int(input('Digite um numero: '))
                    i += 1
                    break
                    file.write(str(num)+'\n')
        return

def Calcula(num):
    lista = []
    with open('1p5.txt','r') as file:
        v = file.readlines()
        v = int(v)
        lista.append(v)

        for i in lista:
            if i % 2 == 1:
                i *= 3
            else:
                i *= 2
    return lista
def Impr(lista):
    print('{}'.format(a))
    return

Ler()
lista = Calcula()
Impr(a)