def func(*args):
	summ = 0
	for arg in args:
		summ += arg
	return summ

if __name__ == '__main__':
	numbers = [int(x) for x in raw_input().split()]
	print func(*numbers)
