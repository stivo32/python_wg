# coding: utf-8

user_input = raw_input()

input_len = len(user_input)
even_input = input_len % 2 == 0
if input_len < 2:
    print 'There is no "?"'
    exit()

first = user_input[:input_len / 2]
second = user_input[input_len / 2 if even_input else input_len / 2 + 1:]

first_qm = 0
second_qm = 0

for symbol in first:
    if symbol == '?':
        first_qm += 1
for symbol in second:
    if symbol == '?':
        second_qm += 1

if first_qm == second_qm:
    if first_qm == 0:
        print 'There is no "?"'
    else:
        print 'Equal'
elif first_qm > second_qm:
    print 'The first one'
else:
    print 'The second one'
