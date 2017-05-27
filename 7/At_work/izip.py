def izip(col_1, col_2):
	iter1 = iter(col_1)
	iter2 = iter(col_2)
	while True:
		yield next(iter1), next(iter2)


def izip_long(col_1, col_2):
	iter1 = iter(col_1)
	iter2 = iter(col_2)
	stop1 = False
	stop2 = False
	while True:
		try:
			first = next(iter1)
		except StopIteration:
			first = None
			stop1 = True
		try:
			second = next(iter2)
		except StopIteration:
			second = None
			stop2 = True
		if stop1 and stop2:
			break
		yield first, second


def izip_long_var2(col_1, col_2):
	iter1 = iter(col_1)
	iter2 = iter(col_2)
	stop1 = object()
	stop2 = object()
	while True:
		first = next(iter1, stop1)
		second = next(iter2, stop2)
		is_finish1 = first is stop1
		is_finish2 = second is stop2
		if is_finish1 and is_finish2:
			break
		yield (
			first if not is_finish1 else None,
			second if not is_finish2 else None,
		)


def main():
	col_1 = (1, 2, 3, 4, 5)
	col_2 = set('ABCD')
	for tup in izip_long(col_1, col_2):
		print tup,


if __name__ == '__main__':
	main()


