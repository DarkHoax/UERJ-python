s = n = total = 0
while i < 6:
    print('Telefonou para a vitima?: ')
    resp = input('[S/N]: ').strip().upper()

print('Esteve no local do crime?: ')
resp1 = input('[S/N]: ').strip().upper()

print('Mora perto da vitima?: ')
resp2 = input('[S/N]: ').strip().upper()

print('Devia para a vitima?: ')
resp3 = input('[S/N]: ').strip().upper()

print('Ja trabalhou com a vitima?: ')
resp4 = input('[S/N]: ').strip().upper()

if resp == 'S':
    s += 1

if s == 5:
    print('Eh o assassino')
elif s == 4 or s == 3:
    print('Cumplice')
elif s == 2:
    print('Suspeito')
elif s == 1:
    print('Inocente')