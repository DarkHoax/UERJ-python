vet=[]
vet2=[]
soma = soma2 = cont = cont2 = cont3 = 0
for i in range(0,10):
    c = float(input('Digite °C: '))
    soma += c
    cont += 1
    vet.append(c)
    f = 1.8*c + 32
    soma2 += f
    cont2 += 1
    vet2.append(f)
    
print('Temperaturea em Celsius:',vet)
print('Temperatuda em Farenheit:',vet2)
media=soma/cont
media2=soma2/cont2
for i in range(0,10):
    if vet2[i]>media2:
        cont3 += 1
print('Media em Celsius:',media)
print('Media em Farenheit:',media2)
print('Temperaturas acima da media em Ferenheit',cont3)