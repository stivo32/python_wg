def forxy(col1, col2):
	for x in col1:
		for y in col2:
			yield x, y


def main():
	print list(forxy('ab', (1, 2)))


if __name__ == '__main__':
	main()
