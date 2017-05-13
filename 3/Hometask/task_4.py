# coding: utf-8

user_input = raw_input()

commas_index = ''
commas_count = 0
for i, symbol in enumerate(user_input):
    if symbol == ',':
        commas_count += 1
        commas_index += str(i) + ' '

print commas_count
print commas_index
