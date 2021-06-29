def Ler():
    string_a = input('Digite uma frase: ').strip().lower()
    string_b = input('Digite outra frase: ').strip().lower()
    return string_a, string_b

def Recoloca(string_a, string_b):
    frase1 = ''
    frase2 = ''

    frase1 = string_a.replace(' ','')
    frase2 = string_b.replace(' ','')
    return frase1, frase2

def Impr(string_a, frase1, string_b, frase2):
    print('"{}" tem {} caracteres e "{}" tem {} caracteres.'.format(string_a, len(frase1), string_b, len(frase2)))

    if len(frase1) == len(frase2):
        if frase1 == frase2:
            print('Possuem o mesmo comprimento e sao iguais')
        else:
            print('Possuem o mesmo comprimenro e sao diferentes')
    else:
        print('Nao possuem o mesmo comprimento entao nao sao iguais')
    return

string_a, string_b = Ler()
frase1, frase2 = Recoloca(string_a, string_b)
Impr(string_a, frase1, string_b, frase2)