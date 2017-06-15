# coding: utf-8


class Fraction(object):
	def __init__(self, numerator, denominator):
		self.numerator = numerator
		self.denominator = denominator

	def __str__(self):
		if self.numerator % self.denominator == 0:
			result_string = '{}({})'.format(Fraction.__name__, self.numerator / self.denominator)
		else:
			self._normal_form()
			result_string = '{}({}, {})'.format(Fraction.__name__, self.numerator, self.denominator)
		return result_string

	def __add__(self, other):
		temp_numerator = 1
		temp_denominator = 1
		if isinstance(other, int):
			temp_numerator = self.numerator + other * self.denominator
		elif isinstance(other, Fraction):
			if self.denominator == other.denominator:
				temp_numerator = self.numerator + other.numerator
				temp_denominator = self.denominator
			else:
				temp_numerator = self.numerator * other.denominator + other.numerator * self.denominator
				temp_denominator = self.denominator * other.denominator
		return Fraction(temp_numerator, temp_denominator)

	def __mul__(self, other):
		temp_numerator = 1
		temp_denominator = 1
		if isinstance(other, int):
			temp_numerator = self.numerator * other
		elif isinstance(other, Fraction):
			temp_numerator = self.numerator * other.numerator
			temp_denominator = self.denominator * other.denominator
		return Fraction(temp_numerator, temp_denominator)

	def __div__(self, other):
		temp_numerator = 1
		temp_denominator = 1
		if isinstance(other, int):
			temp_denominator = self.denominator * other
		elif isinstance(other, Fraction):
			temp_numerator = self.numerator * other.denominator
			temp_denominator = other.numerator * self.denominator

		return Fraction(temp_numerator, temp_denominator)

	def __sub__(self, other):
		temp_numerator = 1
		temp_denominator = 1
		if isinstance(other, int):
			temp_numerator = self.numerator - other * self.denominator
			temp_denominator = self.denominator
		elif isinstance(other, Fraction):
			if self.denominator == other.denominator:
				temp_numerator = self.numerator - other.numerator
				temp_denominator = self.denominator
			else:
				temp_numerator = self.numerator * other.denominator - other.numerator * self.denominator
				temp_denominator = self.denominator * other.denominator
		return Fraction(temp_numerator, temp_denominator)

	def _normal_form(self):
		min_number = min(self.numerator, self.denominator)
		simple_list = simple_numbers(min_number)
		for number in simple_list:
			while True:
				if self.numerator % number == 0 and self.denominator % number == 0:
					self.numerator /= number
					self.denominator /= number
					# print '{} / {}'.format(self.numerator, self.denominator)
				else:
					break


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
	frac = Fraction(32, 1024)
	frac2 = Fraction(256, 16)
	print frac * frac2


if __name__ == '__main__':
	main()