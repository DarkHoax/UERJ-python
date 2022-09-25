from random import choice

ano = 2021

estadio = ['Estádio Monumental "U"', 'Estádio do Maracanã', 'Estádio Morumbi', 'Estádio Mané Garrincha', 'Estádio Monumental de Núñez', 'Estádio do Castelão','Estádio Mineirão', 'Estádio Arena do Grêmio', 'Estádio Centenario', 'Estádio da Arruda', 'Estádio Nacional del Peru', 'Estádio Monumental Isidro Romero Carbo', 'Estadio Mario Alberto Kempes', 'Estadio La Bombonera', 'Estádio Municipal João Havelange', 'Estádio Ciudad de La Plata', 'Estádio Albertão', 'Estádio Deportivo Cali', 'Estádio Monumental de Maturín', 'Estádio Presidente Juan Domingo Perón', 'Estádio Beira-Rio', 'Estádio Serra Dourada', 'Estádio Arena Fonte Nova']

"""[', Michigan Stadium', 'Beaver Stadium', 'Ohio Stadium', 'Kyle Field', 'Neyland Stadium', 'Tiger Stadium', 'Bryant-Denny Stadium', 'Darrell K Royal-Texas Memorial Stadium', 'Estadio Azteca', 'L.A. Coliseum Museum Stadium', 'Stanford Stadium', 'Rose Bowl Stadium', 'Cotton Bowl Stadium', 'Ben Hill Griffin Stadium', 'Jordan-Hare Stadium', 'Lincoln Memorial Stadium', 'MetLife Stadium', 'Gaylord Family Oklahoma Memorial Stadium', 'Clemson Memorial Stadium', 'FedEx Field', 'Bank of America Stadium', 'Mercedes-Benz Stadium', 'Camping World Stadium', 'Gillette Stadium', 'Lumen Field', 'Lucas Oil Stadium', 'Aloha Stadium', 'TIAA Bank Field', 'Estádio Olimpico Universitário do México']"""


while ano < 2031:
	final = choice(estadio)
	print('\nNo ano',ano,'a final será no',final)
	ano += 1