'''1. The city council of a city decided to conduct a survey among its workers. For this, it collected some data such as age, sex (M or F) and salary.

Build an algorithm to reads this data and writes it at the end:
 
 a) the average salary for men, the average salary for women
 b) the highest salary found among people under 30 years old.
 Note:
 (1) Consider that there are N workers
 (2) The end of the data reading is marked by a negative age.'''



count = highest = man = female = medm = medf = 0
while True:
	age = int(input('Age: '))
	if age < 0: break
	salary = float(input('Salary: '))
	sex = input('Gender: ').upper()
	count += 1
	
	if age < 30:
		if salary > highest:
			highest = salary
			
	if sex == 'M':
		man += 1
		medm += salary
		med_sal = (medm / man)
	elif sex == 'F':
		female += 1
		medf += salary
		med_salf = (medf / female)
		
print('The male salarial media is ${:<.2f}'.format(med_sal))
print('The female salarial media is ${:<.2f}'.format(med_salf))
print('The highest salary under 30 years old is ${:<.2f}'.format(highest))
