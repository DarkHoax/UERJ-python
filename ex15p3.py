'''Elabore um programa que leia uma matriz de tamanho mxm elementos inteiros
e, determine a soma da primeira linha com a segunda. Imprimir a matriz lida e o
resultado obtido com mensagens indicativas.'''

def Gera():
    while True:
        try:
            m = int(input('Digite um termo para o quadrado: '))
            break
        except ValueError or m == '':
            print('Erro. Tente novamente...')
            m = int(input('Digite um termo para o quadrado: '))
    return m, n

def Forma(m):
    a = [None] * m
    for i in range(m):
        a[i] = [None] * m
        for j in range(m):
            while True:
                try:
                    a[i][j] = float(input('Digite A = ['+str(i+1)+'],['+str(j+1)+']: '))
                    break
                except ValueError:
                    print('Erro na matriz. Digite novamente...')
    return a

def Soma(a,n):
    s=[]
    for i in range(0,n):
         x=a[0][i]+a[1][i]
         s.append(x)
    return s   

def Impr(a,s,m,n):
    print(f"\n{'Matriz Lida' : >20}\n")

    for i in range(m):
        for j in range (n):
            print (f'{a[i][j]:10.2f}',end=' ')
        print()
    print(f"\n{'Vetor Soma' : >20}\n")
    for i in range(n):
        print (f'{s[i]:>10.2f}'  ,end=' ')
    return    
    
m, n = Gera()
a = Forma(m, n)
s = Soma(a,n)
Impr(a,s,m,n)