# coding: utf-8

for i in range(0, 11):
    for j in range(0, 11):
        if i == 0 and j == 0:
            print ' '.rjust(3),
            continue
        elif i == 0:
            i = 1
        elif j == 0:
            j = 1

        string_to_print = '{}'.format(j * i)
        print string_to_print.rjust(3),
    print
