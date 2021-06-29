"Média Aritmética"

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = (nota1 + nota2)/2
if media >= 7.0:
    print('Aprovado com media ', media)
elif media >= 4.0 and media <= 6.9:
    print('Em prova final com media ', media)
else:
    print('Reprovado com média ', media)
