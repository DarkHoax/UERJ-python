
contrato = float(input('Digite o salário: '))
ano = int(input('Digite quantos anos de contrato: '))

anos = ano * 6

print(f'Salário de US${contrato:.2f}')
print(f'Salário de US$ {(contrato/anos):.2f} por temporada')