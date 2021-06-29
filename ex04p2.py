def Data():
    dia = input('Digite o dia de nascimento: ')
    mes = input('Digite o mes de nascimento: ')
    ano = input('Digite o ano de nascimento: ')
    return dia, mes, ano

def Troca(dia, mes, ano):
    mes = float(mes)
    if len(ano) < 4:
        print('Digite o ano com os 4 digitos')
    if mes > 29:
        print('Digite fevereiro ate dia 29')
    else:
        if mes == 1:
            print('Sua data de nascimento eh {} de janeiro de {}'.format(dia, ano))
        elif mes == 2:
            print('Sua data de nascimento eh {} de fevereiro de {}'.format(dia, ano))
        elif mes == 3:
            print('Sua data de nascimento eh {} de março de {}'.format(dia, ano))
        elif mes == 4:
            print('Sua data de nascimento eh {} de abril de {}'.format(dia, ano))
        elif mes == 5:
            print('Sua data de nascimento eh {} de maio de {}'.format(dia, ano))
        elif mes == 6:
            print('Sua data de nascimento eh {} de junho de {}'.format(dia, ano))
        elif mes == 7:
            print('Sua data de nascimento eh {} de julho de {}'.format(dia, ano))
        elif mes == 8:
            print('Sua data de nascimento eh {} de agosto de {}'.format(dia, ano))
        elif mes == 9:
            print('Sua data de nascimento eh {} de setembro de {}'.format(dia, ano))
        elif mes == 10:
            print('Sua data de nascimento eh {} de outubro de {}'.format(dia, ano))
        elif mes == 11:
            print('Sua data de nascimento eh {} de novembro de {}'.format(dia, ano))
        else:
            print('Sua data de nascimento eh {} de dezembro de {}'.format(dia, ano))
    return

dia, mes, ano = Data()
Troca(dia, mes, ano)