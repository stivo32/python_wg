from random import choice, randint


class Cell(object):
	def __init__(self, max_value):
		self.max_value = max_value

	def roll(self):
		return randint(1, self.max_value)


class Bandit(object):
	max_cell_value = 3

	def __init__(self, cell_number=3):
		self.cells = [
			Cell(self.max_cell_value)
			for _ in range(cell_number)
		]

	def _roll(self):
		return [cell.roll() for cell in self.cells]

	def action(self):
		cell_values = self._roll()
		x, y, z = cell_values
		if x == y == z:
			return 'You won', cell_values
		else:
			return 'You failed', cell_values


def main():
	bandit = Bandit(cell_number=3)
	result, values = bandit.action()
	print result, values

if __name__ == '__main__':
	main()