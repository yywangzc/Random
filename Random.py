l = input('Please key in the lower integer : ')
h = input('please key in the higher integer : ')
l = int(l)
h = int(h)
import random
r = random.randint(l, h)
t = 0
while True:
	g = input('Please guess a number : ')
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
