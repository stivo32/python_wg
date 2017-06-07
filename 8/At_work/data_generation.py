import string
from random import randint, choice
from pprint import pprint


class GeneratedField(object):
	def generate(self):
		raise NotImplementedError()


class IntegerField(GeneratedField):
	def __init__(self, min, max):
		self.min = min
		self.max = max

	def generate(self):
		return randint(self.min, self.max)


class CharField(GeneratedField):
	NUMERIC_CHARS = '1234567890'
	ALPHA_CHARS = string.ascii_lowercase
	ALPHA_NUMERIC_CHARS = ALPHA_CHARS + NUMERIC_CHARS

	def __init__(self, min_length, max_length, chars=ALPHA_NUMERIC_CHARS):
		self.min_length = min_length
		self.max_length = max_length
		self.chars = chars

	def generate(self):
		count = randint(self.min_length, self.max_length)
		return ''.join([
			choice(self.chars)
			for _ in xrange(count)
		])


class ChoiceField(GeneratedField):
	def __init__(self, choices):
		self.choices = list(choices)

	def generate(self):
		return choice(self.choices)


class ModelField(GeneratedField):
	def __init__(self, model):
		self.model = model

	def generate(self):
		return self.model.generate()


class ArrayModelField(GeneratedField):
	def __init__(self, model, min_length, max_length):
		self.model = model
		self.min_length = min_length
		self.max_length = max_length

	def generate(self):
		count = randint(self.min_length, self.max_length)
		return [
			self.model.generate()
			for _ in xrange(count)
		]


class GenerateModel(object):
	@classmethod
	def generate(cls):
		fields = {
			name: field
			for name, field in cls.__dict__.items()
			if isinstance(field, GeneratedField)
		}
		return {
			name: field.generate()
			for name, field in fields.items()
		}


	@classmethod
	def bulk_generate(cls, count):
		return (
			cls.generate()
			for _ in xrange(count)
		)
#######################


class Phone(GenerateModel):
	id = CharField(min_length=5, max_length=5, chars=CharField.NUMERIC_CHARS)


class Passport(GenerateModel):
	id = CharField(min_length=10, max_length=10, chars=CharField.ALPHA_NUMERIC_CHARS)


class Person(GenerateModel):
	age = IntegerField(min=20, max=30)
	name = CharField(min_length=5, max_length=10)
	gender = ChoiceField(['M', 'F', None])
	passport_number = ModelField(Passport)
	phones = ArrayModelField(Phone, min_length=1, max_length=3)

p = Person.generate()
print p

for p in Person.bulk_generate(10):
	print p