def create_file(file1, file2):
	new_file_name = file1.split('.')[0] + file2.split('.')[0] + '.txt'
	with open(file1) as f1, open(file2) as f2, open(new_file_name, 'w') as new_file:
		new_file.write(f1.read() + f2.read())
	print new_file_name


create_file(raw_input(), raw_input())