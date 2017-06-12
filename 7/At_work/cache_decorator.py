# coding: utf-8


def cache_decorator(f):
	memory = {}

	def wrapper(*args, **kwargs):
		if args in memory:
			return memory[args]
		else:
			res = f(*args, **kwargs)
			memory[args] = res
			return res
	return wrapper


@cache_decorator
def summ(a, b, c):
	print 'sum is...'
	return sum([a, b, c])


def main():
	print summ(3, 6, 9)
	print summ(3, 6, 9)
	print summ(1, 2, 3)
	print summ(1, 2, 3)

if __name__ == '__main__':
	main()