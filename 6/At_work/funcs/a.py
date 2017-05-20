def summa(*args):
	summ = 0
	for arg in args:
		summ += arg
	return summ

if __name__ == '__main__':
	print summa(1, 2, 3)
