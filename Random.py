import random
r = random.randint(1, 100)
t = 0
while True:
	g = input('Please guess a number between 1~100 : ')
	g = int(g)
	t = t + 1 # t += 1
	if g == r:
		print('Guessed Right! Guess', t, 'times')
		break
	else:
		if g > r:
			print('Guess towards the lower number, guess', t, 'times')
		elif g < r:
			print('Guess towards the higher number, guess', t, 'times') 
