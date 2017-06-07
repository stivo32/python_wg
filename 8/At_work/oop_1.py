
class Square(object):
	def __init__(self, side):
		self.side = side

	def perimetr(self):
		return self.side * 4

	def resize(self, scale):
		self.side *= scale

square = Square(10)
print square

print isinstance(square,  object)

