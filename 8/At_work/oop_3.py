class Figure(object):
	def P(self):
		raise NotImplemented()


class Rectangle(Figure):
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def P(self):
		return 2 * (self.width + self.height)


class Square(Rectangle):
	def __init__(self, width):
		super(Square, self).__init__(width, width)


x = Square(5)
y = Rectangle(5, 10)
print y.width, y.height
print x.width, x.height

print issubclass(Square, Rectangle)

print getattr(x, 'width', 666)
