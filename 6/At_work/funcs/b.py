def sqr_x2(**kwargs):
	sqr = '_sqr'
	twice = '_2x'
	actions = {
				sqr: lambda x: x ** 2,
				twice: lambda x: x * 2,
				}
	result = dict()
	for arg, value in kwargs.items():
		for end, action in actions.items():
			if arg.endswith(end):
				norm_arg = normalize_name(arg, end)
				result[norm_arg] = action(value)
	return result


def normalize_name(var, end):
	return var[:-len(end)]

if __name__ == '__main__':
	dataset = {'2_sqr': 3, '3_2x': 5, 'qwer_sqr': 10}
	print sqr_x2(**dataset)

