from random import choice


def bandit():
	numbers = ['apple', 'gold', 'cheese']
	a, b, c = choice(numbers), choice(numbers), choice(numbers)
	if a == b == c:
		if a == 'gold':
			print 'You won GOLD!'
		else:
			print "Congrats, You won food!"
	else:
		print "Mb next time..."


def main():
	bandit()

if __name__ == '__main__':
	main()
