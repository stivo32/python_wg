# coding: utf-8
from random import randint


class Dice(object):
	def __init__(self, sides):
		self.chance = 100.0 / sides
		previous = 1
		self.list_with_sides = []
		for side in xrange(sides):
			self.list_with_sides.append([number for number in xrange(previous, previous + int(self.chance))])
			previous += int(self.chance)
		# list_with_chances = [lambda y, z, x: y < x <= z
		#                      for x, previous, previous + chance in xrange(1, sides + 1)]
		# print self.list_with_sides

	def throw_dice(self):
		number = randint(1, 100)
		for i, side in enumerate(self.list_with_sides, 1):
			if number in side:
				return i


class Player(object):
	def __init__(self, dices):
		self.dices = dices
		self.bag_with_dices = []
		for _ in xrange(self.dices):
			self.bag_with_dices.append(Dice(6))
		self.scores = 0

	def throw_all_dices(self):
		self.scores = sum([dice.throw_dice() for dice in self.bag_with_dices])
		print self.scores


def main():
	player = Player(6)
	player.throw_all_dices()


if __name__ == '__main__':
	main()
