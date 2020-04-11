from random import randint

count = 0

while True:
	ans = randint(0,9)
	guess_it = int(input('\nChose a number: '))
	count += 1
	if guess_it < 0: break
	if guess_it == ans:
		print(f'\nRight! {guess_it} == {ans}')
	else:
		print(f'\nYou've made a Mistake!\nYour name == {guess_it}, random == {ans}')
