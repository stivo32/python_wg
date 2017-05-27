from time import time, sleep


def sleeper(tosleep):
	def timer(f):
		def wrapper(*args, **kwargs):
			start = time()
			sleep(tosleep)
			result = f(*args, **kwargs)
			end = time()
			print end - start
			return result
		return wrapper


@timer(sleep=4)
def summ(a, b, c):
	return sum([a, b, c])

print summ(3, 6, 9)

timer = timer()