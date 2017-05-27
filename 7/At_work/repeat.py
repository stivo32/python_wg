def repeat(collection, n=2):
	for a in collection:
		for i in xrange(n):
			yield a


def main():
	col = [1, 'a', [False]]
	print list(repeat(col))


if __name__ == '__main__':
	main()

