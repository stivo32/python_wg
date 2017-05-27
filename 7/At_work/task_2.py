
def sqr(count, start=1):
	i = start
	while True:
		yield i ** 2
		if i >= count:
			break
		i += 1


def sqr2(count, start=1):
	for i in xrange(start, count + 1):
		yield i ** 2


def infinite_sqr():
	i = 1
	while True:
		yield i ** 2
		i += 1


def main():
	print list(sqr(5))
	print list(sqr2(5))
	inf = infinite_sqr()
	for i in xrange(6):
		print next(inf),

if __name__ == '__main__':
	main()