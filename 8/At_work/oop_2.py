class Creature(object):
	def __init__(self, health=100, force=10):
		self.health = health
		self.force = force

	def hit(self, enemy):
		if isinstance(enemy, Creature):
			enemy.health -= self.force

	def get_damage(self, enemy):
		if isinstance(enemy, Creature):
			self.health -= enemy.force


hero = Creature(200)
ork = Creature(40)

