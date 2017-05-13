# coding: utf-8

user_input = list(raw_input('>'))
count = user_input.count('0')

for i in xrange(count):
    user_input.remove('0')

print ''.join(user_input)

