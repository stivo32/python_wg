# coding: utf-8

for i in range(1, 11):
    for j in range(2, 11):
        string_to_print = '{} x {} = {}'.format(j, i, j * i)
        print string_to_print, ' ' * (11 - len(string_to_print)),
    print
