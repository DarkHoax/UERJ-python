'''Matrix trnasposta'''

def Gera():
    try:
        m = int(input('Digite um termo para o quadrado: '))
    except ValueError:
        print('Erro. Tente novamente...')
        m = int(input('Digite um termo para o quadrado: '))
    return m

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
def Impr(a):
    t = []
    #Matriz Original
    print ('\nMatriz Original\n')
    for i in range(m):
        for j in range (m):
            print ('|{:.2f}|'.format(a[i][j]),end=' ')
        print()
    
    #Matriz Transposta
    print('\nMatriz Transposta\n')
    for i in range(len(a)): #Roda as colunas
        for j in range(len(a[0])):
            t[j][i] = a[i][j]
    for r in t:
        print(r)
    return

m = Gera()
a = Forma(m)
Impr(a)