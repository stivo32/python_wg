dataset = 'Name1:number1|Name2:number2|Name1:number3|Name2:number4'.split('|')
print dataset
list_of_phones = [row.split(':') for row in dataset]
db = {name: [] for name, phone in list_of_phones}
names = db.keys()


def printer(name, phones):
	print '{}: {}'.format(name, ', '.join(phones))

[
	printer(
		name,
		[
			phone
			for internal_name, phone in list_of_phones
			if name == internal_name
		],
	)
	for name in names
]


[
	db[name].append(phone)
	for name, phone in list_of_phones
]

[
	printer(name, phones)
	for name, phones in db.items()
]


