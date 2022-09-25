brasil = 216105307
angola = 34756870
brasilf = angolaf = 0
taxab = 0.0091
taxaa = 0.0329

ano = 2022

for i in range(ano):
	brasilf += (brasil * taxab) + brasil
	angolaf += (angola *taxaa) + angola
	ano += 1
print(f"Ano {ano}\n")
print(f"População Brasil: {brasilf:.0f}")
print(f"População Angola: {angolaf:.0f}\n")