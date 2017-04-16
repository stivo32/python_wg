# coding: utf-8

max_number = 6

for i in xrange(max_number - 1, max_number / 2 - 1, -1):
    row_string = [' ']*(max_number - i - 1)
    for j in xrange(max_number / 2, i):
        row_string.append(str(j))
    for j in xrange(i, max_number / 2 -1, -1):
        row_string.append(str(j))
    print ''.join(row_string)
for i in xrange(max_number / 2 - 1, -1, -1):
    row_string = [' '] * i
    for j in xrange(max_number / 2 - 1, i, -1):
        row_string.append(str(j))
    for j in xrange(i, max_number / 2):
        row_string.append(str(j))
    print ''.join(row_string)
