'''Escreva uma programa que grave em um arquivo uma palavra depois leia este arquivo execute
uma função que aceita a palavra lida como parâmetro e retorna a mesma palavra com as
vogais duplicadas. Por exemplo, o chamado da função com o parâmetro 'obrigado' deve
retornar 'oobriigaadoo'.'''

def Ler():
    with open('ex13p5.txt','w+') as file:            
        while True:
            try:
                palavra = input('Digite um frase: ').strip().lower()
                break
            except:
                print('Erro.. Tente de novo')
        file.write(palavra+'\n')
    return palavra

def Duplica(palavra):
    res = ''
    with open('ex13p5.txt','r') as file:
        pal = file.readlines()
        t = len(pal)

        for i in range(t):
            if pal == 'a' or pal == 'e' or pal == 'i' or pal == 'o' or pal == 'u':
                res += pal[i]
            res += pal[i]
  
    return res

def Impr(palavra, res):
    print('Palavra Original: {}\nModificada: {}'.format(palavra, res))
    return


palavra = Ler()
res = Duplica(palavra)
Impr(palavra, res)