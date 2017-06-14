# coding: utf-8


class Fraction(object):
	def __init__(self, numerator, denominator):
		self.numerator = numerator
		self.denominator = denominator

	def __str__(self):
		if self.numerator % self.denominator == 0:
			result_string = '{}({})'.format(Fraction.__name__, self.numerator / self.denominator)
		else:

			result_string = '{}({}, {})'.format(Fraction.__name__, self.numerator, self.denominator)
		return result_string

	def __add__(self, other):
		if isinstance(other, int):
			self.numerator += other * self.denominator
		elif isinstance(other, Fraction):
			if self.denominator == other.denominator:
				self.numerator += other.numerator
			else:
				self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
				self.denominator *= other.denominator
		return Fraction(self.numerator, self.denominator)

	def __mul__(self, other):
		if isinstance(other, int):
			self.numerator *= other
		elif isinstance(other, Fraction):
			self.numerator *= other.numerator
			self.denominator *= other.denominator
		return Fraction(self.numerator, self.denominator)

	def __div__(self, other):
		if isinstance(other, int):
			self.denominator *= other
		elif isinstance(other, Fraction):
			self.numerator *= other.denominator
			self.denominator *= other.numerator
		return Fraction(self.numerator, self.denominator)

	def __sub__(self, other):
		if isinstance(other, int):
			self.numerator -= other * self.denominator
		elif isinstance(other, Fraction):
			if self.denominator == other.denominator:
				self.numerator -= other.numerator
			else:
				self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
				self.denominator *= other.denominator
		return Fraction(self.numerator, self.denominator)

	def _normal_form(self):
		min_number = min(self.numerator, self.denominator)
		simple_list = simple_numbers(min_number)
		for number in xrange(simple_list):
			pass
		return simple_list


def simple_numbers(number):
		if number == 1:
			return number
		L = range(2, number + 1)
		R = set()

		while True:
			if not L:
				break
			x = L.pop()
			if x % 5 == 0 and x != 5:
				L.insert(0, x / 5)
				continue
			if x % 3 == 0 and x != 3:
				L.insert(0, x / 3)
				continue
			if x % 2 == 0 and x != 2:
				L.insert(0, x / 2)
				continue
			R.add(x)
		return sorted(R)


def main():
	frac = Fraction(33, 11)
	# frac2 = Fraction(4, 6)
	# print (frac - 3) * 3
	# #print frac + frac2
	print frac._normal_form()
	#print simple_numbers(22)

if __name__ == '__main__':
	main()