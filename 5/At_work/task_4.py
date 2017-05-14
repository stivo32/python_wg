def func(*args):
	summ = 0
	for arg in args:
		summ += arg
	return summ

if __name__ == '__main__':
	print func(1, 2, 3)
