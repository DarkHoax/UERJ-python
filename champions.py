import random
i = j = 0

pote_1 = ['Borussia Dortmund', 'Real Madrid', 'CLUJ','BATE Borisov','Porto', 'Internazionale', 'Anderlecht','Tottenham']

pote_2 = ['Barcelona', 'Bayern München', 'Liverpool', 'Juventus','Manchester City', 'Athletic Madrid', 'Paris Saint Germain', 'RB Salzburg']

for i in

while i < 8:
    time1 = random.choice(pote_1)
    time2 = random.choice(pote_2)
    i += 1
    pote_1.remove(time1)
    pote_2.remove(time2)
    while j < i:
        print('Jogo {}\n'.format(i))
        print('{} vs {}'.format(time1, time2))
        j += 1