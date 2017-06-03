# coding: utf-8

from time import time, sleep


def timer(t=2):
	def decorator(f):
		def wrapper(*args, **kwargs):
			start = time()
			sleep(t)
			result = f(*args, **kwargs)
			end = time()
			print end - start
			return result
		return wrapper
	return decorator

@timer(5)
def summ(a, b, c):
	return sum([a, b, c])


print summ(3, 6, 9)