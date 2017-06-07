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


class Ork(Creature):
	def __init__(self, health=300, force=30):
		super(Ork, self).__init__(health, force)

	def hit(self, enemy):
		multiple = 1.0
		start_force = self.force
		if isinstance(enemy, Human):
			multiple *= 1.5
		self.force *= multiple
		super(Ork, self).hit(enemy)
		self.scream(enemy)
		self.force = start_force

	def scream(self, enemy):
		reduce_force = (self.force * 1.0) / enemy.force if self.force > enemy.force else 1
		enemy.force = int(enemy.force / reduce_force)


class Human(Creature):
	def __init__(self, health=150, force=20):
		super(Human, self).__init__(health, force)


ork1 = Ork(400, 50)
human1 = Human()
ork1.hit(human1)

print human1.health, human1.force



