# coding: utf-8

VOWELS = 'aeyuio'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'


def is_contain(symbol, dataset=CONSONANTS):
	return symbol in dataset


def symbol_count(line):
	count = 0
	for symbol in line:
		if is_contain(symbol):
			count += 1
	return count


if __name__ == '__main__':
	while True:
		user_input = raw_input('>>>')
		if not user_input:
			break
		print symbol_count(user_input)
