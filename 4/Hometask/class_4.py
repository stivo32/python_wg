# coding: utf-8

for i in xrange(1, 11):
    for j in xrange(2, 10):
        string_to_print = '{} x {} = {}'.format(j, i, j * i)
        print string_to_print, ' ' * (11 - len(string_to_print)),
    print
