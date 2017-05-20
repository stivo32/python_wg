def intersection(list1, list2):
	return list(set(list1) & set(list2))


def numerate_items(*args):
	result = []
	for data in args:
		stat = collect_count_stats(data)

		def decrease_stat(item):
			current_stat = stat[item]
			stat[item] -= 1
			return (item, current_stat)

		result.append([
			decrease_stat(item)
			for item in data
		])
	return result


def collect_count_stats(data):
	return {
		number: data.count(number)
		for number in data
	}


def denumerate_items(data):
	return [
		item for item, _ in data
	]


def main():
	list1 = [3, 2, 3]
	list2 = [2, 1, 5]
	data = [list1, list2]
	data = numerate_items(*data)
	print data
	data = intersection(*data)
	data = denumerate_items(*data)
	print data

if __name__ == '__main__':
	main()
