import random
r = random.randint(1, 100)
while True:
	g = input('Please guess a number between 1~100 : ')
	g = int(g)
	if g == r:
		print('Guessed Right!')
		break
	else:
		if g > r:
			print('Guess towards the lower number')
		elif g < r:
			print('Guess towards the higher number') 
