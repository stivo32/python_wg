def create_file(*files):
	new_file_name = 'result.txt'
	with open(new_file_name, 'w') as new_file:
		for file in files:
			with open(file) as f:
				data = f.read()
				new_file.write('=' * 20 + '\n')
				new_file.write(file + '\n')
				new_file.write('=' * 20 + '\n')
				new_file.write(data)

	print new_file_name

create_file(raw_input(), raw_input())