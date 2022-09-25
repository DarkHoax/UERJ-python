from random import choice

estadios = ['Camp Nou', 'Wembley Stadium', 'Signal Iduna Park', 'Estádio Santiago Bernabéu','Estádio Luzhniki', 'San Siro', 'Estádio Olímpico Atatürk', 'Old Trafford', 'Allianz Arena', 'Berlin Olympiastadion', 'Millennium Stadium', 'Stadio Olimpico', 'NSC Olimpiyskiy', 'Estádio Olímpico de Baku', 'Estádio Spyros Louis', 'Münich Olympiastadion', 'Estádio Krestovsky', 'Wanda Metropolitano', 'Stade Vélodrome', 'Estádio da Luz', 'Veltins-Arena', 'London Stadium', 'Puskás Aréna', 'Tottenham Hotspur Stadium', 'Estadio Benito Villamarín', 'Emirates Stadium', 'Mercedes-Benz Arena', 'Celtic Park', 'Estadi Olímpic Lluís Companys', 'Estadio Olímpico de Sevilla']
temporada = 2022

while temporada < 2033:
	final = choice(estadios)
	print('Na temporada de',temporada,'a final da Champions League será no',final,'\n')
	temporada += 1