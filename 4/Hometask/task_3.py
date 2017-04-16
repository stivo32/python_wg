# coding: utf-8
L = 5
R = 9
spaces = len(str(R * R))

for i in range(L - 1, R + 1):
    for j in range(L - 1, R + 1):
        if i == L - 1 and j == L - 1:
            print ' '.rjust(spaces),
            continue
        elif i == L - 1:
            i = 1
        elif j == L - 1:
            j = 1

        string_to_print = '{}'.format(j * i)
        print string_to_print.rjust(spaces),
    print
