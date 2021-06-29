def Telefone():
    escolha = input('Deseja digitar com hifen? [S/N]:').upper()
    if escolha == 'S':
        p = input('Digite 3 ou 4 numeros: ')
        if len(p) < 3 or len(p) > 4: raise
        else: print('Nao eh um numero')
        
        f = input('Digite os 4 numeros finais: ')
        elif len(f) < 4 or len(f) > 4: raise
        else: print('Nao eh um numero')
    
    if escolha == 'N':
        num = input('Digite 7 ou 8 numeros: ')
        if len(num) == 7:
            novo = '3' + num
    return novo, num, p, f

def Impr():
    