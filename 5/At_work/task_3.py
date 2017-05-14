def factorial(number):
	if number == 0:
		return 1
	fact = 1
	for i in range(1, number + 1):
		fact *= i
	return fact


def math_func(n, m):
	return factorial(n * m) / (factorial(n) * factorial(m))


if __name__ == '__main__':
	print math_func(2, 2)
