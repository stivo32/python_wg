from contextlib import contextmanager
from random import choice

@contextmanager
def choose_one(names):
	name = choice(names)
	print 'Choosen: {}'.format(name)

	yield name

	print 'Bye!'

with choose_one(['A', 'B', 'C']) as name:
	print 'Hello', name, '!'