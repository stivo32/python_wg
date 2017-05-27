def countdown(count):
	return (i for i in range(count, 0, -1))


def countdown2(count):
	while True:
		if count < 1:
			raise StopIteration
		yield count
		count -= 1


def main():
	#print list(countdown(5))
	print list(countdown2(5))


if __name__ == '__main__':
	main()
