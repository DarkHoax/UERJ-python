from random import choice

potea = ['River', 'Boca Jrs', 'Flamengo', 'Nacional', 'Peñarol', 'Atl Mineiro', 'Cerro']

poteb = ['Atl Paranaense', 'Libertad', 'Del Valle', 'Unv. Católica', 'Emelec', 'Corithians', 'Colo Colo', 'Velez']

potec = ["Sporting Cristal", "Deportivo Cali", "RB Bragantino", "Deportivo Táchira", "Alianza Lima", "Deportes Tolima", "Colón", "Caracas"]

poted = ["Always Ready", "Talleres", "Ind. Petrolero", "Fortaleza", "Olimpia", "Estudiantes", "The Strongest", "América Mineiro"]

ga = []
gb = []
gc = []
gd = []
ge = []
gf = []
gg = []
gh = []

a = b = c = d = e = f = g = h = 0

ga.append("Palmeiras")
for a in potea:
	gb.append(choice(potea))
	gc.append(choice(potea))
	gd.append(choice(potea))
	ge.append(choice(potea))
	gf.append(choice(potea))
	gg.append(choice(potea))
	gh.append(choice(potea))
	
for b in poteb:
	ga.append(choice(poteb))
	gb.append(choice(poteb))
	gc.append(choice(poteb))
	gd.append(choice(poteb))
	ge.append(choice(poteb))
	gf.append(choice(poteb))
	gg.append(choice(poteb))
	gh.append(choice(poteb))
	b += 1
	