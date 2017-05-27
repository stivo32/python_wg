def merge(collection):
	iterator = iter(collection)
	while True:
		for element in next(iterator):
			yield element


def merge_deep(collection):
	from collections import Iterable
	for item in collection:
		if not isinstance(item, Iterable):
			yield item
			continue
		for sub_item in merge_deep(item):
			yield sub_item
	# try:
	# 	iterator = iter(collection)
	# 	for sub_col in iterator:
	# 		yield (merge_deep(sub_col)
	# except TypeError:
	# 	print collection
	# 	yield collection




def main():
	col = [[1, 2], [3], [[4]], [1, 2, 3]]
	col1 = [1, 2, 'as']
	#print list(merge(col))
	print list(merge_deep(col))


if __name__ == '__main__':
	main()
