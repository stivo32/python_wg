names_list = 'Kate Helen Max Eugen Olga'.split()

print [x[-1] for x in names_list]

vowel_names = [name for name in names_list if name[0].lower() in 'eyuioa']
print vowel_names, len(vowel_names)

print sorted(names_list, key=lambda name: name[-1])

print [
	name[::-1]
	for name in sorted([
		name1[::-1]
		for name1 in names_list
	])
]
