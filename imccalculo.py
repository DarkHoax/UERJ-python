peso = float(input("Diga o seu peso em kg: "))
altura = float(input("Diga a sua altura em m: "))

imc = peso / (altura**2)

print(f"\n\tSeu imc é {imc:.2f} kg/cm")