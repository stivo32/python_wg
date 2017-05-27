from forxy import forxy


def takexy(col1, col2, func):
	for a, b in forxy(col1, col2):
		if func(a, b):
			yield a, b


def main():
	col1 = 'ab'
	col2 = (1, 2)
	print list(takexy(col1, col2, lambda x, y: len(x * y) > 1))

if __name__ == '__main__':
	main()