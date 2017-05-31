from time import time


def timer(f):
	def wrapper(*args):
		start = time()
		result = f(*args)
		end = time()
		print end - start
		return result
	return wrapper


def summ(a, b, c):
	return sum([a, b, c])


print summ(3, 6, 9)
