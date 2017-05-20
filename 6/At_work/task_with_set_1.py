def intersection(list1, list2):
	return list(set(list1) & set(list2))


def main():
	list1 = [1, 2, 3]
	list2 = [2, 1, 5]
	print intersection(list1, list2)


if __name__ == '__main__':
	main()