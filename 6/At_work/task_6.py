dataset = 'Name1:123433|Name2:6789556|Name1:5678933|Name2:12367833'.split('|')
# print dataset
list_of_phones = [row.split(':') for row in dataset]
db = {name: [] for name, phone in list_of_phones}
names = db.keys()

number_end = '33'


def printer(name, phones):
	print '{}: {}'.format(name, ', '.join(phones))


[
	db[name].append(phone)
	for name, phone in list_of_phones
]

[
	printer(name, phones)
	for name, phones in db.items()
]

people_with_number = {
	name: len([
		phone for phone in phones
		if phone.endswith(number_end)
	])
	for name, phones in db.items()
}
print people_with_number


