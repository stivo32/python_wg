# coding: utf-8

user_input = raw_input()

pluses = 0
minuses = 0

for symbol in user_input:
    if symbol == '+':
        pluses += 1
    if symbol == '-':
        minuses += 1
print '+: {}'.format('no one' if pluses == 0 else pluses)
print '-: {}'.format('no one' if minuses == 0 else minuses)
